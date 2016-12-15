var map = L.map('mapid', {
  center: [59.93,30.30],
  zoom: 11
});

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpandmbXliNDBjZWd2M2x6bDk3c2ZtOTkifQ._QA7i5Mpkd_m30IGElHziw', {
  maxZoom: 17,
  attribution: '',
  id: 'mapbox.streets'
}).addTo(map);

// CallApi('GET', 'ping?test=123', function(resp){
//   console.log(resp.responseText)
// }, function(resp){
//   console.log(resp.code)
// });
//
// CallApi('GET', 'data', function(resp){
//   console.log(resp.responseText)
// }, function(resp){
//   console.log(resp.code)
// });

var multiplier = 1.5;
CallApi('GET', 'data', function(resp){
  JSON.parse(resp.responseText).forEach(function(item){

    var circle = L.circle([item.lat, item.lon], multiplier * item.count);
    circle.addTo(map);

    L.marker([item.lat, item.lon], {title: item.area_name, alt: item.area_name})
    .bindTooltip("<p style='font-size:9px; margin-top: 0; margin-bottom: 0;'>" + item.area_name +"<br/>Кол-во: " + item.count + "<br>" + item.prvs +  "</p>", {
      permanent: true,
      direction: 'right'
    }).addTo(map);
  })
}, function(resp){
  console.log(resp.code)
});

setInterval(function(){

}, 2000);