// Copyright (c) 2024, Avani and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Transaction", {
//     onload(frm) {
//         frm.set_query('library_member', () => {
//             return {
//                 filters: {
//                     last_name: 'Jance'
//                 }
//             };
//         });

//         // If custom_query is needed in onload
//        // custom_query(frm);
    
//        frm.set_query('articles', 'article', () => {
//         return {
//             filters: {
//                 Status:'return'
//             }
//         };
//     });
//     },
//     },
//     has_fine(frm) {
//         // Clear any existing buttons to avoid duplicates
//         frm.remove_custom_button('Pay Fine');

//         if (frm.doc.has_fine) {
//             // Add the "Pay Fine" button
//             frm.add_custom_button('Pay Fine', () => {
//                 // Create and show the dialog box
//                 let dialog = new frappe.ui.Dialog({
//                     title: 'Fine Details',
//                     fields: [
//                         {
//                             fieldname: 'fine_amount',
//                             fieldtype: 'Currency',
//                             label: 'Fine Amount',
//                             reqd: 1
//                         },
//                         {
//                             fieldname: 'fine_reason',
//                             fieldtype: 'Data',
//                             label: 'Reason for Fine',
//                             reqd: 1
//                         }
//                     ],
//                     primary_action_label: 'Submit',
//                     primary_action(values) {
                       
//                         console.log(values)
//                         dialog.hide();

//                         frappe.call({
//                             method: "library_management.library_management.doctype.library_transaction.library_transaction.create_fine_document",
//                             args: {
//                                 fine_amount: values.fine_amount,
//                                 reason_for_fine: values.fine_reason,
//                                 library_transaction: frm.doc.name

//                             },
//                             callback: function(r) {
//                             if (r.message) {
//                                 console.log(r)
//                                 frm.set_value('fine', r.message.fine_amount)
//                                 frm.refresh_field('fine')
//                             } else {
//                                 frappe.msgprint(__('Server did not return a valid response.'));
//                             }
//                         }
//                         });
//                     }
//                 });

//                 dialog.show();
//             });
//         }
//     }
// });

// function custom_query(frm) {
//     frm.set_query('library_member', () => {
//         return {
//             query: 'library_management.library_management.doctype.library_transaction.library_transaction.custom_query',
//         };
//     });
// }




// frappe.ui.form.on('Add Article', {
//     articles_add: function(frm, cdt, cdn) {
//       set_totals(frm);
//       },
//       articles_remove: function(frm, cdt, cdn) {
//       set_totals(frm);
//       },
//       total_amount: function(frm, cdt, cdn) {
//       set_totals(frm);
//       }
//   });
  
//   function set_totals(frm) {
//       let total = 0;
//       if (frm.doc.articles) {
//           frm.doc.articles.forEach((d) => {
//               if (d.amount) {
//                   total += d.amount;
//               }
//           });
//       }
//       frm.set_value('total_amount', total);
//   }

// frappe.ui.form.on("Library Transaction", {
//     onload(frm) {
//         frm.set_query('library_member', () => {
//             return {
//                 filters: {
//                     last_name: 'Jance'
//                 }
//             };
//         });

//         // If custom_query is needed in onload
//         // custom_query(frm);

//         frm.set_query('article', 'articles', () => {
//             return {
//                 filters: {
//                     Status: 'return'
//                 }
//             };
//         });
//     },

//     has_fine(frm) {
//         // Clear any existing buttons to avoid duplicates
//         frm.remove_custom_button('Pay Fine');

//         if (frm.doc.has_fine) {
//             // Add the "Pay Fine" button
//             frm.add_custom_button('Pay Fine', () => {
//                 // Create and show the dialog box
//                 let dialog = new frappe.ui.Dialog({
//                     title: 'Fine Details',
//                     fields: [
//                         {
//                             fieldname: 'fine_amount',
//                             fieldtype: 'Currency',
//                             label: 'Fine Amount',
//                             reqd: 1
//                         },
//                         {
//                             fieldname: 'fine_reason',
//                             fieldtype: 'Data',
//                             label: 'Reason for Fine',
//                             reqd: 1
//                         }
//                     ],
//                     primary_action_label: 'Submit',
//                     primary_action(values) {
//                         console.log(values)
//                         dialog.hide();

//                         frappe.call({
//                             method: "library_management.library_management.doctype.library_transaction.library_transaction.create_fine_document",
//                             args: {
//                                 fine_amount: values.fine_amount,
//                                 reason_for_fine: values.fine_reason,
//                                 library_transaction: frm.doc.name
//                             },
//                             callback: function(r) {
//                                 if (r.message) {
//                                     console.log(r)
//                                     frm.set_value('fine', r.message.fine_amount)
//                                     frm.refresh_field('fine')
//                                 } else {
//                                     frappe.msgprint(__('Server did not return a valid response.'));
//                                 }
//                             }
//                         });
//                     }
//                 });

//                 dialog.show();
//             });
//         }
//     }
// });

// function custom_query(frm) {
//     frm.set_query('library_member', () => {
//         return {
//             query: 'library_management.library_management.doctype.library_transaction.library_transaction.custom_query',
//         };
//     });
// }

// frappe.ui.form.on('Add Article', {
//     articles_add: function(frm, cdt, cdn) {
//         set_totals(frm);
//     },
//     articles_remove: function(frm, cdt, cdn) {
//         set_totals(frm);
//     },
//     total_amount: function(frm, cdt, cdn) {
//         set_totals(frm);
//     }
// });

// function set_totals(frm) {
//     let total = 0;
//     if (frm.doc.articles) {
//         frm.doc.articles.forEach((d) => {
//             if (d.amount) {
//                 total += d.amount;
//             }
//         });
//     }
//     frm.set_value('total_amount', total);
// }


// 
frappe.ui.form.on("Library Transaction", {
    onload(frm) {
        frm.set_query('library_member', () => {
            return {
                filters: {
                    last_name: 'Jance'
                }
            };
        });

        // Call custom_query function if needed
        // custom_query(frm);

        // Uncomment and correct this section if needed
        // frm.set_query('article', 'articles', () => {
        //     return {
        //         filters: {
        //             status:'Return'
        //         }
        //     };
        // });
    },

    has_fine(frm) {
        // Clear any existing "Pay Fine" button
        frm.remove_custom_button('Pay Fine');

        if (frm.doc.has_fine) {
            // Add the "Pay Fine" button
            frm.add_custom_button('Pay Fine', () => {
                let dialog = new frappe.ui.Dialog({
                    title: 'Fine Details',
                    fields: [
                        {
                            fieldname: 'fine_amount',
                            fieldtype: 'Currency',
                            label: 'Fine Amount',
                            reqd: 1
                        },
                        {
                            fieldname: 'fine_reason',
                            fieldtype: 'Data',
                            label: 'Reason for Fine',
                            reqd: 1
                        }
                    ],
                    primary_action_label: 'Submit',
                    primary_action(values) {
                        dialog.hide();
                        frappe.call({
                            method: "library_management.library_management.doctype.library_transaction.library_transaction.create_fine_document",
                            args: {
                                fine_amount: values.fine_amount,
                                reason_for_fine: values.fine_reason,
                                library_transaction: frm.doc.name
                            },
                            callback: function(r) {
                                if (r.message) {
                                    frm.set_value('fine', r.message.fine_amount);
                                    frm.refresh_field('fine');
                                } else {
                                    frappe.msgprint(__('Server did not return a valid response.'));
                                }
                            }
                        });
                    }
                });

                dialog.show();
            });
        }
    }
});

frappe.ui.form.on('Add Article', {
    articles_add: function(frm, cdt, cdn) {
        set_totals(frm);
    },
    articles_remove: function(frm, cdt, cdn) {
        set_totals(frm);
    },
    total_amount: function(frm, cdt, cdn) {
        set_totals(frm);
    }
});

function set_totals(frm) {
    let total = 0;
    if (frm.doc.articles) {
        frm.doc.articles.forEach((d) => {
            if (d.amount) {
                total += d.amount;
            }
        });
    }
    frm.set_value('total_amount', total);
}


frappe.ui.form.on('Library Transaction', {
    // Triggered when a row in the child table is added or edited
    article_on_form_rendered: function(frm) {
        frm.fields_dict['article'].grid.get_field('row').get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    // Optionally filter rows based on some criteria
                }
            };
        };
    },

    // Triggered when a field value in the child table is changed
    article: function(frm, cdt, cdn) {
        const row = locals[cdt][cdn];
        if (row.row) {
            // Fetch the details of the selected row
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Row',
                    name: row.row
                },
                callback: function(r) {
                    if (r.message) {
                        // Populate the row_number field in the child table
                        frappe.model.set_value(cdt, cdn, 'row_number', r.message.row_number);
                    }
                }
            });
        } else {
            // Clear the row_number field if no row is selected
            frappe.model.set_value(cdt, cdn, 'row_number', '');
        }
    }
});

frappe.ui.form.on('Library Transaction', {
    refresh: function(frm) {
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Library Membership', {
                library_member: frm.doc.name
            });
        });
        frm.add_custom_button('Reserve', () => {
            frappe.new_doc('Reservation', {
                library_member: frm.doc.name
            });
        });
    }
});

