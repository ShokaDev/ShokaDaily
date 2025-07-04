---

```markdown
# 🎵 Lyric Player in Terminal (Python)

Ini adalah script Python sederhana yang menampilkan **lirik lagu secara animasi di terminal**, dengan efek "mesin ketik" dan jeda waktu per baris. Cocok digunakan untuk membuat konten seperti TikTok dengan gaya terminal.

---

## 📌 Fitur

- Animasi teks huruf per huruf
- Setiap baris punya jeda dan kecepatan tampil sendiri
- Multi-threaded agar timing tiap lirik bisa jalan bersamaan
- Cocok untuk direkam layar sebagai konten video

---

## 🧪 Cara Kerja

- Lirik disimpan dalam list Python, lengkap dengan jeda dan kecepatan tampil
- Fungsi `animate_text()` akan menampilkan tiap karakter satu per satu
- Menggunakan `threading` agar beberapa baris bisa muncul dengan jeda yang berbeda
- **Tidak memutar lagu**, hanya menampilkan teks lirik

---

## 🚀 Teknologi yang Digunakan

- Python 3.x
- Modul standar:
  - `time`
  - `threading`
  - `sys`

---

## 📁 Struktur Folder

Setiap file `.py` di dalam folder ini berisi lirik lagu yang berbeda.  
Semua menggunakan struktur kode yang sama, hanya isi lirik dan waktunya saja yang berbeda.

```

lyric-player/
│
├── right\_now\.py       ← contoh lirik lagu
├── lagu\_lain.py       ← (opsional, file lain milikmu)
├── README.md

````

---

## ▶️ Cara Menjalankan

```bash
python right_now.py

Gantilah `Right_Now.py` dengan nama file lirik lain yang ingin kamu tampilkan.

---

## 📝 Contoh Lirik

> Right now
> I wish you were here with me
> Cause right now
> Everything is new to me
> ...

---

## ⚠️ Catatan

* Tidak ada audio — ini hanya efek visual untuk teks
* Dibuat untuk keperluan konten dan hiburan pribadi
* Pastikan kamu menjalankan di terminal (bukan IDE) agar efek tampil maksimal

---

## 🧠 Tujuan

Script ini dibuat untuk membantu membuat konten dengan gaya teks terminal animasi, terutama untuk video pendek seperti TikTok.

---

## 📖 Lisensi

Gratis digunakan dan dimodifikasi untuk keperluan pribadi atau edukasi.

```

---
