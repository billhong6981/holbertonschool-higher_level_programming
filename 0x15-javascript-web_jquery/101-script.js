$(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});

$(function () {
  $('DIV#remove_item').click(function () {
    $('Ul.my_list li').last().remove();
  });
});

$(function () {
  $('DIV#clear_list').click(function () {
    $('Ul.my_list').empty();
  });
});
