jQuery(document).ajaxSend(function(event, xhr, settings) {
  var getCookie, safeMethod, sameOrigin;
  getCookie = function(name) {
    var cookie, cookieValue, cookies, i;
    cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      cookies = document.cookie.split(";");
      i = 0;
      while (i < cookies.length) {
        cookie = jQuery.trim(cookies[i]);
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
        i++;
      }
    }
    return cookieValue;
  };
  sameOrigin = function(url) {
    var host, origin, protocol, sr_origin;
    host = document.location.host;
    protocol = document.location.protocol;
    sr_origin = "//" + host;
    origin = protocol + sr_origin;
    return (url === origin || url.slice(0, origin.length + 1) === origin + "/") || (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + "/") || !(/^(\/\/|http:|https:).*/.test(url));
  };
  safeMethod = function(method) {
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  };
  if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
    return xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  }
});
