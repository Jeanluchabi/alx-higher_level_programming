$(document).ready(function(){
    // This fetches data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            // This displays the translation in the HTML tag with id 'hello'
            $('#hello').text(data.hello);
        },
        error: function(error) {
            // This Handles errors, for example, display an error message
            $('#hello').text('Error fetching translation');
        }
    });
});
