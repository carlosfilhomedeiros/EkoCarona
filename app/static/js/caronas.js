var marker;
var mapOptions = { center:{ lat: -34.397, lng: 150.644},
                   zoom:8
                 }
function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), mapOptions);
    map.addListener('click', function(event){
        placeMaker(event.latLng, map);
        
    });
}
function placeMaker(latLng, map) {
    if (!marker){
        marker = new google.maps.Marker({
            position: latLng,
            map: map,
            draggable:true
              });
        map.panTo(latLng);
    } else {
        marker.setPosition(latLng);
        map.panTo(latLng);
        

    }
}
function placeCrimes(crimes, map) {
    console.log("Crimes");
    console.log(crimes);
    console.log(crimes[0]["description"]);
    for (var i=0; i<crimes.length; i++) {
        crime = new google.maps.Marker( {
            position: new google.maps.LatLng(crimes[i].latitude, crimes[i].
                                             longitude),
            map: map,
            title: crimes[i].date + "\n" + crimes[i].category + "\n" + crimes[i].description});
    }
}
