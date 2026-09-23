# README — Tugas Individu Pelcod

## 1. Deskripsi Project

Project ini adalah program Python sederhana untuk **menghitung nilai akhir mahasiswa dan menentukan status kelulusan berdasarkan nilai dan kehadiran**.

Program menggunakan:
- Nilai tugas
- Nilai kuis
- Nilai ujian
- Persentase kehadiran

Kemudian program menghitung nilai akhir dengan bobot tertentu dan menggunakan percabangan `if`, `elif`, dan `else` untuk menentukan predikat.

File utama project:
- `tugas individu pelcod.py`

## 2. Data yang Digunakan

Pada program, data awal mahasiswa adalah:

```python
nama = "caila"
nilai_tugas = 90
nilai_kuis = 93
nilai_ujian = 98
kehadiran = 97
```

Artinya:
- Nama mahasiswa: Caila
- Nilai tugas: 90
- Nilai kuis: 93
- Nilai ujian: 98
- Kehadiran: 97%

Nilai-nilai tersebut disimpan dalam **variabel** agar dapat digunakan dalam proses perhitungan.

## 3. Cara Menghitung Nilai Akhir

Program menghitung nilai akhir menggunakan rumus:

```python
nilai_akhir = ((nilai_tugas * 0.30) + (nilai_kuis * 0.20) + (nilai_ujian * 0.50))
```

Bobot yang digunakan:

| Komponen | Bobot |
|---|---:|
| Tugas | 30% |
| Kuis | 20% |
| Ujian | 50% |

Dengan data pada program:

- Tugas: `90 × 30% = 27`
- Kuis: `93 × 20% = 18,6`
- Ujian: `98 × 50% = 49`

Jadi:

**Nilai akhir = 27 + 18,6 + 49 = 94,6**

## 4. Logika Penentuan Kelulusan

Setelah nilai akhir dihitung, program memeriksa kehadiran dan nilai menggunakan percabangan.

### Kondisi 1 — Tidak Lulus karena Kehadiran

```python
if kehadiran < 75:
    status = "Tidak Lulus"
```

Jika kehadiran kurang dari 75%, mahasiswa langsung dinyatakan **Tidak Lulus**.

### Kondisi 2 — Predikat A

```python
elif nilai_akhir >= 85 and kehadiran >= 80:
    status = "Lulus dengan Predikat A"
```

Syarat:
- Nilai akhir minimal 85
- Kehadiran minimal 80%

### Kondisi 3 — Predikat B

```python
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "Lulus dengan Predikat B"
```

Syarat:
- Nilai akhir minimal 75
- Kehadiran minimal 80%

### Kondisi 4 — Predikat C

```python
elif nilai_akhir >= 65 and kehadiran >= 75:
    status = "Lulus dengan Predikat C"
```

Syarat:
- Nilai akhir minimal 65
- Kehadiran minimal 75%

### Kondisi 5 — Tidak Memenuhi Syarat

```python
else:
    status = "Tidak Lulus"
```

Jika tidak memenuhi kondisi-kondisi sebelumnya, status menjadi **Tidak Lulus**.

## 5. Urutan Kerja Program

Secara sederhana, alur program adalah:

```text
Mulai
  ↓
Masukkan data mahasiswa
  ↓
Hitung nilai akhir
  ↓
Apakah kehadiran < 75%?
  ├── Ya → Tidak Lulus
  └── Tidak
        ↓
   Apakah nilai akhir ≥ 85
   dan kehadiran ≥ 80%?
        ├── Ya → Predikat A
        └── Tidak
              ↓
        Apakah nilai akhir ≥ 75
        dan kehadiran ≥ 80%?
              ├── Ya → Predikat B
              └── Tidak
                    ↓
              Apakah nilai akhir ≥ 65
              dan kehadiran ≥ 75%?
                    ├── Ya → Predikat C
                    └── Tidak → Tidak Lulus
  ↓
Tampilkan hasil
  ↓
Selesai
```

## 6. Output Program

Bagian akhir program menggunakan `print()`:

```python
print("===== HASIL PENILAIAN =====")
print("Nama           :", nama)
print("Nilai Akhir    :", nilai_akhir)
print("Kehadiran      :", str(kehadiran) + "%")
print("Status         :", status)
```

Dengan data yang tersedia, hasilnya secara logika adalah:

```text
===== HASIL PENILAIAN =====
Nama           : caila
Nilai Akhir    : 94.6
Kehadiran      : 97%
Status         : Lulus dengan Predikat A
```

## 7. Materi Python yang Bisa Dipelajari

Project ini cocok untuk belajar beberapa konsep dasar Python:

### Variabel

Variabel digunakan untuk menyimpan data.

```python
nilai_tugas = 90
```

### Operasi Aritmatika

Program menggunakan perkalian dan penjumlahan untuk menghitung nilai akhir.

```python
nilai_tugas * 0.30
```

### Percabangan `if`

Digunakan untuk mengecek suatu kondisi.

```python
if kehadiran < 75:
    status = "Tidak Lulus"
```

### `elif`

Digunakan untuk memeriksa kondisi lain jika kondisi sebelumnya tidak terpenuhi.

```python
elif nilai_akhir >= 85 and kehadiran >= 80:
```

### `else`

Digunakan ketika tidak ada kondisi sebelumnya yang terpenuhi.

```python
else:
    status = "Tidak Lulus"
```

### Operator Perbandingan

Program menggunakan operator seperti:

- `<` → kurang dari
- `>=` → lebih besar atau sama dengan

Contoh:

```python
nilai_akhir >= 85
```

### Operator Logika `and`

`and` berarti **kedua kondisi harus benar**.

```python
nilai_akhir >= 85 and kehadiran >= 80
```

Artinya nilai akhir harus minimal 85 **dan** kehadiran harus minimal 80%.

### `print()`

Digunakan untuk menampilkan hasil ke layar.

## 8. Cara Menjalankan Program

Pastikan Python sudah terpasang.

Kemudian buka terminal pada folder project dan jalankan:

```bash
python "tugas individu pelcod.py"
```

Jika menggunakan `python3`, dapat menjalankan:

```bash
python3 "tugas individu pelcod.py"
```

## 9. Latihan Agar Lebih Paham

Setelah memahami program, coba ubah bagian berikut:

### Latihan 1 — Ubah nilai

Coba ubah:

```python
nilai_tugas = 70
nilai_kuis = 80
nilai_ujian = 75
kehadiran = 85
```

Kemudian perhatikan perubahan nilai akhir dan status.

### Latihan 2 — Ubah kehadiran

Coba gunakan:

```python
kehadiran = 70
```

Perhatikan apakah status berubah menjadi **Tidak Lulus**.

### Latihan 3 — Buat data mahasiswa sendiri

Ganti:

```python
nama = "caila"
```

dengan nama sendiri dan masukkan nilai yang berbeda.

### Latihan 4 — Pahami urutan `if`

Coba jelaskan dengan kata-kata sendiri mengapa program memeriksa:

1. Kehadiran kurang dari 75%
2. Predikat A
3. Predikat B
4. Predikat C
5. Selain kondisi tersebut → Tidak Lulus

## 10. Kesimpulan

Project ini merupakan latihan dasar Python yang menggabungkan **variabel, operasi aritmatika, percabangan, operator perbandingan, operator logika, dan output**.

Hal utama yang perlu dipahami bukan hanya hasil akhirnya, tetapi juga **bagaimana data diproses dari awal sampai program menentukan status mahasiswa**.
