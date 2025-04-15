// Copyright (c) 2025, BWM and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm) {

    },
	refresh(frm) {
        if (frm.doc.status === "New") {
            frm.add_custom_button("Accept Order",() => {
                frm.set_value("status", "Accepted");
                frm.save();
            }, "Actions")
            frm.add_custom_button("Rejected Order",() => {
                frm.set_value("status", "Rejected");
                frm.save();
            }, "Actions")    
        }
        
    }
});
