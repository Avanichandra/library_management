# Copyright (c) 2024, Avani and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
    def before_submit(self):
        if not self.articles:
            frappe.throw("At least one article must be added before submitting")

        if self.type == "Issue":
            self.validate_issue()
            self.validate_maximum_limit()
            for article_entry in self.articles:
                article = frappe.get_doc("Article", article_entry.article)
                article.status = "Issued"  # Note: Need to add "Issued" to Article status options
                article.save()

        elif self.type == "Return":
            self.validate_return()
            for article_entry in self.articles:
                article = frappe.get_doc("Article", article_entry.article)
                article.status = "Available"
                article.save()

    def validate(self):
        self.validate_amount()

    def validate_issue(self):
        self.validate_membership()
        for article_entry in self.articles:
            article = frappe.get_doc("Article", article_entry.article)
            if article.status == "Issued":  # Note: Need to add "Issued" to Article status options
                frappe.throw(f"Article {article.name} is already issued by another member")

    def validate_return(self):
        for article_entry in self.articles:
            article = frappe.get_doc("Article", article_entry.article)
            if article.status == "Available":
                frappe.throw(f"Article {article.name} cannot be returned without being issued first")

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
        count = frappe.db.count(
            "Library Transaction",
            {"library_member": self.library_member, "type": "Issue", "docstatus": DocStatus.submitted()}
        )
        if count + len(self.articles) > max_articles:
            frappe.throw("Maximum limit reached for issuing articles")

    def validate_membership(self):
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            }
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")

    
    def validate_amount(self):
        total_amount = self.total_amount
        actual_total_amount = 0
        for article_entry in self.articles:
            if article_entry.amount:
                actual_total_amount += article_entry.amount

        if total_amount != actual_total_amount:
            frappe.throw("Total amount is incorrect")

  





    
    



            
@frappe.whitelist()
def check_has_fine(doc):
    if frappe.db.exists('Library Transaction' , doc.name, {"has_fine" : True}):
        return 1
    else: 
        return 0

@frappe.whitelist()
def create_fine_document(fine_amount,reason_for_fine, library_transaction):
        fine_doc = frappe.get_doc({
            'doctype': 'Library Fine',
            'fine_amount': fine_amount,
            'reason_for_fine': reason_for_fine,
            'library_transaction':library_transaction
        })
        fine_doc.insert()
        frappe.db.commit()
        return fine_doc.name
   
#         frappe.throw(f"Error creating fine document: {e}")

@frappe.whitelist()
def custom_query(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql('''
        SELECT 
            last_name
        FROM 
            library_member
        WHERE 
            last_name = 'Jance'

    ''')
    

