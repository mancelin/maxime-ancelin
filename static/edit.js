(function() {

function initEditProject() {

  // Prevents enter key to submit form.
  $('form').on('keypress', function(evt) {
   if (evt.keyCode === 13 || evt.which === 13) {
      evt.preventDefault();
    }
  });

  $('#project-date').datepicker();

  $('#tags').select2();

  $('#readme').wysihtml5({
    "html": true,
    "blockquote": true,
  });
}

// Exports

window.initEditProject = initEditProject;


}).call(this);
