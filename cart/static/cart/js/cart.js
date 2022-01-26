/**
 * cart.js: Javascript file for cart app and page.
 */

/*jshint esversion: 6 */
/*globals $:false */

//  btt-button functionality
$('.btt-link').click(function(e) {
    window.scrollTo(0,0);
});
//  Update product quantity on click
$('.update-link').click(function(e) {
    let form = $(this).prev('.update-form');
    form.submit();
});
/**
* Function to remove item and reload on click
* Gets the csrf token as a string, the item id by using split with id attr
* posts data to the url and reloads page to reflect updated cart.
*/
$('.remove-item').click(function(e) {
    let csrfToken = "{{ csrf_token }}";
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('product_size');
    let url = `/cart/remove/${itemId}/`;

    // The field expected by Django when form is posted to server
    let data = {'csrfmiddlewaretoken': csrfToken, 'product_size': size};

    $.post(url, data)
    .done(function() {
        location.reload();
    });
});