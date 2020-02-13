$( document ).ready(function() {
    console.log( "ready!" );
    $( "button" ).click(function() {
      submitDataToBackend(this.value)
  });
});

function submitDataToBackend(button_value){
  console.log('Sending value ' + button_value);
  $.post( "{{ url_for('generate_new_question') }}", { value: button_value })
    .done(function( data ) {
      $('#videoGrouping').html(data);
    });
}
