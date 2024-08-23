import frappe

def execute():
    # Example: Add a default value to a new field 'category' in the 'Article' DocType
    frappe.db.sql("""
        UPDATE `tabArticle`
        SET genre = 'Science'
        WHERE genre IS NULL
    """)