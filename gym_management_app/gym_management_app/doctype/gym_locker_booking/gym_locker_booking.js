// Copyright (c) 2023, Watson Kodua Acheampong and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Locker Booking", {
	refresh(frm) {

        frm.set_query("locker_id", function() {
            return {
                "filters": {
                    "availability": "Available"
                }
            };
        });
	},
});
