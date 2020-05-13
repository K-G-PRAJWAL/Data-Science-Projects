function getBathValue() {
  // Get no of bathrooms
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  // Get no of BHK's
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";
  //   var url = "/api/predict_home_price"; // only Deployment

  $.post(
    url,
    {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value,
    },
    function (data, status) {
      estPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
    }
  );
}

function onPageLoad() {
  var url = "http://127.0.0.1:5000/get_location_names";
  //   var url = "/api/get_location_names"; // only Deployment
  $.get(url, function (data, status) {
    // function to render the location names
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]); // Add location to drop drown list
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
