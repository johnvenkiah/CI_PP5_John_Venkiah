/**
 * countryfield.js: Javascript file for adding style to the country field in the profile and checkout pages.
 */

/*jshint esversion: 6 */
/*globals $:false */

let countrySelected = $('#id_default_country').val();
if(!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});