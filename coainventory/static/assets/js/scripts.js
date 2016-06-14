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

$(document).ready(function() {


    if (document.documentElement.clientWidth > 768) {
        page = document.documentElement.clientWidth
        sidebar = $('.nav-side-menu').width();
        content = page - sidebar
        margins = content * .07
        content2 = content - margins

        $('.mainwrapper').css({'leftMargin': margins, 'marginRight': margins, 'width': content2})
        $('#devicestable, #printerstable, #serverstable').css('width', '100%');

    }
    // fire when below 768
    else {
        $('.mainwrapper').css({'margin': '0','width': '100%', 'padding': '30px'})
        $('#devicestable').css({'padding': '30px','width': '95%'});
    }

    $(window).resize(function() {
            page = document.documentElement.clientWidth
            sidebar = $('.nav-side-menu').width();
            content = page - sidebar
            margins = content * .07
            content2 = content - margins

        if (document.documentElement.clientWidth < 768) {
            $('.mainwrapper').css({'width': '100%'})
        } else {
            $('.mainwrapper').css({'leftMargin': margins, 'marginRight': margins, 'width': content2})
        }

    });




});