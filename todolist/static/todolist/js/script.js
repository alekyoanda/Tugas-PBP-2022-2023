$(document).ready(function(e){
  const getTaskURL = window.location.href + "json";
  $.ajax({
    type: 'GET',
    url: getTaskURL,
    success: function (response) {
      if (!response.length){
        $('#card-grid').prepend(`
        <div class="d-flex justify-content-center" id="no-task-div">
          <h1>No Task :)</h1>
        </div>`)
      }
      else{
        $('#card-grid').prepend('<h1 class="text-center id="task-exist-h1">Todolist</h1>');
        for (let i = 0; i < response.length; i++){
          addTaskAsync($('#card-grid'), response[i]["fields"], response[i]["pk"]);
        }
      }
    },
    error: function (response) {
        console.log(response)
    }
  })
});

$("#add-task-ajax").click(function(e){
  e.preventDefault();
  const serializedData = getFormData($('#add-task-form'));
  const addTaskURL = window.location.href + "add";
  $.ajax({
    type: 'POST',
    url: addTaskURL,
    data: serializedData,
    success: function (response) {
        // on successfull creating object
        $("#add-task-form").trigger('reset');
        $("#title-input").focus();
        // display the newly friend to table.
        var instance = JSON.parse(response);
        var fields = instance[0]["fields"];
        var task_id = instance[0]["pk"];
        if ($('#no-task-div').length){
          $('#no-task-div').remove();
          $('#card-grid').prepend('<h1 class="text-center id="task-exist-h1">Todolist</h1>');
        }
        addTaskAsync($('#card-grid'), fields, task_id);
    },
    error: function (response) {
        // alert the error if any error occured
        alert(response["responseJSON"]["error"]);
    }
  })
  $('#staticBackdrop').modal('hide');
});

$('#card-grid').ready ( function () {
  $('#card-grid').on('click', '.delete-task-ajax', function(e) {
    e.preventDefault()
    const deleteTaskURL = window.location.href + "delete/" + this.id;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
      type: 'DELETE',
      url: deleteTaskURL,
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    $(`#task-card-${this.id}`).remove();
  });
});

$('#card-grid').ready ( function () {
  $('#card-grid').on('click', '.finish-task-ajax', function(e) {
    e.preventDefault()
    const id = this.id.substring(7);
    const finishTaskURL = window.location.href + "finish_task/" + id;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
      type: 'POST',
      url: finishTaskURL,
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    })
    $(`#task-status-${id}`).text("Selesai");
    $(`#task-status-${id}`).addClass("card-subtitle mb-2 text-success").removeClass("card-subtitle mb-2 text-danger");
    $(`#${this.id}`).remove();
  });
});

function getFormData($form){
  var unindexed_array = $form.serializeArray();
  var indexed_array = {};

  $.map(unindexed_array, function(n, i){
      indexed_array[n['name']] = n['value'];
  });

  return indexed_array;
}

function addTaskAsync($element, fields, task_id) { 
  const title = fields["title"];
  const description = fields["description"];
  const date = fields["date"];
  const tombol_selesai = (!fields["is_finished"]) ? `<div class="finish-task-ajax" id="finish-${task_id}">` +
  '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-check-circle text-muted" id="check_task" viewBox="0 0 16 16">' +
      '<path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>' +
      '<path d="M10.97 4.97a.235.235 0 0 0-.02.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-1.071-1.05z"/>' +
  '</svg>' +
'</div>' : "";
  const status_text = (!fields["is_finished"]) ? `<h6 class="card-subtitle mb-2 text-danger" id="task-status-${task_id}" style="color:red;">Belum Selesai</h6>` :  `<h6 class="card-subtitle mb-2 text-success" id="task-status-${task_id}" style="color:green;">Selesai</h6>`

  var html = 
  `<div class="col-lg-4 col-md-6 col-sm-10 col-xs-1 mb-4" id="task-card-${task_id}">` +
  '<div class="card border-light mx-auto" id="card" style="width: 22rem;">' +
      '<div class="card-body">' +
          '<div class="d-flex justify-content-between">' +
              `<h5 class="card-title">${title}</h5>` +
              '<div class="d-flex justify-content-end">' +
                  tombol_selesai + 
                  `<div class="delete-task-ajax" id="${task_id}">` +
                      '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-trash text-muted" id="delete_task" viewBox="0 0 16 16">' +
                          '<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>' +
                          '<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>' +
                      '</svg>' +
                  '</div>' +
              '</div>' +
          '</div>' +
          status_text +
          `<p class="card-text">${description}</p>` +
          `<p class="card-text text-muted">${date}</p>` +
      '</div>' +
    '</div>' +
  '</div>'

  $($element).append(html);
}