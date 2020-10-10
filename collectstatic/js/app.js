let mymap;
let newMarkerLatLng;

$(document).ready(function () {
    initMap();
});

$(document).bind("mousedown", function (e) {

    // If the clicked element is not the menu
    if (!$(e.target).parents(".custom-menu").length > 0) {

        // Hide it
        $(".custom-menu").hide(100);
    }
});

function initMap() {
    mymap = L.map('mapid').setView([51.505, -0.09], 13);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);

    mymap.on('contextmenu', (e) => {
        console.log('eeee', e.originalEvent.pageY);

        $(".custom-menu")
            .finish()
            .toggle(100)
            .css({
                top: e.originalEvent.pageY + "px",
                left: e.originalEvent.pageX + "px"
            });

        newMarkerLatLng = e.latlng
    });
}

function addNewMarker() {
    const email = $('#email').val();

    if (!email || !description) {

        return;
    }

    console.log('test', newMarkerLatLng);
    newMarkerLatLng = null;
}



// ajax example
function sendEmail() {
    var data = new FormData();
    data.append('email', "bhaiii@gmail.com");
    data.append('latitude', "25.422151");
    data.append('longitude', "26.142132");

    // Creating the XMLHttpRequest object
    var request = new XMLHttpRequest();

    request.open("POST", "send-email", true);
    // Defining event listener for readystatechange event
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            console.log(this.responseText);
        }
    };

    // Sending the request to the server
    request.send(data);
}
