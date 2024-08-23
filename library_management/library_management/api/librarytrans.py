import frappe

@frappe.whitelist(allow_guest=False)  # Set allow_guest=True if you want to allow unauthenticated access
def get_transaction_details(name):
    try:
        # Fetch the transaction document
        transaction = frappe.get_doc("Library Transaction", name)
        
        # Prepare the response data
        response = {
            "name": transaction.name,
            "library_member": transaction.library_member,
            "total_amount": transaction.total_amount,
            "add_articles": []
        }

        # Add details of child table "Add Article"
        for article in transaction.add_more:
            response["add_articles"].append({
                "article": article.article,
                "amount": article.amount,
                "shelf_name1": article.row,
                "shelf_name2": article.shelf
            })

        return response

    except frappe.DoesNotExistError:
        return {"message": "Transaction not found"}
    except Exception as e:
        return {"exc": str(e), "exc_type": str(type(e))}


import frappe

@frappe.whitelist(allow_guest=False)
def add_transaction(library_member, total_amount, date, add_articles):
    try:
        # Check if the Library Member exists
        if not frappe.db.exists("Library Member", library_member):
            return {"status": "error", "message": f"Could not find Library member: {library_member}"}

        # Prepare the transaction document
        transaction = frappe.get_doc({
            "doctype": "Library Transaction",
            "library_member": library_member,
            "total_amount": total_amount,
            "date": date,
            "add_article": add_articles  # Ensure this matches the child table field name
        })

        # Insert the document
        transaction.insert()

        # Commit the transaction to the database
        frappe.db.commit()

        return {"status": "success", "message": "Transaction added successfully", "transaction_id": transaction.name}
    
    except Exception as e:
        # Log the exception for debugging
        frappe.log_error(frappe.get_traceback(), "Error adding transaction")
        return {"status": "error", "message": str(e)}
