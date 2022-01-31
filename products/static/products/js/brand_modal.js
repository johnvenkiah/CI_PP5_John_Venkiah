/**
 * products/brand_modal.js, file used in manage_brands.html
 * 
 * Script to access and display image filename in each modal window.
 * Elements are given a new class and are iterated to apply the new
 * filename to. Thanks to my friend Daniel Rasmussen for guidance on this one.
*/

/*jshint esversion: 6 */
/*globals $:false */

$(document).ready(function() {
    const brandImges = $('.brand-img-class');
    brandImges.each(function(_, item) {
        const brandImg = '.' + item.classList[0];
        $(brandImg).change(function(e) {
            const {target} = e;
            const {name} = target.files[0];
            const allFileName = $('.filename-for-brand');
            allFileName.each(function(_, item) {
                item.innerHTML =`Set new image to: ${name}`;
            });
        });
    });
});