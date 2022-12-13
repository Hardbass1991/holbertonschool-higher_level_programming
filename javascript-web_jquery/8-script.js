$(function() {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function(data) {
    const movies = data.results;
    console.log(movies);
    $.each(movies, function(index, value) {
      $('UL#list_movies').append("<li>" + value.title + "</li>")
    });
  });
});