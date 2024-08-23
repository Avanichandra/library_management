import frappe

def get_context(context):
    context.articles = frappe.get_all('Article', fields=['article_name', 'author', 'description', 'image'])
