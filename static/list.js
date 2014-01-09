(function() {

function initListProject() {

$('[type="checkbox"]').change(function(){
  console.log(this.name);
  if(this.name == "toogle_select_all"){
    checkboxes = $('[type="checkbox"]');
    if($(this).is(':checked')){
      checkboxes.each(function(){
        this.checked=true;
      })
    } else {
      checkboxes.each(function(){
        this.checked=false;
      })
    }
  } else {
    $('[name="toogle_select_all"]').attr("checked", false)
  }
})

}

// Exports

window.initListProject = initListProject;


}).call(this);
