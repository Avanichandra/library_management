// Copyright (c) 2024, Avani and contributors
// For license information, please see license.txt

frappe.query_reports["Memberquery"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": __("From date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
        },
        {
            "fieldname": "to_date",
            "label": __("To date"),
            "fieldtype": "Date",
            "default": frappe.datetime.nowdate(),
        }
    ]
};



