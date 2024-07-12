// Copyright (c) 2024, Avani and contributors
// For license information, please see license.txt
frappe.ui.form.on('Library Membership', {
    from_date: function(frm) {
        if (frm.doc.from_date && frm.doc.to_date && (frm.doc.to_date < frm.doc.from_date)) {
            frm.set_value('from_date', "");
            frappe.throw({
                message: __("To Date should be later than From Date"),
                indicator: 'red'
            });
        }
    },
    to_date: function(frm) {
        if (frm.doc.from_date && frm.doc.to_date && (frm.doc.to_date < frm.doc.from_date)) {
            frm.set_value('to_date', "");
            frappe.throw({
                message: __("<b>To Date</b> should be later than From Date"),
                indicator: 'red'
            });
        }
    },
    refresh: function(frm) {
        
        frm.add_custom_button('FINE', () => {
            let d = new frappe.ui.Dialog({
                title: 'Enter details',
                fields: [
                    {
                        label: 'Amount',
                        fieldname: 'amount',
                        fieldtype: 'Currency'
                    },
                    {
                        label: 'Date',
                        fieldname: 'date',
                        fieldtype: 'Date'
                    },
                    
                ],
                size: 'small', // small, large, extra-large 
                primary_action_label: 'Submit',
                primary_action(values) {
                    console.log(values);
                    d.hide();
                }
            });
            
            d.show();
              
        });cd

    }
});

