# Tugas 3 PBP

## Link Aplikasi Heroku
https://tugas2-pbp-alek.herokuapp.com

## Perbedaan Antara JSON, XML, dan HTML
### HTML
HTML merupakan singkatan dari *Hypertext Markup Language*. HTML digunakan sebagai struktur dokumen standar dari sebuah halaman *web*. HTML tersusun dari banyak *built-in tag* yang bisa kita gunakan, sedangkan ***tag*** sendiri bisa memiliki **atribut**. 

Berikut merupakan struktur dasar HTML:
```
<html>
  <head>
    <title>My Website</title>
  </head>
  <body>
    <a href="www.google.com">Link Menuju Google</a>
  </body>
</html>
```
Sintaks sebuah *tag* pad HTML adalah ```"<...>"```. Misalnya, ```<a>``` merupakan sebuah *tag* dengan atribut ```href```. Sebuah *tag* biasanya ditutup dengan sintaks ```</...>```.

### JSON
JSON merupakan singkatan dari *JavaScript Object Notation*. JSON digunakan sebagai format *data delivery* dalam bentuk *key-value pair*. Data-data yang berbeda dipisah dengan karakter koma (```,```).

Berikut merupakan contoh data yang disimpan dalam format JSON:
```
{
  "movie": "The Shawshank Redemption",
  "release_date": "1994-09-10",
  "reviews": [
    {
      "description": "Very good film!!",
      "rating": 5
    },
    {
      "description": "I like this film!",
      "rating": 4
    }
  ]
}
```
*Key* dan *value* pada JSON dipisahkan dengan karakter titik dua (```:```), dimana *key* terletak di sebelah kiri karakter titik dua, sedangkan *value*-nya terletak di sebelah kanan karakter titik dua. Data pada JSON bersifat *nested*, sehingga sebuah *value* juga bisa menjadi *key-value pair*. Sebuah *value* juga bisa mengandung lebih dari satu data *key-value pair*, contohnya pada data di atas adalah sebuah *key* ```reviews``` memiliki 2 data *review*, dimana tiap *review* memiliki *key-value pair* ```description``` dan ```rating```.

### XML
XML merupakan singkatan dari *Extensible Markup Language*, dimana XML digunakan untuk melakukan *data delivery*, seperti halnya JSON. Namun, hal yang membedakan antara XML dengan JSON adalah formatnya yang cukup serupa dengan HTML, di mana XML menggunakan *tag*. Tetapi, berbeda dengan HTML yang hanya terdapat *built-in tag*, pada XML kita bisa membuat nama *tag* sendiri sesuai dengan data yang kita miliki.

Berikut merupakan contoh data yang disimpan dalam format XML:
```
<watchlist>
   <movie>
      <title>The Shawshank Redemption</title>
      <release_date>1994-09-10</release_date>
   </movie>
   <movie>
      <title>Avengers: Infinity War</title>
      <release_date>2018-04-23</release_date>
   </movie>
</watchlist>
```

## Pentingnya *Data Delivery* dalam Pengimplementasian Sebuah Platform
*Data delivery* sangat penting di dalam pengimplementasian sebuah *platform* pada aplikasi yang melakukan pengaksesan data pada sebuah *database*. Jika tidak ada mekanisme *data delivery*, maka data dari *database* tidak bisa ditampilkan kepada *client*.

## Implementasi *Checklist* Tugas 3
Pertama, saya membuat aplikasi baru bernama ```mywatchlist``` dengan menjalankan perintah

```
python manage.py startapp mywatchlist
```

Setelah itu, tambahkan aplikasi ```mywatchlist``` pada ```settings.py``` di variabel ```INSTALLED_APPS```. Selain itu, tambahkan juga *route* ```/mywatchlist``` ke dalam ```urls.py``` pada folder ```project_django```. Lalu, buat class baru bernama ```MyWatchList``` pada ```models.py``` dengan atribut-atribut seperti yang diminta soal sesuai dengan kebutuhannya. Setelah itu, kita jalankan

```
python manage.py makemigrations
python manage.py migrate
```

Kode di atas bertujuan untuk mempersiapkan dan melaksanakan skema model. Setelah itu, saya membuat folder bernama ```fixtures``` di dalam aplikasi ```mywatchlist``` dan membuat file bernama ```initial_watchlist_data.json``` yang berisi 10 data sesuai dengan skema model ```MyWatchList``` yang telah dibuat sebelumnya. Lalu, saya menjalankan perintah 
```
python manage.py loaddata initial_wishlist_data.json
``` 
untuk memasukkan data tersebut ke dalam *database*.

Setelah itu, saya melanjutkan dengan menyajikan data dalam HTML, XML, dan JSON dengan membuat 3 fungsi yang ```handle``` masing-masing format di ```views.py``` pada folder ```mywatchlist```. Untuk HTML, saya mengakses semua data pada *database*, serta dimasukkan ke dalam sebuah *dictionary* bernama ```context```. Lalu, dilanjutkan dengan menggunakan fungsi ```render()``` dengan ```request```, ```context```, dan *file template*``` mywatchlist.html```.

Pada XML dan JSON, seperti pada HTML, saya mengakses semua data pada *database*. Namun, yang berbeda adalah fungsi untuk kedua format ini mengembalikan ```HttpResponse``` yang isinya adalah data yang di-*serialize* sesuai dengan tipe penyajian datanya, yaitu JSON atau XML.

Setelah itu, buatlah *path-path* untuk penyajian data HTML, XML, dan JSON ke dalam ```urls.py``` pada folder ```mywatchlist```. Sesuaikan dengan fungsi yang ada pada ```views.py```. 

Dalam melakukan *deployment*, saya melakukan *push* ke *remote* dari Tugas 2 PBP sebelumnya yang sudah di-*deploy* sehingga projek kali ini langsung ter-*deploy* ulang.

## Pemeriksaan *Routes* dengan Postman
```mywatchlist/html```
<img width="956" alt="html" src="https://user-images.githubusercontent.com/84554095/191294810-4ff2899f-ae7b-47fc-abe0-1a4424b3a259.png">

```mywatchlist/json```
<img width="960" alt="json" src="https://user-images.githubusercontent.com/84554095/191294879-d3b45a39-de01-4f5f-9436-dda2727d5d23.png">

```mywatchlist/xml```
<img width="960" alt="xml" src="https://user-images.githubusercontent.com/84554095/191294911-c685addc-a6de-4b66-8e18-e5a6ea77198e.png">
