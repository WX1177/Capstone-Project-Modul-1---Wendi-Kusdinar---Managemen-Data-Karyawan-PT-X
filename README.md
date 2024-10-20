# Manajemen Data Karyawan PT X

Selamat datang di project **Manajemen Data Karyawan PT X**! project ini bertujuan untuk memudahkan pengelolaan data karyawan tanpa menggunakan database eksternal atau SQL. Program ini memanfaatkan Python dan library **Tabulate** untuk menampilkan data dalam format tabel yang rapi.

## Daftar Isi
- [Gambaran Project](#gambaran-project)
- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi & Pengaturan](#instalasi--pengaturan)

## Gambaran Project
Sistem Manajemen Data Karyawan ini adalah project berbasis Python yang dirancang untuk mengelola catatan karyawan secara efisien. Sistem ini memungkinkan pengguna untuk membuat, membaca, memperbarui, dan menghapus (CRUD) data karyawan, memastikan pengelolaan informasi karyawan yang penting berjalan lancar.

Project ini bertujuan untuk memberikan solusi yang terstruktur dan skalabel bagi organisasi yang perlu mengelola catatan karyawan, sambil memastikan kemudahan penggunaan dan fleksibilitas.

## Fitur Utama
- 📊 **Laporan Data Karyawan**: Menampilkan seluruh data karyawan dalam format tabel.
- 🔍 **Mencari Data Karyawan**: Mencari data berdasarkan NIK, nama, posisi, bagian, atau domisili.
- ➕ **Menambah Data Karyawan**: Menambahkan data karyawan baru dengan validasi NIK.
- ✏️ **Merubah Data Karyawan**: Mengupdate informasi karyawan yang ada.
- 🗑️ **Menghapus Data Karyawan**: Menghapus data karyawan berdasarkan NIK.
  
## Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python
- **Penyimpanan Data**: Struktur data dalam memori (dictionary)
- **Library**:
  - **Tabulate**: Untuk menampilkan data dalam format tabel

## Instalasi & Pengaturan
1. Library
   ```bash
   pip install tabulate
2. Jalankan program:
    ```bash
   python main.py

## Penggunaan

- **Laporan Karyawan**:
Pilih untuk menampilkan semua data karyawan NIK/ID, Posisi, Bagian, Domisili dalam bentuk tabel.
- **Mencari Karyawan**:
Pilih untuk mencari data karyawan berdasarkan NIK/ID, Posisi, Bagian, Domisili mereka.
- **Menambah Karyawan**:
Sistem akan meminta Anda untuk memasukkan detail karyawan seperti nama, ID, departemen, dan posisi.
Setelah menambah, sistem akan mengonfirmasi bahwa data telah berhasil ditambahkan.
- **Menghapus Karyawan**:
Hapus seorang karyawan dengan memasukkan ID mereka.
- **Merubah/Memperbarui Karyawan**:
Pilih seorang karyawan berdasarkan ID mereka dan berikan data baru untuk diperbarui.


