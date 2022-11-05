function initMap() {
    // const directionsRenderer = new google.maps.DirectionsRenderer();
    // const directionsService = new google.maps.DirectionsService();
    var map = new google.maps.Map(document.getElementById("map"), {
      zoom: 14,
      center: { lat: 42.3601, lng: -71.0589 },
    });
    var marker=new google.maps.Marker(
        {
            position:{lat: 25.5788, lng: 91.8933},
            map:map
        })
    // directionsRenderer.setMap(map);
    // calculateAndDisplayRoute(directionsService, directionsRenderer);
    // document.getElementById("mode").addEventListener("change", () => {
    //   calculateAndDisplayRoute(directionsService, directionsRenderer);
    //});
  }
  
  
  function calculateAndDisplayRoute(directionsService, directionsRenderer) {
    const selectedMode = document.getElementById("mode").value;
  
    directionsService
      .route({
        origin: document.getElementById("from").value,
        destination: document.getElementById("to").value,
        // Note that Javascript allows us to access the constant
        // using square brackets and a string value as its
        // "property."
        travelMode: google.maps.TravelMode[selectedMode],
      })
      .then((response) => {
        directionsRenderer.setDirections(response);
      })
      .catch((e) => window.alert("Directions request failed due to " + status));
  }