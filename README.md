- [x]Membuat sebuah proyek Django baru.
    disini saya membuat proyek django baru dengan tema football shop jadi project yang dibuat saya beri nama goalies safehouse. sama memilih project ini karena saya merasa ini akan jadi menarik ketika football shop ini menjual peralatan khusus kiper.
    pada pembuatan project ini awalnya saya membuat repo baru dulu di github dengan nama 'Goalie-s-Safehouse' lalu saya melakukan cloning dari repo itu ke lokal dan saya mulai melakukan berbagai konfigurasi menggunakan folder hasil kloning itu. disitu saya memulai dengan mengunduh requirements yang dibutuhkan untuk project django setelah itu saya konfigurasi dari env, env.prod, settings database dan lain lain. setelah siap saya mencoba menjalankan server untuk memastikan bahwa project berhasil dibuat.

- [x]Membuat aplikasi dengan nama main pada proyek tersebut.
    disini saya membuat aplikasi dengan nama main dari project tersebut, lalu saya membuat folder templates yang berisikan file html yang nantinya akan digunakan untuk menampilkan informasi project saya, nama saya, npm saya, dan juga kelas saya. lalu saya mengisi bagian models sesuai dengan permintaan yang ada seperti di permintaan 4. setelah itu selesai saya melakukan routing dengan melakukan perubahan pada views.py, urls.py di main, dan urls.py di project utama.

- [x]Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    bagian ini saya lakukan setelah bagian pembuatan model selesai jadi saya membuat model terlebih dahulu baru melakukan routing sesuai dengan permintaan 5 dan 6

- [x]Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
    name sebagai nama item dengan tipe CharField.
    price sebagai harga item dengan tipe IntegerField.
    description sebagai deskripsi item dengan tipe TextField.
    thumbnail sebagai gambar item dengan tipe URLField.
    category sebagai kategori item dengan tipe CharField.
    is_featured sebagai status unggulan item dengan tipe BooleanField.

    saya membuat model pada models.py dengan atribut seperti yang diminta. setelah itu saya melakukan routing

- [x]Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    mengisi views.py dengan fungsi yang akan mengembalkan nilai kedalam template html yang nantinya digunakan untuk menampilkan nama project, nama saya, npm saya, dan juga kelas saya

- [x]Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    melakukan routing agar views.py dapat dipanggil dan informasinya dapat melengkapi template html. disini saya melakukan perubahan pada urls.py di main terlebih dahulu baru dilanjutkan menambahkan informasinya ke urls.py di project utama.

- [x]Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    sebagai langkah terakhir saya melakukan push git hub pekerjaan saya terdokumentasi dengan jelas dan saya melakukan push pws agar project ini dapat dilihat semua orang yang mengakses internet

- [x]Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). saya sudah menjelaskan dibagian atas

    - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    ```mermaid
    flowchart TD
        A[Client Browser] -->|HTTP Request| B[urls.py]
        B --> C[views.py]
        C -->|Ambil data| D[models.py]
        D --> C
        C --> E[Template HTML]
        E -->|HTTP Response| A
    ```
    
    jadi pertama ketika ketika pengguna mengakses URL tertentu maka Django akan mencocokkan URL request dengan pola (pattern) yang sudah didefinisikan di urls.py yang nantinya request diarahkan ke fungsi/kelas tertentu di views.py. Fungsi di views.py menerima request. Jika butuh data dari database, views.py memanggil models.py. models.py menyediakan interface antara views.py dan database jadi melalui models.py data data yang dibutuhkan akan diambil. setelah data diambil maka akan dimasukan ke HTML. HTML ini berisi struktur tampilan halaman web yang nantinya akan diakses pengguna. setelah semua data dimasukan ke HTML maka HTML ini akan dikembalikan ke client broser jadi pengguna dapat melihat tampilannya.

    
    - Jelaskan peran settings.py dalam proyek Django!
        settings.py ini layaknya sebuah pusat penganturan. semua konfigurasi dari framework django ada di file settings.py. mulai dari pengaturan database, pengaturan aplikasi yang diinstal, host yang diizinkan dan juga beberapa konfigurasi yang belum saya pelari seperti Middleware, Security, dan Authentication.
    
    - Bagaimana cara kerja migrasi database di Django?
        pentingnya migrasi dalam menggunakan framework django adalah ketika kita mengubah model (misalnya menambah field, menghapus field, atau membuat model baru), Django menyediakan cara otomatis untuk memperbarui skema database tanpa harus menulis SQL manual. prosesnya adalah ketika kita ada perubahan di models.py maka di terminal kita dapat menjalan kan perintah python manage.py makemigrations. dengan menjalankan perintah ini maka django akan membuat folder berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. setelah itu, dapat menjalankan perintah python manage.py migrate. dengan perintha migrate ini django akan mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data.
    
    - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
        menurut saya karena dengan menggunakan django karena django sudah memiliki banyak fitur bawaan. selain itu django juga terbilang cepat dalam proses developmentnya jadi cocok untuk belajar dan yang paling penting django memiliki komunitas yang besar dan aktif. komunitas yang aktif ini menandakan bahwa django memang relevan dengan industri saat ini.
    
    - Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya? asdos sudah sangat membantu selama tutorial 1 dan 0, semangat trus kakak-kakak asdos