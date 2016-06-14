$(document).ready( function () {
    if(window.location.pathname.indexOf("/devices/") == 0){
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 100,
             "pagingType": "full_numbers",
        });
        $('#devicestable').show()
        $('#container').css( 'display', 'block' );
        table.columns.adjust().draw();
     }
     if(window.location.pathname.indexOf("/ports/") == 0){
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 100,
             "pagingType": "full_numbers",
        });
        $('#devicestable').show()
        $('#container').css( 'display', 'block' );
        table.columns.adjust().draw();
     }
    if(window.location.pathname == "/printers/") {
             var table = $('#printerstable').DataTable({
             "iDisplayLength": 50,
             "pagingType": "full_numbers",
        });
        $('#printerstable').show()
        $('#container').css( 'display', 'block' );
        table.columns.adjust().draw();
     }
    if(window.location.pathname.indexOf("/servers/") == 0){
             var table = $('#serverstable').DataTable({
             "iDisplayLength": 50,
             "pagingType": "full_numbers",
        });
        $('#serverstable').show()
        $('#container').css( 'display', 'block' );
        table.columns.adjust().draw();
     }

    if(window.location.pathname.indexOf("/status/") == 0){
             var table = $('#serverstable').DataTable({
             "iDisplayLength": 50,
             "pagingType": "full_numbers",
        });
        $('#serverstable').show()
        $('#container').css( 'display', 'block' );
        table.columns.adjust().draw();
     }
    if(window.location.pathname == "/repair/") {
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 50,
        });
        table.search(' "Repair" ').draw();
        $('#devicestable').show()
      }
    if(window.location.pathname == "/replace/") {
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 50,
        });
        table.search(' "Replace" ').draw();
        $('#devicestable').show()
      }
    if(window.location.pathname == "/inspect/") {
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 50,
        });
        table.search(' "Inspect" ').draw();
        $('#devicestable').show()
      }
    if(window.location.pathname == "/warranty/") {
             var table = $('#devicestable').DataTable({
             "iDisplayLength": 50,
        });
        table.search(' "Warranty" ').draw();
        $('#devicestable').show()
      }
    $(document).ready(function(){
          $('#historytable').DataTable( {
            });
          $('#historytable').show()
      });
} );