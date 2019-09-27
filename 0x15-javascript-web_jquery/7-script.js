$(function () {
  const requestURL = 'https://swapi.co/api/people/5/?format=json';
  $.get(requestURL, function (data, textStatus) {
    $('DIV#character').text(data.name);
  });
});
