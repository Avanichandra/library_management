# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

import frappe
from frappe.model.document import Document

class LibraryMember(Document):
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
        print("Updated full name:", self.full_name)

    def on_submit(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'  # Ensure full_name is up-to-date
        self.save()  # Save the LibraryMember document before creating the user
        create_user_for_library_member(self)

def create_user_for_library_member(self):
    # Check if required fields are set
    if not (self.first_name and self.last_name and self.email_address):
        frappe.throw("First name, last name, or email address cannot be empty.")

    # Check if a User with the same email already exists
    if not frappe.db.exists("User", self.email_address):
        # Create a new User based on Library Member data
        user = frappe.get_doc({
            "doctype": "User",
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email_address,
            "username": self.full_name,
            "role_profile_name": 'Library Member',
            "enabled": 1,
        })
        user.insert(ignore_permissions=True)
        print("New role created for user:", user.name)
        frappe.msgprint(f"User {user.name} created for Library Member {self.name}.")
    else:
        frappe.msgprint(f"A user with email {self.email_address} already exists.")

