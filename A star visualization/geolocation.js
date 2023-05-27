const geoLocation = () => {
    navigator.geolocation.watchPosition(success, error);

    function success (pos) {
        const lat = pos.coords.latitude;
        const lng = pos.coords.longitude;
        const accuracy = pos.coords.accuracy;

        L.marker([lat,lng]).addTo(map_);
        L.circle([lat,lng],{radius: accuracy}).addTo(map_);
    }

    function error(err) {
        if (err.code == 1) {
            alert("Please allow geolocation access");
        } else {
            alert("Cannot get current location");
        }
    }
}

export default geoLocation;
