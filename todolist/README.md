# Tugas 4 PBP

## Link Aplikasi Heroku
https://tugas2-pbp-alek.herokuapp.com

## Kegunaan CSRF Token
CSRF atau *Cross-Site Request Forgery* token merupakan sebuah cara django untuk memastikan *HTTP Request* yang dilakukan *client* memang benar dibuat oleh aplikasi tersebut. CSRF token sendiri adalah sebuah token dengan nilai *random* yang panjang untuk menjamin keamanannya dan digunakan untuk mencegah penyerangan. Oleh karena itu, token tersebut harus unik untuk setiap *user*. Token tersebut dibuat unik untuk setiap *session user* dan disembunyikan parameter HTML untuk operasi-operasi *server side* yang kemudian dikirim ke *browser client*. Sehingga ketika sebuah user melakukan sesuatu, aksi tersebut harus disertakan CSRF token sebagai alat verifikasi. Apabila CSRF token tidak dimasukkan, kita tidak tahu apabila *request* tersebut benar-benar dari *user* melalui aplikasi tersebut atau bukan.

## Bisakah Membuat Form Secara Manual?
Ya, kita bisa membuat form secara manual pada *file html*, contohnya:
```
<form method="POST" action="">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" class="form-control">
    <input type="password" name="password" placeholder="Password" class="form-control">
    <input class="btn login_btn" type="submit" value="Login">
</form>
```

## Alur Submisi Data pada Django
Pertama, *user* mengisi *form* yang telah disediakan pada halaman web, jika sudah selesai mengisi *form*, maka *user* menekan tombol *"submit"*. Lalu, server akan menerima *HTTP Request* dari *server* dengan *method* "POST" dan memastikan  apakah benar memang *user* mengisi form tersebut melalui aplikasi webnya dengan menggunakan fitur CSRF Token. Setelah itu, salah satu *mapping URL* yang dituju oleh *action* pada *form* tersebut. Lalu, pada fungsi yang sesuai, data dari form tersebut diakses dengan cara ***request.POST[\<input:name>]*** dan melakukan validasi data *form*. Jika data valid, maka buat sebuah objek baru dari model dengan data - data *form* tadi menjadi nilai - nilai atribut modelnya, lalu *save* objek baru tadi. Setelah itu, data bisa ditampilkan pada *template* karena sudah disimpan pada *database*.
## Implementasi *Checklist* Tugas 4
Pertama, saya membuat aplikasi baru bernama ```todolist``` dengan menjalankan perintah

```
python manage.py startapp todolist
```

Setelah itu, tambahkan aplikasi ```todolist``` pada ```settings.py``` di variabel ```INSTALLED_APPS```. Selain itu, tambahkan juga *route* ```/todolist``` ke dalam ```urls.py``` pada folder ```project_django```. Lalu, buat class baru bernama ```Task``` pada ```models.py``` dengan atribut-atribut seperti yang diminta soal sesuai dengan kebutuhannya.
```
lass Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

Setelah itu, kita jalankan
```
python manage.py makemigrations
python manage.py migrate
```

Kode di atas bertujuan untuk mempersiapkan dan melaksanakan pembuatan skema model *database*. 

Setelah itu membuat fungsi untuk mengontrol fitur register, login, serta logout
```
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    if request.user.is_authenticated:
        return redirect(reverse('todolist:show_todolist')) 
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login') # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    if request.user.is_authenticated:
        return redirect(reverse('todolist:show_todolist')) 
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```

Lalu, saya membuat file html untuk menampilkan todolist, login, register, serta pembuatan *task* baru.

Setelah itu, saya tambahkan *path - path* yang sesuai dengan fungsinya pada views.py.
```
urlpatterns = [
    path('', views.show_todolist, name="show_todolist"),
    path('login/', views.login_user, name="login"),
    path('register/', views.register, name="register"),
    path('create-task/', views.create_task, name="create_task"),
    path('logout/', views.logout_user, name="logout"),
    path('delete_task/<int:task_id>', views.delete_task, name="delete_task"),
    path('selesaikan_task/<int:task_id>', views.selesaikan_task, name="selesaikan_task"),
]
```
Terakhir, untuk melakukan *deployment*, saya menambahkan HEROKU_API_KEY dan HEROKU_APP_NAME pada *Secrets* yang ada pada *repository* tugas. Lalu, buka aplikasi tersebut melalui heroku dan register 2 akun dengan masing - masing akun membuat 3 *task*