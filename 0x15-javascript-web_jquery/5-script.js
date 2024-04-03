$(document).ready(function(){
    // Handles click event on DIV#add_item
    $('#add_item').click(function(){
        // It creates a new <li> element
        var newItem = $('<li></li>').text('Item');
        
        // It appends the new <li> element to UL.my_list
        $('ul.my_list').append(newItem);
    });
});
