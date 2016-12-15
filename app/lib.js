function CallApi(method, route, success, error) {
  var xhr = new XMLHttpRequest();
  xhr.open(method, route, true);
  xhr.send();
  xhr.onreadystatechange = function() {
    if (xhr.readyState != 4) return;
    if (xhr.status != 200) {
      error(xhr)
    } else {
      success(xhr)
    }
  }
}