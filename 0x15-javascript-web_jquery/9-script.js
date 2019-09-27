$(function () {
  const requestURL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(requestURL, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
