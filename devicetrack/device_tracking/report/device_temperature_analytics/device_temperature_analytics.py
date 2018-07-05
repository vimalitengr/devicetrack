# Copyright (c) 2013, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import add_to_date,format_time, cstr, getdate,formatdate

def execute(filters=None):
	columns, data = [], []	
	columns = get_columns(filters)
	
	chart, data, labels = get_chart_data(filters, columns)
	columns = columns[:-1]
	return columns, data, None, chart

def get_chart_data(filters, columns):
	
	# for example
	# labels = ["0:00","4:00","8:00", "12:00","16:00","20:00"]
	
	lab_list = []
	time_list = []

	for i in range(len(columns)):
		if i+1 < len(columns):
			time_list.append((columns[i], columns[i+1]))			
			lab_list.append(format_time(columns[i])+"-"+format_time(columns[i+1]))			
	if filters.get("from_date") == filters.get("to_date"):			
		labels = lab_list
	else:		
		labels = columns[:-1]

	data_vals = get_data_vals(time_list)
	data = []
	datasets = []

	for l in data_vals:
		# frappe.msgprint(cstr(l))
		datasets.append({'title': '&#8451;', 'values': l})
		data.append(l)

	# for example 
	# datasets.append({'title': 'Temperature', 'values': [41,40,41,45,41,44]})
	# datasets.append({'title': 'Temperature', 'values': [36,-38,45,42,33,30]})

	chart = {
		"data": {
			'labels': labels,
			'datasets': datasets
		},
		"colors": ['light-blue']*len(datasets),	
		"isNavigable": 1
		
	}
	chart["type"] = "bar"
	chart["barOptions"] = {
	        "spaceRatio": 0	       
	      }	
	return chart, data, labels

def get_columns(filters):
	from datetime import datetime, timedelta
	c_list = [filters.get('from_date')]
	new_date = filters.get('from_date')
	if filters.get('from_date') == filters.get('to_date'):
		end_date = add_to_date(date =filters.get('from_date'),days=1 )
		
		while (new_date < end_date):	
			new_date = add_to_date(new_date,hours=4 )
			c_list.append(new_date)
	else:
		end_date = add_to_date(date =filters.get('to_date'),days=1 )
		end_date = filters.get('to_date')
		while (new_date <= end_date):	
			new_date = add_to_date(new_date,days=1 )
			c_list.append(new_date)
	# frappe.throw(cstr(c_list))				
	return c_list

def get_data_vals(time_list):
	d = {}
	z = []
	r_len = []
	for i in time_list:	
		a = []
		temperature_data = frappe.db.sql("""SELECT other_adc1 from `tabTracking Entry` t1 where t1.items_raw_time BETWEEN %s AND %s order by t1.items_raw_time""",(i[0], i[1]), as_dict=1)
		for j in temperature_data:
			a.append(j.other_adc1)
		
		d[str(str(i[0])+"-"+str(i[1]))] = a	
		z.append(a)
		r_len.append(len(a))
	
	max_len = max(r_len)
	
	y = []
	for k in z:
		if len(k) < max_len:
			y.append(k+[0]*(max_len-len(k))) 
		else:
			y.append(k)	

	rez = [[y[j][i] for j in range(len(y))] for i in range(len(y[0]))]	

	return rez	