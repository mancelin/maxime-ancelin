(function() {

function initEditProject() {

  // Prevents enter key to submit form.
  $('form').on('keypress', function(evt) {
    if ((evt.keyCode === 13 || evt.which === 13) &&
        (document.activeElement.id !== "description" || document.activeElement.id !== "readme")){
      evt.preventDefault();
    }
  });

  $('#project-date').datepicker();

  $.ajax({
    dataType: 'json',
    url: '/tags.json'
  })
    .done(function(data) {
      $('#tags').select2({
        containerCssClass: 'input-xxlarge',
        tags: data,
        tokenSeparators: [',', ' ']
      });
    });


  $('#readme').wysihtml5({
    "html": true,
    "blockquote": true,
  });
}

// Exports

window.initEditProject = initEditProject;


}).call(this);
