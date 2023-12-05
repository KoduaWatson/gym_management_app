# Copyright (c) 2023, Watson Kodua Acheampong and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	total_revenue = 0.0
	columns, data = [
		{
			'label': 'Class Name',
			'fieldname': 'class_name',
			'fieldtype': 'Data',
			'width': 250
		},
		{
			'label': 'Revenue',
			'fieldname': 'revenue',
			'fieldtype': 'Currency',
			'width': 250
		}
	],[]

	records = frappe.db.get_all('Group Class Booking', fields=['class_name', 'price_of_class'])

	revenue_by_group_class = {}

	for record in records:
		if record.class_name in revenue_by_group_class:
			revenue_by_group_class[record.class_name] = revenue_by_group_class[record.class_name] + record.price_of_class
		else:
			revenue_by_group_class[record.class_name] = record.price_of_class
		
	for class_name, price_of_class in revenue_by_group_class.items():
		data.append(frappe._dict({'class_name': class_name, 'revenue': price_of_class}))
		total_revenue += price_of_class

	
	report_summary = [
		{
			"value": total_revenue,
			"indicator": "Green" if total_revenue is not None else "Red",
			"label": ("Total Revenue"),
			"datatype": "Currency",
			"currency": "Sh"
		}
	]
	

	chart = {
		"data":{
			"labels": [d.class_name for d in data],
			"datasets": [
				{
					"name": "Revenue by Class",
					"values": [d.revenue for d in data]
				}
			]
		},
		"type": "donut"
	}
	
	data.append(frappe._dict({'class_name': 'Total', 'revenue': total_revenue}))

	return columns, data, None, chart, report_summary
