import frappe

@frappe.whitelist()
def get_profile_html():
    
    return frappe.render_template("gym_management_app/gym_management_app/page/template/newprofile.html")