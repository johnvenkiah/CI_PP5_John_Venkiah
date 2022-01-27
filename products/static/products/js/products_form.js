/**
 * products_form.js: Javascript file for add_product page in products app.
 */

/*jshint esversion: 6 */
/*globals $:false */

/**
The two functions below let the text displayed when uploading a new
product or brand image is customizeable. Credit: Code Institute,
Boutique Ado project
*/

$('#new-product-image').change(function() {
    let prodUpload = $('#new-product-image')[0].files[0];
    $('#filename-product').text(`Set new image to: ${prodUpload.name}`);
}); 

$('.brand-img-class').change(function() {
    let brandUpload = $('.brand-img-class')[0].files[0];
    $('.filename-for-brand').text(`Set new image to: ${brandUpload.name}`);
});

/**
This function makes sure that the original price is higher that the current one,
if it is set. If not, a modal window is triggered and values are set to null again.
*/

$("#id_product-price").change(function() {
if (
    (parseInt($('#id_product-initial_price').val()) !== null) &&
    (parseInt($('#id_product-price').val()) >= parseInt($('#id_product-initial_price').val()))
) {
    $('#wrongPriceModal').modal('show');
    $('#id_product-price').val(null);
    $('#id_product-initial_price').val(null);
}});