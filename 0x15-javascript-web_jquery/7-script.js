$(document).ready(function(){
    // Fetchs data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(data) {
            // Updates the text of the <div> with id 'character'
            $('#character').text(data.name);
        },
        error: function(error) {
            // Handles errors, for example, display an error message
            $('#character').text('Error fetching character name');
        }
    });
});
