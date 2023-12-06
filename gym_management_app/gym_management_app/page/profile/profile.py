import frappe

@frappe.whitelist()
def membership_details():
    details = frappe.db.get_all('Gym Membership', fields = \
                             ['member_name', 'member_id', 'start_date', 'end_date', \
                            'allocated_trainer', 'trainer_contact', 'workout_plan'])
    return details

@frappe.whitelist()
def get_profile_html(pagename="profile"):
    
    return frappe.render_template("gym_management_app/gym_management_app/page/profile/profile.html")
