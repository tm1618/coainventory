$(document).delegate('*[data-toggle="lightbox"]', 'click', function(event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

$(function(){
      if (window.location.pathname != "/devices/") {
            $('.statusmenu').hide();
            $('.departmentmenu').hide();
      }
 });

