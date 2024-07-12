# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns = [
		{
			'fieldname': 'first_name',
			'label': _('First Name'),
			'fieldtype': 'Data',
			
			'width':250
		},
		{
			'fieldname': 'email_address',
			'label': _('Email Address'),
			'fieldtype': 'Data',
			'options': 'Email',


			'width':250
		},
		{
			'fieldname': 'phone',
			'label': _('Phone'),
			'fieldtype': 'Data',
		}
	]

	data = frappe.db.get_list("Library Member", fields=["first_name", "email_address", "phone"])

	return columns, data