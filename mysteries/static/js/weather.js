console.log('weather js')

if ('geolocation' in navigator) {
    /* geolocation is available */
} else {
    /* geolocation IS NOT available */
}


const status = document.querySelector('#status');
// const mapLink = document.querySelector('#map-link');

// mapLink.href = '';
// mapLink.textContent = '';

function success(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    status.textContent = '';
    fetch(`https://weather-proxy.freecodecamp.rocks/api/current?lat=${latitude}&lon=${longitude}`)
        .then((res) => res.json())
        .then((data) => {
            console.log(data)

            temp = document.querySelector("#temp")
            temp.innerHTML = Math.round(data.main.temp, 0) + "°C"

            weather = document.querySelector("#weather")
            weather.innerHTML = data.weather[0].main

            tempRange = document.querySelector("#temp-range")
            tempRange.innerHTML = Math.floor(data.main.temp_min) + '°C / ' + Math.ceil(data.main.temp_max) + "°C"

            feelsLike = document.querySelector("#feels-like")
            feelsLike.innerHTML = "Feels Like: " + Math.round(data.main.feels_like) + "°C"

            humidity = document.querySelector("#humidity")
            humidity.innerHTML = "Humidity: " + data.main.humidity + "%"

            visibility = document.querySelector("#visibility")
            visibility.innerHTML = "Visibility: " + Math.round(data.visibility / 1000) + " Km"

            pressure = document.querySelector("#pressure")
            pressure.innerHTML = "Pressure: " + Math.round(data.main.pressure / 10) + " kPa"

            wind = document.querySelector("#wind")
            wind.innerHTML = "Wind: " + Math.round((data.wind.speed * 18) / 5) + " Km/h"

            sunriseDate = new Date(data.sys.sunrise * 1000)

            sunsetDate = new Date(data.sys.sunset * 1000)

            sunrise = document.querySelector("#sunrise")
            sunrise.innerHTML = `Sunrise: ${sunriseDate.getHours()}:${sunriseDate.getMinutes()}:${sunriseDate.getSeconds()} AM`

            sunset = document.querySelector("#sunset")
            sunset.innerHTML = `Sunset: ${sunsetDate.getHours() - 12}:${sunsetDate.getMinutes()}:${sunsetDate.getSeconds()} PM`

        })
        .catch((err) => {
            status.textContent = "Error!"
        })

    //   mapLink.href = `https://www.openstreetmap.org/#map=18/${latitude}/${longitude}`;
    //   mapLink.textContent = `Latitude: ${latitude} °, Longitude: ${longitude} °`;
}

function error() {
    status.textContent = 'Unable to retrieve your location';
}

if (!navigator.geolocation) {
    status.textContent = 'Geolocation is not supported by your browser';
} else {
    status.textContent = 'Locating…';
    navigator.geolocation.getCurrentPosition(success, error);
}


//   document.querySelector('#find-me').addEventListener('click', geoFindMe);