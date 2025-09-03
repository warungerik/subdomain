# Fast Subdomain Scanner 🚀

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Fast Subdomain Scanner adalah sebuah alat command-line sederhana namun kuat yang ditulis dengan Python untuk menemukan subdomain dari sebuah domain target. Alat ini menggunakan wordlist dan memanfaatkan multithreading untuk melakukan pemindaian dengan sangat cepat.



---

## ✨ Fitur Utama

- **Pencarian Berbasis Wordlist**: Menggunakan file `wordlist.txt` untuk melakukan brute-force subdomain.
- **Multithreading**: Didesain untuk kecepatan maksimal dengan mengirimkan puluhan permintaan secara bersamaan.
- **Resolusi IP**: Secara otomatis menampilkan alamat IP dari setiap subdomain yang ditemukan.
- **Pengecekan Status HTTP**: Memvalidasi subdomain dengan memeriksa status kode HTTP (misalnya 200 OK, 404 Not Found, dll.).
- **Tampilan Interaktif**: Dilengkapi dengan progress bar (`tqdm`) untuk memantau proses pemindaian secara real-time.
- **Output Berwarna**: Menggunakan `termcolor` untuk output yang mudah dibaca, di mana status kode diberi warna berbeda.

---

## 🛠️ Instalasi

Untuk menjalankan alat ini, Anda hanya memerlukan Python 3. Ikuti langkah-langkah di bawah ini.

**1. Clone Repositori**

```bash
git clone [https://github.com/warungerik/subdomain.git](https://github.com/warungerik/subdomain.git)
cd subdomain
```
**2. Instal Dependensi**

Jalankan perintah berikut untuk menginstal semua library yang dibutuhkan dari file `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

## ▶️ Cara Penggunaan

Penggunaan alat ini sangat mudah.

**1. Siapkan Wordlist Anda**

Pastikan Anda memiliki file `wordlist.txt` di dalam direktori yang sama. Isi file ini dengan daftar calon subdomain, satu per baris. Contoh:

```
www
api
dev
blog
mail
```
> Anda bisa mengunduh wordlist yang lebih lengkap dari repositori seperti [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS).

**2. Jalankan Script**

Gunakan perintah di bawah ini di terminal Anda, ganti `domain.com` dengan target yang Anda inginkan.

```bash
python main.py domain.com
```

**Contoh:**
```bash
python main.py google.com
```

---

## ⚠️ Disclaimer

Alat ini dibuat untuk tujuan edukasi dan pengujian keamanan yang sah. Pengguna bertanggung jawab penuh atas tindakan mereka saat menggunakan alat ini. Jangan gunakan alat ini untuk melakukan pemindaian pada domain tanpa izin eksplisit dari pemiliknya. Pengembang tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh program ini.