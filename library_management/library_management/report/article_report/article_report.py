# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt

# import frappe


from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = [
		{
			'fieldname': 'article_name',
			'label': _('Article name'),
			'fieldtype': 'Data',

			'width':250
		},
		{
            'fieldname': 'status',
            'label': _('Status'),
            'fieldtype': 'Select',
            'options': "\n Available\n Return"
        },
		
		{
			'fieldname': 'isbn',
			'label': _('ISBN'),
			'fieldtype': 'Data',

			'width':450
		},
		
		
		{
			'fieldname': 'publisher',
			'label': _('Publisher'),
			'fieldtype': 'Data',
			'width':450
		}
	]
	

	data = frappe.db.get_list("Article", fields=["article_name","status","isbn","publisher"])

	return columns, data


