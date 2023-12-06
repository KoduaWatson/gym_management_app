import frappe

def execute():
    current_pricelist = frappe.db.get_all('Group Class Pricelist', fields=['name', 'price'])

    for price in current_pricelist:
        if price.name == 'Zumba/Fitness Dance':
            frappe.db.set_value('Group Class Pricelist', 'price', 280, update_modified=False)
        
        elif price.name == 'Yoga Class':
            frappe.db.set_value('Group Class Pricelist', 'price', 250, update_modified=False)

        elif price.name == 'Spinning/Cycling Class':
            frappe.db.set_value('Group Class Pricelist', 'price', 200, update_modified=False)

        elif price.name == 'Senior Fitness Class':
            frappe.db.set_value('Group Class Pricelist', 'price', 130, update_modified=False)

        elif price.name == 'Mindfulness Meditation':
            frappe.db.set_value('Group Class Pricelist', 'price', 230, update_modified=False)

        elif price.name == 'Boxing/Kickboxing Class':
            frappe.db.set_value('Group Class Pricelist', 'price', 210, update_modified=False)