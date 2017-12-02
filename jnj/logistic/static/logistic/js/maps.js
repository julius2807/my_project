// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

var map, infoWindow;
var directionsService, directionsDisplay;
var marker, marker2;

function initMap() {
  var card = document.getElementById('pac-card');
  var input_origin = document.getElementById('pac-input-origin');
  var input_dest = document.getElementById('pac-input-dest');
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;

  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 15
  });

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
  directionsDisplay.setMap(map);


  // ****** START set the location to the current location *****

  infoWindow = new google.maps.InfoWindow;
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
        };

      infoWindow.setPosition(pos);
      infoWindow.setContent('Your Location');
      infoWindow.open(map);
      map.setCenter(pos);
      }, function() {
              handleLocationError(true, infoWindow, map.getCenter());
      });
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }

  // ****** END set the location to the current location *****

  // ****** START setting up markers after search *****
  var autocomplete = new google.maps.places.Autocomplete(input_origin);
  var autocomplete2 = new google.maps.places.Autocomplete(input_dest);

  marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });

  marker2 = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });

  autocomplete.bindTo('bounds', map);
  autocomplete2.bindTo('bounds', map);


  autocomplete.addListener('place_changed', function() {
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);  // Why 17? Because it looks good.
    }
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

  });

  autocomplete2.addListener('place_changed', function() {
    marker2.setVisible(false);
    var place = autocomplete2.getPlace();
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);  // Why 17? Because it looks good.
    }
    marker2.setPosition(place.geometry.location);
    marker2.setVisible(true);

  });

  // ****** END setting up markers after search *****

  // ****** START initialize the direction service *****

  var onChangeHandler = function() {
    var origin = document.getElementById('pac-input-origin').value;
    var destination = document.getElementById('pac-input-dest').value;
    if (origin.trim() == '' || destination.trim() == '') {
        window.alert('Both origin and destination must be filled!');
    } else {
      calculateAndDisplayRoute(directionsService, directionsDisplay);
    }
  };
  document.getElementById('pac-search').addEventListener('click', onChangeHandler);

  // ****** END  initialize the direction service *****

}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
  infoWindow.open(map);
}

function calculateAndDisplayRoute(directionsService, directionsDisplay) {
  marker.setVisible(false);
  marker2.setVisible(false);

  directionsService.route({
    origin: document.getElementById('pac-input-origin').value,
    destination: document.getElementById('pac-input-dest').value,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
      document.getElementById('pac-output-distance').value = response.routes[0].legs[0].distance.text;
      document.getElementById('pac-output-duration').value = response.routes[0].legs[0].duration.text;
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });


}
