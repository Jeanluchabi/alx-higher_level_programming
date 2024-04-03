document.addEventListener("DOMContentLoaded", function() {
  var addBtn = document.getElementById("add_item");
  var removeBtn = document.getElementById("remove_item");
  var clearBtn = document.getElementById("clear_list");
  var myListing = document.querySelector("ul.my_list");

  addBtn.addEventListener("click", function() {
    var newItem = document.createElement("li");
    newItem.textContent = "Item";
    myListing.appendChild(newItem);
  });

  removeBtn.addEventListener("click", function() {
    var lastItem = myListing.lastElementChild;
    if (lastItem) {
      myListing.removeChild(lastItem);
    }
  });

  clearBtn.addEventListener("click", function() {
    while (myListing.firstChild) {
      myListing.removeChild(myListing.firstChild);
    }
  });
});

