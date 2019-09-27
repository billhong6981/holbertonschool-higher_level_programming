$(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const requestURL = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang;
    $.get(requestURL, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});

$(function () {
  $('INPUT#language_code').keypress(function (INT) {
    if (INT.which === 13) {
      const lang = $('INPUT#language_code').val();
      const requestURL = 'https://www.fourtonfish.com/hellosalut/?lang=' + lang;
      $.get(requestURL, function (data) {
        $('DIV#hello').text(data.hello);
      });
      return false;
    }
  });
});
