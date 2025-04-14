import frappe

def execute():
    vehicles = frappe.db.get_all("Vehicle", pluck="name")
    for vehicle in vehicles:
        doc = frappe.get_doc("Vehicle", vehicle)
        doc.set_title()
        doc.save()
    frappe.db.commit()