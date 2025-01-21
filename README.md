### Nama: Qhomar Latif Praditya
### NIM : 23.83.0990

# Sistem Penitipan Barang

## Deskripsi 
Project ini adalah sistem penitipan barang berbasis Python dan menggunakan Flask sebagai backend REST API dan aplikasi berbasis terminal/CLI sebagai clientnya.
```
penitipan_barang/
├── app.py   
├── server/
│   ├── client.py  
│   └── server.py  
├── soal.md
```

## Fitur Utama
- **CRUD (Create, Read, Update, Delete)** barang dengan menggunakan REST API.
- Penyimpanan data barang menggunakan struktur list yang sederhana.
- Pemisahan antara barang yang dititipkan dan juga barang yang sudah diambil.
- CLI(Command Line Interface) untuk interaksi pengguna.

## Tools yang Digunakan
- **Bahasa Pemrograman:** Python 
- **Framework:** Flask
- **Library:** Requests
- **Tools:** Visual Studio Code, IDLE (Python)

## Cara Menjalankan Program

### 1. Menjalankan Server
1. Buka terminal dan navigasikan ke folder `server/`.
2. Jalankan perintah berikut:
   ```bash
   python client.py
   ```
3. Server akan berjalan di `http://127.0.0.1:5000`

### 2. Menjalankan Client
1. Buka terminal baru dan navigasikan ke folder penitipan_barang
2. Jalankan perintah berikut:
   ```bash
   python app.py
   ```
3. Ikuti instruksi yang ada pada cli untuk mengelola barang.

## Endpoint API
| Metode | Endpoint          | Deskripsi                        |
|--------|------------------|----------------------------------|
| GET    | /items            | Melihat daftar barang           |
| POST   | /items            | Menambahkan barang baru         |
| PUT    | /items/<id>       | Memperbarui data barang         |
| DELETE | /items/<id>       | Menghapus barang berdasarkan ID |
| POST   | /items/take/<id>  | Mengambil barang berdasarkan ID |

## Contoh Penggunaan API dengan Curl
- Menambahkan barang:
  ```bash
  curl -X POST http://127.0.0.1:5000/items -H "Content-Type: application/json" -d '{"id":1, "nama":"Laptop", "pemilik":"John"}'
  ```

- Melihat daftar barang:
  ```bash
  curl -X GET http://127.0.0.1:5000/items
  ```
