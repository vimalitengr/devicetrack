# -*- coding: utf-8 -*-
# Copyright (c) 2018, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import add_to_date,format_time, cstr, getdate, formatdate


class DeviceTemperatureGraph(Document):
	def _get_chart_data(self):
		columns = self.get_columns()
		# chart, data, labels = self.get_chart_data(columns)

		return columns

	def get_chart_data(filters, columns):
		pass
		# for example
		# labels = ["0:00","4:00","8:00", "12:00","16:00","20:00"]
		
		# lab_list = []
		# time_list = []

		# for i in range(len(columns)):
		# 	if i+1 < len(columns):
		# 		time_list.append((columns[i], columns[i+1]))			
		# 		lab_list.append(format_time(columns[i])+"-"+format_time(columns[i+1]))			
		# if filters.get("from_date") == filters.get("to_date"):			
		# 	labels = lab_list
		# else:		
		# 	labels = columns[:-1]

		# data_vals = get_data_vals(time_list)
		# data = []
		# datasets = []
		# for l in data_vals:
		# 	datasets.append({'title': '&#8451;', 'values': l})
		# 	data.append(l)

		# # for example 
		# # datasets.append({'title': 'Temperature', 'values': [41,40,41,45,41,44]})
		# # datasets.append({'title': 'Temperature', 'values': [36,-38,45,42,33,30]})

		# chart = {
		# 	"data": {
		# 		'labels': labels,
		# 		'datasets': datasets
		# 	},
		# 	"colors": ['light-blue']*len(datasets),	
		# 	"isNavigable": 1,		
		# }
		# chart["type"] = "bar"
	
		# return chart, data, labels	

	def get_columns(self):
		from datetime import datetime, timedelta
		c_list = [self.from_date]
		new_date =self.from_date
		if self.from_date == self.to_date:
			end_date = add_to_date(date = self.from_date,days=1 )
			
			while (new_date < end_date):	
				new_date = add_to_date(new_date,hours=4 )
				c_list.append(new_date)
		else:
			end_date = add_to_date(date =self.to_date,days=1 )
			end_date = self.to_date
			while (new_date <= end_date):	
				new_date = add_to_date(new_date,days=1 )
				c_list.append(new_date)
		# frappe.throw(cstr(c_list))				
		return c_list	

	def get_chart_data(self):
		end_date = add_to_date(date = self.to_date,days=1 )
		temperature_data = frappe.db.sql("""SELECT t1.dt as date, t1.temp1 as temperature FROM `tabTracking Data` t1 where t1.dt BETWEEN %s AND %s order by t1.dt""",(self.from_date, end_date), as_list=1)	
		# clm_ticks = frappe.db.sql("""SELECT Distinct date(t1.show) FROM `tabTracking Data` t1 where t1.show BETWEEN %s AND %s order by t1.show""",(self.from_date, end_date), as_list=1)
		# frappe.msgprint(str(clm_ticks))
		if temperature_data:
			# frappe.msgprint(cstr(tem_data))
			temperature_data = [["Date","Temperature"]]+temperature_data
			return temperature_data
		else:
			return [["Date - Time","Temperature"]]
