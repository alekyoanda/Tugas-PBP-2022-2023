# Tugas 5 PBP
## Link Aplikasi Heroku
https://tugas2-pbp-alek.herokuapp.com

## Inline, Internal, dan External CSS
### Inline CSS
Inline CSS umumnya digunakan untuk menata tag HTML tertentu saja. Kita dapat melakukan *styling* dengan CSS hanya dengan menambahkan atribut ```style``` ke tag HTML.\
Contoh:
```
<h1 style="background-color:yellow;"> Ini heading dengan warna background kuning</h1>
<p style="color:red"> Ini paragraf dengan tulisan berwarna merah</p>
```
#### Kelebihan:
<ul>
    <li> Tidak perlu membuat atau menautkan dokumen terpisah seperti yang disyaraktkan di external CSS.
    <li> Berguna untuk menguji atau melihat pratinjau perubahan, dan melakukan perbaikan cepat ke halaman html.
</ul>

#### Kekurangan:
<ul>
    <li>Kita perlu menulis CSS styling di setiap tag HTML satu per satu. Jadi mengelola aplikasi web yang besar mungkin tidak efektif dan efisien.
    <li> Menata banyak tag HTML dengan Inline CSS dapat memengaruhi ukuran halaman dan waktu pengunduhan
</ul>

### Internal CSS
Internal CSS biasanya digunakan untuk melakukan *styling* pada satu halaman HTML. Kita dapat menulis CSS internal dengan menggunakan tag ```<style>``` yang dimasukkan di dalam tag ```<head>``` pada sebuah halaman html.\
Contoh:
```
<!DOCTYPE html>
<html>
    <head>
        <style>
            body {
                background-color: red;
            }
            h1 {
                color: maroon;
                margin-left: 40px;
            }
        </style>
    </head>
    <body>
        <h1>Ini heading</h1>
        <p>Ini paragraf</p>
    </body>
</html>
```

#### Kelebihan:
<ul>
    <li> Kita dapat menggunakan ID dan Class selector untuk melakukan CSS styling.
    <li> Tidak perlu membuat atau menautkan dokumen terpisah seperti yang disyaraktkan di external CSS.
</ul>

#### Kekurangan:
<ul>
    <li>Karena kita hanya akan menambahkan kode CSS dalam satu halaman HTML, menata beberapa halaman HTML akan memakan waktu.
    <li> Menambahkan kode CSS ke tiap halaman HTML dapat meningkatkan ukuran halaman dan waktu pemuatan.
</ul>

### External CSS
Dengan external CSS, kita dapat mengubah tampilan seluruh halaman html hanya dengan mengubah satu file CSS. Kita dapat menulis external CSS dalam file ```.css``` terpisah. Setiap halaman HTML harus menyertakan referensi ke file CSS eksternal tadi di dalam tag ```<link href=|nama-file-css|>```, di dalam tag ```<head>```.\
Contoh:

Berikut adalah file CSS-nya, misal nama filenya ```style.css```:
```
h1{
   background-color:orange;
}
.box{
   height:200px;
   width:300px;
   background-color:yellow;
}
#circle{
   height:200px;
   width:200px;
   background-color:red;
   border-radius:50%;
}
```
Lakukan *linking* dari file HTML ke file CSS tersebut:
```
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="my-style.css" />
    </head>
    <body>
        <h1>Simple example of external CSS</h1>
        <div class="box"></div>
        <div id="circle"></div>
  </body>
</html>
```
#### Kelebihan:
<ul>
    <li> Karena kode CSS berada dalam file terpisah, halaman HTML Anda akan memiliki struktur yang rapi dan ukurannya lebih kecil.
    <li> Kita dapat menggunakan file .css yang sama untuk beberapa halaman HTML jika kita menginginkan tampilan yang sama untuk setiap halaman.
</ul>

#### Kekurangan:
<ul>
    <li>Halaman Web kita mungkin tidak te-render dengan benar hingga external CSS dimuat.
</ul>

## Macam - Macam Tag HTML5
Beberapa tag HTML5 yang saya tau adalah sebagai berikut:

```
1. <h1> - <h6>  : Typography khusus header pada halaman web
2. <a>          : Menautkan elemen HTML ke sebuah tautan
3. <form>       : Membuat sebuah form pada halaman web
4. <p>          : Typography khusus penulisan paragraf pada halaman web
5. <img>        : Memuat sebuah gambar pada halaman web
6. <table>      : Membuat sebuah tabel pada halaman web
7. <style>      : Melakukan internal CSS styling
```

## Tipe - Tipe CSS Selector
Terdapat beberapa tipe CSS Selector, antara lain:

### 1. CSS Element Selector
Selector tipe ini memilih elemen berdasarkan nama tag HTML-nya.\
Contoh:
```
p{  
    text-align: center;  
    color: blue;  
}   
```
### 2. CSS Id Selector
Selector tipe ini memilih elemen berdasarkan Id dari elemennya yang bersifat unik. Cara menggunakan selector tipe ini adalah dengan menulis ```#```, dilanjutkan dengan Id elemennya.
Contoh:
```
#para1 {  
    text-align: center;  
    color: blue;  
}  
```
### 3. CSS Class Selector
Selector tipe ini memilih elemen HTML dengan atribut ```class``` tertentu. Digunakan dengan karakter titik ```.``` diikuti dengan nama class-nya.\
Contoh:
```
.center {  
    text-align: center;  
    color: blue;  
}  
```
## Implementasi Tugas 5
Pertama, saya melakukan *linking* bootstrap *framework* pada folder ```base.html``` yang ada di ```project_django```.
Setelah itu, saya membuat sebuah folder dengan nama ```static/todolist``` pada aplikasi ```todolist```, dimana terdapat 2 buah file CSS dalam folder tersebut. File CSS pertama namanya ```style_login.css```. File CSS tersebut akan mengatur *styling* dari beberapa file HTML, yaitu ```login.html```, ```register.html```, dan ```create_task.html```. Sedangkan, file CSS kedua dengan nama ```style_index.css``` akan mengatur *styling* dari file HTML ```show_todolist.html```.Setelah itu, saya melakukan *linking* file HTML yang saya tujukan tadi ke file CSS-nya masing - masing dengan menggunakan baris kode berikut:
```
<link rel="stylesheet" href="{% static 'todolist/<nama_file_css>' %}">
```
Setelah itu, saya melakukan *styling* dengan menggunakan CSS dan juga bootstrap. Pada ```show_todolist.html```, saya membuat sebuah ```card``` untuk merepresentasikan 1 buah task dengan menggunakan bootstrap. Lalu, saya juga melakukan *styling* pada ```card``` tersebut di file CSS agar bisa menerapkan efek *hover*. Tidak lupa juga saya membuat semua halaman web saya menjadi *responsive* dengan menggunakan ```media query``` yang ditulis pada file CSS.

---
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