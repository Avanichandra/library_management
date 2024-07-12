
// frappe.ui.form.on("Food Count Details", {
//     normal_rate: function(frm) {
//       if (frm.doc.normal_rate) {
//         frm.events.update_normal_rate_value_table(frm);
//       }
//     },
//     special_rate: function(frm) {
//       if (frm.doc.special_rate) {
//         frm.events.update_special_rate_value_table(frm);
//       }
//     },
//     update_normal_rate_value_table: function(frm) {
//       if (frm.doc.food_counts) {
//         frm.doc.food_counts.forEach(function(food_count) {
//           if (food_count.food_type == "Normal") {
//             frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.normal_rate);
//           }
//         });
//       }
//       frm.refresh_fields();
//     },
//     update_special_rate_value_table: function(frm) {
//       if (frm.doc.food_counts) {
//         frm.doc.food_counts.forEach(function(food_count) {
//           if (food_count.food_type == "Special") {
//             frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.special_rate);
//           }
//         });
//       }
//       frm.refresh_fields();
//     }
//   });
  
//   frappe.ui.form.on("Daily Food Count Details", {
//     count: function(frm,cdt,cdn) {
//        calculate_amount(frm, cdt, cdn);
//        amount(frm, cdt, cdn);
//        count(frm, cdt, cdn);
//     },
//     rate: function(frm,cdt,cdn) {
//         calculate_amount(frm,cdt,cdn);
//         amount(frm, cdt, cdn);
//         count(frm, cdt, cdn);
//     },
//     amount: function(frm,cdt,cdn) {
//         let d = locals[cdt][cdn];
//         total_amount += d.amount; 
//         frm.set_value('total_amount', total_amount);
//     }
//   });
  
//   function calculate_amount(frm, cdt, cdn) {
    
//     let d = locals[cdt][cdn];
//     let amount = d.count * d.rate;
//     frappe.model.set_value(cdt, cdn, 'amount', amount);
//   }



// function amount(frm, cdt, cdn) {
   
//     let d = locals[cdt][cdn];
//     total_amount += d.amount; // Corrected this line to properly reference 'e' instead of 'd'
//     frm.set_value(cdt, cdn, 'total_amount', total_amount);
// }
  
//   function count(frm, cdt, cdn) {
   
//     let g = locals[cdt][cdn];
//     let count =+ g.count;
//     frappe.model.set_value(cdt, cdn, 'count', total_count);
//   }



frappe.ui.form.on("Food Count Details", {
    normal_rate: function(frm) {
        if(frm.doc.normal_rate){
          frm.events.update_normal_rate_value_table(frm);
        }
    },
    special_rate: function(frm) {
        if(frm.doc.special_rate){
          frm.events.update_special_rate_value_table(frm);
        }
    },
    update_normal_rate_value_table: function(frm) {
    if (frm.doc.food_counts) {
    frm.doc.food_counts.forEach(function(food_count) {
            if(food_count.food_type == "Normal"){
              frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.normal_rate);
            }
    });
    }
    frm.refresh_fields();
    },
      update_special_rate_value_table: function(frm) {
    if (frm.doc.food_counts) {
    frm.doc.food_counts.forEach(function(food_count) {
            if(food_count.food_type == "Special"){
              frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.special_rate);
    
            }
    });
    }
    frm.refresh_fields();
    },
    });
    
    frappe.ui.form.on("Daily Food Count Details", {
    normal_rate: function(frm) {
    if (frm.doc.normal_rate) {
    frm.events.update_normal_rate_value_table(frm);
    }
    },
    special_rate: function(frm) {
    if (frm.doc.special_rate) {
    frm.events.update_special_rate_value_table(frm);
    }
    },
    add_food_count: function(frm, cdt, cdn) {
    frm.events.set_totals(frm);
    },
    remove_food_count: function(frm, cdt, cdn) {
    frm.events.set_totals(frm);
    },
    update_normal_rate_value_table: function(frm) {
    if (frm.doc.food_counts) {
    frm.doc.food_counts.forEach(function(food_count) {
    if (food_count.food_type == "Normal") {
    frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.normal_rate);
    }
    });
    }
    frm.events.set_totals(frm);
    frm.refresh_fields();
    },
    update_special_rate_value_table: function(frm) {
    if (frm.doc.food_counts) {
    frm.doc.food_counts.forEach(function(food_count) {
    if (food_count.food_type == "Special") {
    frappe.model.set_value(food_count.doctype, food_count.name, 'rate', frm.doc.special_rate);
    }
    });
    }
    frm.events.set_totals(frm);
    frm.refresh_fields();
    },
    });
    
    frappe.ui.form.on("Daily Food Count Details", {
        refresh: function(frm) {
           
            set_totals(frm);
        },
        food_counts_add: function(frm, cdt, cdn) {
            set_totals(frm);
        },
        food_counts_remove: function(frm, cdt, cdn) {
            set_totals(frm);
        },
        count: function(frm, cdt, cdn) {
            set_totals(frm);
            let d =locals[cdt][cdn];
            let amount = d.count * d.rate;
            frappe.model.set_value(cdt,cdn,'amount',amount);
        },
        rate: function(frm, cdt, cdn) {
            set_totals(frm);
            let d =locals[cdt][cdn];
            let amount = d.count * d.rate;
            frappe.model.set_value(cdt,cdn,'amount',amount);
        }
    });
    
    
    function set_totals(frm) {
        let total_amount = 0;
        let total_count = 0;
    
    
        if (frm.doc.food_counts) {
            frm.doc.food_counts.forEach((d) => {
                if (d.count && d.rate) {
                    let amount = d.count * d.rate;
                    total_amount += amount;
                }
                if (d.count) {
                    total_count += d.count;
                }
            });
        }
    
        // Set the calculated totals back to the form fields
        frm.set_value('total_amount', total_amount);
        frm.set_value('total_count', total_count);
    
        // Refresh form fields to reflect updated values
        frm.refresh_fields();
    }
    
    
    