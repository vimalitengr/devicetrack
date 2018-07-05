# -*- coding: utf-8 -*-
# Copyright (c) 2018, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from urllib2 import Request, urlopen, URLError
import datetime
import json
import requests

class APITestEnvironment(Document):
	pass

@frappe.whitelist()
def entry_using_api_call():
	# Get from datetime and to datetime
	#from_datetime = datetime.datetime.now()- datetime.timedelta(minutes=60)
	#to_datetime = datetime.datetime.now()
	#frappe.errprint(from_datetime)

	from_datetime = datetime.datetime.now()- datetime.timedelta(minutes=60)
	to_datetime = datetime.datetime.now()
	
	# Set fromdate and todate.
	from_date = from_datetime.date()
	to_date = to_datetime.date()

	# set fromtime and totime.
	from_time = from_datetime.time()
	to_time = to_datetime.time()
	frappe.errprint(from_time)

	# Get device list.
	device_list = frappe.db.sql("""SELECT device_id FROM `tabDevice` WHERE status='A'""",(),as_dict = 1)
	
	# Loop over all the device.
	for device in device_list:
		# Get Url and it's parameter from tracking API Setup
		url = frappe.db.get_value("Tracking API Setup",None,"api_url")
		url+= '&' + str(frappe.db.get_value("Tracking API Setup",None,"parameter_1_device_id")) + "="+ str(device.device_id)
		url+= '&' + str(frappe.db.get_value("Tracking API Setup",None,"parameter_2_from_date")) + "="+ str(from_date)
		url+= '&' + str(frappe.db.get_value("Tracking API Setup",None,"parameter_3_to_date")) + "="+ str(to_date)
		url+= '&' + str(frappe.db.get_value("Tracking API Setup",None,"parameter_4_from_time")) + "="+ str(":".join(str(from_time).split(":", 2)[:2]))
		url+= '&' + str(frappe.db.get_value("Tracking API Setup",None,"parameter_5_to_time")) + "="+ str(":".join(str(to_time).split(":", 2)[:2]))
        
		frappe.msgprint(url)
		# Make request to the url.
		request = requests.get(url)

		# Get response in json format.
		data = request.json()

		# Convert response to list.
		data_list = list(data['items']) 
        	#frappe.errprint(data_list)
		
		# List to check duplicate row id
        	rawid_obj=list()

		# Loop over the response.
		for item in data_list:
			
			for i in item["items"]:				
				if i['id'] not in rawid_obj:
         	   			rawid_obj.append(i['id'])
           				#frappe.errprint(rawid_obj)
					# Make Tracking Entry dict
					TrackingDict = {"doctype": "Tracking Data", 
					"device_id": i['device_id'] or 0, 
					"dt":  i['raw_time'] or '',  
					"lat": i['lat'] or 0, 
					"lng": i['lng'] or 0,
					"altitude": i['altitude'] or 0, 
					"speed": i['speed'] or 0, 
					}	 
					for j in range(len(i["other_arr"])):		 
							if str(i["other_arr"][j].split(":")[0].strip())=="sat":
 								TrackingDict["sat"] = i["other_arr"][j].split(":")[1].strip()
	
							if str(i["other_arr"][j].split(":")[0].strip())=="di1":
 								TrackingDict["di1"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="di2":
 								TrackingDict["di2"] = i["other_arr"][j].split(":")[1].strip()
						
							if str(i["other_arr"][j].split(":")[0].strip())=="di3":
 								TrackingDict["di3"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="out1":
 								TrackingDict["out1"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="out2" :
 								TrackingDict["out2"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="adc1":
 								TrackingDict["adc1"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="adc2" :
 								TrackingDict["adc2"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="rssi":
 								TrackingDict["rssi"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="power":
 								TrackingDict["power"] = i["other_arr"][j].split(":")[1].strip()

							if str(i["other_arr"][j].split(":")[0].strip())=="battery":
 								TrackingDict["battery"] = i["other_arr"][j].split(":")[1].strip()
	
							if str(i["other_arr"][j].split(":")[0].strip())=="temp1":
 								TrackingDict["temp1"] = i["other_arr"][j].split(":")[1].strip()
			
							if str(i["other_arr"][j].split(":")[0].strip())=="temp2":
 								TrackingDict["temp2"] = i["other_arr"][j].split(":")[1].strip()
		
							if str(i["other_arr"][j].split(":")[0].strip())=="io16":
 								TrackingDict["odometer"] = i["other_arr"][j].split(":")[1].strip()
	
							if str(i["other_arr"][j].split(":")[0].strip())=="totaldistance":
 								TrackingDict["totaldistance"] = i["other_arr"][j].split(":")[1].strip()

				    	# Make Tracking Entry object
					TE = frappe.get_doc(TrackingDict)
					
					# Insert and save object.
					TE.insert()
					TE.save()
					frappe.db.commit()
					#frappe.msgprint(str(TE.name))
	return 1			