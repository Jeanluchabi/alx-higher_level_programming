$(document).ready(function() {
  $("#btn_translate").click(function() {
    var langCode = $("#language_code").val();
    var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";
    
    $.ajax({
      url: apiUrl + langCode,
      method: "GET",
      success: function(response) {
        $("#hello").text(response.hello);
      },
      error: function(xhr, status, error) {
        console.error("Error fetching translation:", error);
      }
    });
  });
});

