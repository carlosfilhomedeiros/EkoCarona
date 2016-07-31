$(function() {
  $(document).on('keyup keypress', 'form input[type="text"]', function(e) {
  if(e.which == 13) {
    $('form input[type="text"]').blur()
    e.preventDefault();
    return false;
  }
});

  $('.datepicker').pickadate({
  selectMonths: true, // Creates a dropdown to control month
});

  $('#saida').hide()
  $('#date').hide()


  $("#chegada a i").click(function(){
    $("#chegada").animate({
            height: 'toggle'
        });
    $('#saida').show()
  });

  $("#saida a i").click(function(){
    $("#saida").animate({
            height: 'toggle'
        });
    $('#date').show()
  });


});
