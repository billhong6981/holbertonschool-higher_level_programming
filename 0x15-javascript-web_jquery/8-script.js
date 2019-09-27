$(function () {
  const requestURL = 'https://swapi.co/api/films/?format=json';
  $.get(requestURL, function (data) {
    data = data.results;
    data.forEach(entry => {
      $('UL#list_movies').append(`<li>${entry.title}</li>`);
    });
  });
});
