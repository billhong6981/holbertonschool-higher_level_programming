$(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const requestURL = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(requestURL, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
