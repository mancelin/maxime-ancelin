(function() {

function initEditProject() {

  // Prevents enter key to submit form.
  $('form').on('keypress', function(evt) {
   if (evt.keyCode === 13 || evt.which === 13) {
      evt.preventDefault();
    }
  });

  $('#project-date').datepicker();

  $.ajax({
    dataType: 'json',
    url: '/tags.json'
  })
    .done(function(data) {
      $('.tags input', $el).select2({
        containerCssClass: 'input-xxlarge',
        tags: data,
        tokenSeparators: [',', ' ']
      });
    });
}

// Exports

window.initEditProject = initEditProject;


}).call(this);
