import frappe
 
@frappe.whitelist()
def get_data():
    return ["Apple", "Orange", "Banana", "Grapes"]