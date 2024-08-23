import frappe
from frappe import _

@frappe.whitelist()
def get_article(article_name):
    if frappe.db.exists("Article", article_name):
        return True
    else:
        return False
    

@frappe.whitelist()
def articles(article, author,price):
    book = frappe.get_doc({
        'doctype': 'Article',
        'article_name': article ,
        'author': author,
        'price': price,
        'status': 'Available'
    })
    book.insert()
    return {'message': 'Article added successfully'}

@frappe.whitelist(methods = ["PUT"])
def update_article():
    try:
        data = frappe.request.json  
        if not data.get("name"):
            return {"status":"error","message": "Article name (ID) is required"}
        
        article = frappe.get_doc("Article", data['name'])

        if not article:
            return {"status": "error", "message": "Article not found"}
            
        article.update({
            "status":data.get('status'),
            "author":data.get("author")
        })

        article.save(ignore_permissions = True)
        frappe.db.commit()

        return {"Status":"Success","Message":"Article Updated","Article_id": article.name}
    
    except Exception as e:
        frappe.log_error(str(e)[:130], "Error in updating document")
        return {"Status":"error", "Message": "Updating failed check logs"}