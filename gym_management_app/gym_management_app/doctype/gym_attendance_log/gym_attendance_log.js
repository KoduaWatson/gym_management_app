// Copyright (c) 2023, Watson Kodua Acheampong and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Attendance Log", {
	onload(frm) {

        // frappe.call({
        //     method: 'frappe.utils.now_datetime',
        //     callback: function (r) {
        //         // Parse the response to get the time
        //         const currentTime = frappe.datetime.str_to_user(r.message);
                
        //         // Set the value in the 'current_time_field' field
        //         frm.set_value(frm.doc.in_time, currentTime);
    
        //         // Show a message or perform additional actions if needed
        //         frappe.msgprint(__('Current time is: {0}', [currentTime]));
        //     }
        // });

    }
})
    
//         const current_timestamp = frappe.utils.datetime.now()

//         // Convert the string to a Date object
//         const dateTime = new Date(current_timestamp);

//         // Extract hours, minutes, and seconds
//         const hours = dateTime.getHours().toString().padStart(2, '0');
//         const minutes = dateTime.getMinutes().toString().padStart(2, '0');
//         const seconds = dateTime.getSeconds().toString().padStart(2, '0');

//         // Formatted time string
//         frm.doc.in_time = `${hours}:${minutes}:${seconds}`;


// 	},
// });
