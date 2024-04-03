$(document).ready(function() {
  // A unction to fetch translation
  function fetchTranslation() {
    var languageCode = $("#language_code").val();
    var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";
    
    $.ajax({
      url: apiUrl + languageCode,
      method: "GET",
      success: function(response) {
        $("#hello").text(response.hello);
      },
      error: function(xhr, status, error) {
        console.error("Error fetching translation:", error);
      }
    });
  }

  // Fetches translation when button is clicked
  $("#btn_translate").click(function() {
    fetchTranslation();
  });

  // This fetches translation when ENTER key is pressed on input field
  $("#language_code").keypress(function(event) {
    if (event.which === 13) { // Check if ENTER key is pressed
      fetchTranslation();
    }
  });
});

