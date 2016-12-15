var map = L.map('mapid', {
  center: [59.93,30.30],
  zoom: 12
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
  maxZoom: 18,
  attribution: '',
  id: 'mapbox.streets'
}).addTo(map);



L.circle([59.93,30.30], 1000).addTo(map);