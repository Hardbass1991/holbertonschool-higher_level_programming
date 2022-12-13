$(function() {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.get(url, function(data) {
    const salut = data.hello;
    $('DIV#hello').text(salut);
  });
});