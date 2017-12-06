// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

var map, infoWindow;
var directionsService, directionsDisplay;
var marker, marker2;


function initMap() {

  var input_origin = document.getElementById('pac-input-origin');
  var input_dest = document.getElementById('pac-input-dest');
  var directionsService = new google.maps.DirectionsService;
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var geocoder = new google.maps.Geocoder();

  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 15
  });

  //map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);
  directionsDisplay.setMap(map);

  // ****** START  show the directions based on origin and dest *****
  var origin = document.getElementById('pac-input-origin').value;
  var destination = document.getElementById('pac-input-dest').value;
  if (origin.trim() == '' || destination.trim() == '') {
    window.alert('Both origin and destination must be filled!');
  } else {
    calculateAndDisplayRoute(directionsService, directionsDisplay);
  }
  // ****** END  show the directions based on origin and dest *****

}


function calculateAndDisplayRoute(directionsService, directionsDisplay) {
  directionsService.route({
    origin: document.getElementById('pac-input-origin').value,
    destination: document.getElementById('pac-input-dest').value,
    travelMode: 'DRIVING'
  }, function(response, status) {
    if (status === 'OK') {
      directionsDisplay.setDirections(response);
    } else {
      window.alert('Directions request failed due to ' + status);
    }
  });

}
