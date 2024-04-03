$(document).ready(function(){
    // This Handles click event on DIV#toggle_header
    $('#toggle_header').click(function(){
        // Toggles class between red and green on <header> element
        $('header').toggleClass('red green');
    });
});
