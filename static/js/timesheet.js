$(function () {

    /* Functions */
  
    // var loadMetrics = function () {
    //   var btn = $(this);
    //   $.ajax({
    //     url: btn.attr("data-url"),
    //     type: 'get',
    //     dataType: 'json',
    //     success: function (data) {
    //       $("#metrics-refresh").html(data.html_form);
    //     }
    //   });
    // };
  
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-timesheet").modal("show");
        },
        success: function (data) {
          $("#modal-timesheet .modal-content").html(data.html_form);
        }
      });
    };

    var loadFormTimesheet = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-timesheet-real").modal("show");
        },
        success: function (data) {
          $("#modal-timesheet-real .modal-content").html(data.html_form);
        }
      });
    };
  
    // var loadFormDownload = function () {
    //   var btn = $(this);
    //   $.ajax({
    //     url: btn.attr("data-url"),
    //     type: 'get',
    //     dataType: 'json',
    //     beforeSend: function () {
    //       $("#modal-inventory").modal("show");
    //     },
    //     success: function (data_download) {
    //       $("#modal-inventory .modal-content").html(data_download);
    //     }
    //   });
    // };
    
  
    // var saveForm = function () {
    //   var form = $(this);
    //   $.ajax({
    //     url: '/inventory/createview/',
    //     data: form.serialize(),
    //     type: form.attr("method"),
    //     dataType: 'json',
    //     success: function (data) {
    //       if (data.form_is_valid) {
    //         $("#refresh-table").html(data.html_book_list);
    //         $("#modal-inventory").modal("hide");
    //       }
    //       else {
    //         $("#modal-inventory .modal-content").html(data.html_form);
    //       }
    //     }
    //   });
    //   return false;
    // };
    
    /* Binding */
  
    $(".js-add-task").click(loadForm);
    $(".js-add-timesheet").click(loadFormTimesheet);
    // $(".js-download").click(loadFormDownload);  
    // $("#modal-inventory").on("submit", ".js-view-create-form", saveForm);
    // $(".js-get-metrics").click(loadMetrics);
    
  });
  
  
  
  