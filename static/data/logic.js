

// Initialize all of the LayerGroups we'll be using
var layers = {
  Pixies: new L.LayerGroup(),
  Willie_Nelson: new L.LayerGroup(),
  Bring_me_the_horizon: new L.LayerGroup()
};
// Creating map object
var myMap = L.map("marker-map", {
  center: [31.51, -96.42],
  zoom: 8
});



// Create the tile layer that will be the background of our map
var markerMapLayer = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "light-v10",
  accessToken: API_KEY
}).addTo(myMap);
// console.log(API_KEY);

//Read in our band year location Data from SQL
// Use this link to get the geojson data.
var link = "static/data/bandyearlocation.json";


// Grabbing our sql data..
d3.json(link).then(function(response) {
  var markerclustergroup = L.markerClusterGroup();
  // Creating a GeoJSON layer with the retrieved data
  console.log(response);



//for loop for coordinates
for (var i = 0; i < response.length; i++) {
  var location = response[i];
//check for location property
  if (location) {
  // Add a new marker to the cluster group and bind a pop-up
  L.marker([location.lat, location.long])
  .bindPopup(location.state).addTo(myMap);
  
}

}
myMap.addLayer(markerclustergroup);
});




// Initialize all of the LayerGroups we'll be using
// var layers = {
  // 2005: new L.LayerGroup(),
  // 2010: new L.LayerGroup(),
  // 2015: new L.LayerGroup(),
  // 2019: new L.LayerGroup(),
// };

// Create the map with our layers
// var map = L.map("marker-map", {
  // center: [42.88, -97.38],
  // zoom: 5,
  // layers: [
    // layers.2005,
    // layers.2010,
    // layers.2015,
    // layers.2019,
  // ]
// });
// 




