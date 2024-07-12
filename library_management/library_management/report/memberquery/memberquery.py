# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt


# from __future__ import unicode_literals
# import frappe
# from frappe import _
# from frappe.utils.dateutils import get_from_date_from_timespan
# import calendar

# def execute(filters=None):
#     columns, data = get_columns(filters), get_data(filters)
#     return columns, data

# def get_columns(filters):
#     columns = []
#     if filters:
#         if filters.doc == 'Library Membership':
#             columns = get_columns_library_membership(filters)
#         if filters.doc == 'Library Transaction':
#             columns = get_columns_library_transaction(filters)
#     columns = get_columns_for_all_data()
#     return columns

# def get_data(filters):
#     data = []
#     if filters:
#         if filters.doc == 'Library Membership':
#             data = get_data_of_library_membership(filters)
#         if filters.doc == 'Library Transaction':
#             data = get_data_of_library_transaction(filters)
#     data = get_all_data()
#     return data

# def get_columns_library_membership(filters):
#     columns = [
#         {
#             'fieldname': 'library_member',
#             'label': _('Library Member'),
#             'fieldtype': 'Link',
#             'options': 'Library Member',
#         },
#         {
#             'fieldname': 'full_name',
#             'label': _('Full name'),
#             'fieldtype': 'Data',
#         },
#         {
#             'fieldname': 'from_date',
#             'label': _('From date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'to_date',
#             'label': _('To date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'paid',
#             'label': _('Paid'),
#             'fieldtype': 'Check',
#         }
#     ]
#     return columns

# def get_columns_library_transaction(filters):
#     columns = [
#         {
#             'fieldname': 'library_member',
#             'label': _('Library Member'),
#             'fieldtype': 'Link',
#             'options': 'Library Member',
#         },
#         {
#             'fieldname': 'date',
#             'label': _('Date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'type',
#             'label': _('Type'),
#             'fieldtype': 'Select',
#             'options': "\n Issue\n Return"
#         },
#         {
#             'fieldname': 'fine',
#             'label': _('Fine Amount'),
#             'fieldtype': 'Currency',
#         },
#         {
#             'fieldname': 'has_fine',
#             'label': _('Has Fine'),
#             'fieldtype': 'Check',
#         },
#         {
#             'fieldname': 'total_amount',
#             'label': _('Total Amount'),
#             'fieldtype': 'Float',
#         }
#     ]
#     return columns

# def get_data_of_library_membership(filters):
#     data = []
#     fields = "library_member,full_name,from_date,to_date,paid"

#     query = """
#         SELECT
#             {fields}
#         FROM
#             `tabLibrary Membership`
#         WHERE
#             1
#     """.format(fields=fields)

#     if filters.from_date and filters.to_date:
#         query += " AND creation BETWEEN '{from_date}' AND '{to_date}'".format(from_date=filters.from_date, to_date=filters.to_date)

#     data = frappe.db.sql(query, as_dict=True)
#     return data

# def get_data_of_library_transaction(filters):
#     data = []
#     fields = "library_member,date,type,fine,has_fine,total_amount"

#     query = """
#         SELECT
#             {fields}
#         FROM
#             `tabLibrary Transaction`
#         WHERE
#             1
#     """.format(fields=fields)

#     if filters.from_date and filters.to_date:
#         query += " AND date BETWEEN '{from_date}' AND '{to_date}'".format(from_date=filters.from_date, to_date=filters.to_date)

#     data = frappe.db.sql(query, as_dict=True)
#     return data

# def get_columns_for_all_data():
#     return []

# def get_all_data(data):
#     return data
# from __future__ import unicode_literals
# import frappe
# from frappe import _

# def execute(filters=None):
#     columns, data = get_columns(filters), get_data(filters)
#     return columns, data

# def get_columns(filters):
#     if filters:
#         if filters.doc == 'Library Membership':
#             return get_columns_library_membership(filters)
#         elif filters.doc == 'Library Transaction':
#             return get_columns_library_transaction(filters)
#     return get_columns_for_all_data()

# def get_data(filters):
#     if filters:
#         if filters.doc == 'Library Membership':
#             return get_data_of_library_membership(filters)
#         elif filters.doc == 'Library Transaction':
#             return get_data_of_library_transaction(filters)
#     return get_all_data(filters)

# def get_columns_library_membership(filters):
#     return [
#         {
#             'fieldname': 'library_member',
#             'label': _('Library Member'),
#             'fieldtype': 'Link',
#             'options': 'Library Member',
#         },
#         {
#             'fieldname': 'full_name',
#             'label': _('Full name'),
#             'fieldtype': 'Data',
#         },
#         {
#             'fieldname': 'from_date',
#             'label': _('From date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'to_date',
#             'label': _('To date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'paid',
#             'label': _('Paid'),
#             'fieldtype': 'Check',
#         }
#     ]

# def get_columns_library_transaction(filters):
#     return [
#         {
#             'fieldname': 'library_member',
#             'label': _('Library Member'),
#             'fieldtype': 'Link',
#             'options': 'Library Member',
#         },
#         {
#             'fieldname': 'date',
#             'label': _('Date'),
#             'fieldtype': 'Date',
#         },
#         {
#             'fieldname': 'type',
#             'label': _('Type'),
#             'fieldtype': 'Select',
#             'options': "\n Issue\n Return"
#         },
#         {
#             'fieldname': 'fine',
#             'label': _('Fine Amount'),
#             'fieldtype': 'Currency',
#         },
#         {
#             'fieldname': 'has_fine',
#             'label': _('Has Fine'),
#             'fieldtype': 'Check',
#         },
#         {
#             'fieldname': 'total_amount',
#             'label': _('Total Amount'),
#             'fieldtype': 'Float',
#         }
#     ]

# def get_data_of_library_membership(filters):
#     fields = "library_member, full_name, from_date, to_date, paid"
#     query = """
#         SELECT
#             {fields}
#         FROM
#             `tabLibrary Membership`
#         WHERE
#             1
#     """.format(fields=fields)

#     if filters.from_date and filters.to_date:
#         query += " AND creation BETWEEN '{from_date}' AND '{to_date}'".format(from_date=filters.from_date, to_date=filters.to_date)

#     return frappe.db.sql(query, as_dict=True)

# def get_data_of_library_transaction(filters):
#     fields = "library_member, date, type, fine, has_fine, total_amount"
#     query = """
#         SELECT
#             {fields}
#         FROM
#             `tabLibrary Transaction`
#         WHERE
#             1
#     """.format(fields=fields)

#     if filters.from_date and filters.to_date:
#         query += " AND date BETWEEN '{from_date}' AND '{to_date}'".format(from_date=filters.from_date, to_date=filters.to_date)

#     return frappe.db.sql(query, as_dict=True)

# def get_columns_for_all_data():
#     return [
#         {
#             'fieldname': 'library_member_name',
#             'label': _('Library Member Name'),
#             'fieldtype': 'Data',
#         },
#         {
#             'fieldname': 'full_name',
#             'label': _('Full Name'),
#             'fieldtype': 'Data',
#         },
#         {
#             'fieldname': 'membership_name',
#             'label': _('Membership Name'),
#             'fieldtype': 'Data',
#         },
#         {
#             'fieldname': 'library_member',
#             'label': _('Library Member'),
#             'fieldtype': 'Link',
#             'options': 'Library Member',
#         }
#     ]

# def get_all_data(filters):
#     query = """
#         SELECT
#             lm.name as library_member_name,
#             lm.full_name,
#             lmp.name as membership_name,
#             lmp.library_member
#         FROM
#             `tabLibrary Member` lm
#         LEFT JOIN
#             `tabLibrary Membership` lmp ON lmp.library_member = lm.name
#     """

#     return frappe.db.sql(query, as_dict=True)

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(filters), get_data(filters)
    return columns, data

def get_columns(filters):
    if filters:
        if filters.doc == 'Library Membership':
            return get_columns_library_membership(filters)
        elif filters.doc == 'Library Transaction':
            return get_columns_library_transaction(filters)
    return get_columns_for_all_data()

def get_data(filters):
    if filters:
        if filters.doc == 'Library Membership':
            return get_data_of_library_membership(filters)
        elif filters.doc == 'Library Transaction':
            return get_data_of_library_transaction(filters)
    return get_all_data(filters)

def get_columns_library_membership(filters):
    return [
        {
            'fieldname': 'library_member',
            'label': _('Library Member'),
            'fieldtype': 'Link',
            'options': 'Library Member',
        },
        {
            'fieldname': 'full_name',
            'label': _('Full Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'from_date',
            'label': _('From Date'),
            'fieldtype': 'Date',
            'width': 250
        },
        {
            'fieldname': 'to_date',
            'label': _(' Date'),
            'fieldtype': 'To Date',
            'width': 250
        }
    ]
    fields = "library_member, full_name, from_date, date, paid"
    query = """
        SELECT
            {fields}
        FROM
            `tabLibrary Membership`
        WHERE
            1
    """.format(fields=fields)

    if filters.from_date and filters.date:
        query += " AND creation BETWEEN '{from_date}' AND '{to_date}'".format(from_date=filters.from_date,to_date=filters.to_date)

    return frappe.db.sql(query, as_dict=True)

def get_data_of_library_transaction(filters):
    fields = "library_member, date, type, fine, has_fine, total_amount"
    query = """
        SELECT
            {fields}
        FROM
            `tabLibrary Transaction`
        WHERE
            1
    """.format(fields=fields)

    if filters.from_date and filters.date:
        query += " AND date BETWEEN '{from_date}' AND '{date}'".format(from_date=filters.from_date, date=filters.to_date)

    return frappe.db.sql(query, as_dict=True)

def get_columns_for_all_data():
    return [
        {
            'fieldname': 'first_name',
            'label': _('First Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'last_name',
            'label': _('Last Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'from_date',
            'label': _('From Date'),
            'fieldtype': 'Date',
        },
        {
            'fieldname': 'to_date',
            'label': _('To Date'),
            'fieldtype': 'Date',
        }
    ]

def get_all_data(filters):
    query = """
        SELECT
            lm.first_name as first_name,
            lm.last_name as last_name,
            lmp.from_date,
            lmp.to_date
        FROM
            `tabLibrary Member` lm
        LEFT JOIN
            `tabLibrary Membership` lmp ON lmp.library_member = lm.name
    """

    return frappe.db.sql(query, as_dict=True)
