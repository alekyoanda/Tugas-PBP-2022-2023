# Tugas 6 PBP

## Link Aplikasi Heroku
https://tugas2-pbp-alek.herokuapp.com

## Perbedaan Antara *Asynchronous* Dengan *Synchronous Programming*
Dalam *synchronous programming*, proses - proses pada program dijalankan secara *sequential*. Dengan kata lain, proses - proses yang lain akan menunggu sampai proses saat ini selesai dieksekusi. Sebaliknya, pada *asynchronous programming* program bisa menjalankan proses yang berbeda, walaupun ada proses lain yang sedang dieksekusi. Dengan cara ini, program bisa menjalankan banyak proses dalam waktu yang bersamaan. *Asynchronous programming* sering dikaitkan dengan *parallelization*. Dengan *parallelization*, kita dapat memecah apa yang biasanya diproses secara *sequential*, artinya memecahnya menjadi bagian-bagian yang lebih kecil yang dapat berjalan secara independen dan bersamaan.

## *Event-Driven Programming* Dan Contoh Penerapannya Pada AJAX dan Javascript
*Event-Driven Programming* menyatakan bahwa alur dari sebuah program itu bergantung pada *event* yang diperoleh dari *action* oleh *user*. Contoh penerapannya pada Javascript misalnya pada saat *user* menekan sebuah *button*, setelah itu muncul sebuah alert pada *window browser user*.

## Penerapan *Asynchronous Programming* Pada AJAX
Contoh penerapannya adalah ketika kita ingin menambah *task* melalui sebuah *form* pada aplikasi *todolist* kita menggunakan AJAX dengan *method* POST
```
...
$.ajax({
    type: 'POST',
    url: addTaskURL,
    data: isiForm,
    ...
```
Pada saat AJAX *Request* dibuat ke URL yang dituju, yaitu ```addTaskURL```, maka fungsi yang di-*mapping* oleh ```addTaskURL``` di ```views.py``` akan mengeksekusi instruksi - instruksi pada *body* fungsi tersebut. Tetapi, aplikasi web kita tidak perlu menunggu fungsi tersebut selesai dieksekusi terlebih dahulu sebelum bisa melakukan tugas lain. Melainkan, aplikasi web kita bisa menjalankan tugas lain selagi fungsi tesebut dieksekusi. Misalnya, *user* menghapus sebuah task yang sudah ada. Ketika fungsi tadi selesai dieksekusi, maka return dari fungsi tersebut akan menjadi *response* parameter pada *state success* pada AJAX *Request* tadi.
```
...
success: function (response) {
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
...
```


## Implementasi Tugas 6

### <li> Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON </li>
```
def show_todolist_json(request):
    if request.method == "GET":
        data = Task.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
### <li>  Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat </li>
```
urlpatterns = [
    ...
    path('json', views.show_todolist_json, name="json_todolist"),
    ...
]
```
### <li>  Lakukan pengambilan task menggunakan AJAX GET </li>
```
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
```
Dimana fungsi addTaskAsync adalah sebagai berikut:
```
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
```
### <li>Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task</li>
```
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
    Create Task
</button>

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="staticBackdropLabel">Add task</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="container-login">
                    <div class="login-form">
                        <form method="POST" action="" id="add-task-form">
                            {% csrf_token %}
                            <table>
                                <tr>
                                    <td>Title: </td>
                                    <td><input type="text" name="title" placeholder="Title" class="form-control" id="title-input"></td>
                                </tr>
                                        
                                <tr>
                                    <td>Description: </td>
                                    <td><textarea name="description" placeholder="Description" class="form-control" cols="30" rows="4"></textarea></td>
                                </tr>
                            </table>
                        </form>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="add-task-ajax">Add Task</button>
            </div>
        </div>
    </div>
</div>
```
### <li>Buatlah view baru untuk menambahkan task baru ke dalam database</li>
```
def add_task_ajax(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_task = Task.objects.create(user=request.user, title=title, description=description)
        
        serialize_json = serializers.serialize('json', [new_task])
        print(serialize_json)
        
        return HttpResponse(serialize_json)

    return JsonResponse({"error": "Not an ajax request"}, status=400)
```
### <li>Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat</li>
```
urlpatterns = [
    ...
    path('add', views.add_task_ajax, name="add_task_ajax"),
    ...
]
```
### <li>Buat sebuah AJAX POST Request untuk menambah task baru yang menuju ke URL tersebut </li>
```
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
```