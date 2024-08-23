# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt

# import frappe


# from __future__ import unicode_literals
# 
from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    """
    Generates a report with library member details including membership status and current articles.
    
    Args:
        filters (dict, optional): Dictionary containing filter values for the report.
    
    Returns:
        columns (list): List of dictionaries defining the columns of the report.
        data (list): List of dictionaries containing the member data for the report.
    """
    columns = [
        {
            'fieldname': 'full_name',
            'label': _('Full Name'),
            'fieldtype': 'Data',
            'width': 250
        },
        {
            'fieldname': 'email_address',
            'label': _('Email Address'),
            'fieldtype': 'Data',
            'width': 250
        },
        {
            'fieldname': 'phone',
            'label': _('Phone'),
            'fieldtype': 'Data',
            'width': 150
        },
        {
            'fieldname': 'membership_status',
            'label': _('Membership Status'),
            'fieldtype': 'Data',
            'width': 150
        },
        {
            'fieldname': 'current_articles',
            'label': _('Current Articles Held'),
            'fieldtype': 'Data',
            'width': 250
        },
    ]

    today = frappe.utils.nowdate()

    query = """
        SELECT
            lm.full_name,
            lm.email_address,
            lm.phone,
            lm.name AS member_name,
            'Valid Membership' AS membership_status,
            GROUP_CONCAT(DISTINCT current_articles.article_name 
            ORDER BY current_articles.article_name SEPARATOR ', ') AS current_articles
        FROM
            `tabLibrary Member` lm
        LEFT JOIN (
            SELECT
                lmem.library_member
            FROM
                `tabLibrary Membership` lmem
            WHERE
                lmem.docstatus = 1
                AND lmem.from_date <= %(today)s
                AND lmem.to_date >= %(today)s
            ORDER BY
                lmem.from_date DESC
        ) membership ON lm.name = membership.library_member
        LEFT JOIN (
            SELECT
                lt.library_member,
                la.article AS article_name
            FROM
                `tabLibrary Transaction` lt
            JOIN
                `tabAdd Article` la ON lt.name = la.parent
            LEFT JOIN (
                SELECT
                    library_member,
                    article,
                    MAX(date) AS last_return_date
                FROM
                    `tabLibrary Transaction`
                WHERE
                    type = 'Return'
                    AND docstatus = 1
                GROUP BY
                    library_member, article
            ) returns ON returns.library_member = lt.library_member 
            AND returns.article = la.article
            WHERE
                lt.type = 'Issue'
                AND lt.docstatus = 1
                AND (returns.last_return_date IS NULL OR lt.date > returns.last_return_date)
        ) current_articles ON lm.name = current_articles.library_member
        GROUP BY
            lm.full_name, lm.email_address, lm.phone, lm.name
    """

    members_data = frappe.db.sql(query, {"today": today}, as_dict=True)

    data = []

    for member in members_data:
        data.append({
            'full_name': member["full_name"],
            'email_address': member["email_address"],
            'phone': member["phone"],
            'membership_status': member["membership_status"],
            'current_articles': member["current_articles"] if member["current_articles"] else "No Articles Issued"
        })

    return columns, data
