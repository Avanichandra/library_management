import frappe

def create_user_for_library_member(doc, method):
    # Check if required fields are set
    if not (doc.first_name and doc.last_name and doc.email_address):
        frappe.throw("First name, last name, or email address cannot be empty.")

    # Check if a User with the same email already exists
    if not frappe.db.exists("User", doc.email_address):
        # Create a new User based on Library Member data
        user = frappe.get_doc({
            "doctype": "User",
            "first_name": doc.first_name,
            "last_name": doc.last_name,
            "email": doc.email_address,
            "username": f"{doc.first_name} {doc.last_name or ''}",
            "role_profile_name": 'Library Member',
            "enabled": 1,
        })
        user.insert(ignore_permissions=True)
        print("New user created:", user.name)
        frappe.msgprint(f"User {user.name} created for Library Member {doc.name}.")
    else:
        frappe.msgprint(f"A user with email {doc.email_address} already exists.")
