# zeller_calculator
Zeller Calculator adalah aplikasi terminal Python sederhana yang menghitung **hari dalam seminggu**. Perhitungan dilakukan menggunakan algoritma klasik **Zeller's Congruence**.

---

## 🔧 Fitur

- Validasi input tanggal, bulan, dan tahun
- Perhitungan tahun kabisat
- Validasi jumlah hari dalam bulan
- Hitung nama hari dari tanggal
- Penanganan error saat input bukan angka

---

## 📜 Penjelasan Kode
Kode yang dibuat pada Zeller Calculator Menggunakan 4 Function, dimana Function nya adalah sebagai berikut : 

## 🔍 1. Fungsi `is_kabisat`

Fungsi ini digunakan untuk menentukan apakah suatu tahun adalah tahun kabisat atau bukan.

```python
def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)
```
📖 Penjelasan:
- Tahun yang habis dibagi 4 adalah kabisat,
- Kecuali jika juga habis dibagi 100 (bukan kabisat),
- Kecuali lagi jika habis dibagi 400 (tetap kabisat).

## 🔍 2. Menentukan Jumlah Hari dalam Sebulan

Fungsi ini digunakan untuk memberikan jumlah hari yang sesuai dengan bulan dan tahun. 
```python
def jumlah_hari(bulan, tahun):
    if bulan == 2 : 
        return 29 if is_kabisat(tahun) else 28
    elif bulan in [4,6,9,11]: 
        return 30
    else:
        return 31
```
📖 Penjelasan:
- Jika bulan = 2 maka jumlah hari nya adalah 29 jika tahun kabisat selain itu 28.
- Pada Bulan 4,6,9,11 jumlah harinya adalah 30
- Selain yang disebutkan di atas maka dia adalah 31

## 🔍 3. Meminta dan Memvalidasi Input Angka

Fungsi ini digunakan untuk meminta dan memvalidasi angka yang telah di input. 
```python
def masukan_angka(pesan, min_val=None, max_val=None):
    while True:
        try:
            angka = int(input(pesan))
            if angka < min_val or (max_val is not None and angka > max_val):
                print(f"Nilai harus antara {min_val}" + (f" dan {max_val}" if max_val else "") + ".")
            else:
                return angka
        except ValueError:
            print("Input Harus Berupa Angka.")
```
📖 Penjelasan:
- Pada Script di atas input yang digunakan harus berupa Angka
- Input harus berada dalam batas minimum dan maksimum.

## 🔍 4. Validasi Input Tanggal Lengkap

Fungsi ini digunakan untuk memastikan bahwa inputan sesuai dengan tanggal yang valid. 
```python
def validasi_input():
    tanggal = masukan_angka("Masukan Tanggal (1 s.d 31): ", 1, 31)
    bulan = masukan_angka("Masukan Bulan (1 s.d 12): ", 1, 12)
    tahun = masukan_angka("Masukan tahun (positif) : ", 1)

    # Validasi hari di setiap bulan nya 
    max_hari = jumlah_hari(bulan, tahun)
    if tanggal > max_hari:
        print(f"Tanggal Melebihi jumlah tanggal pada bulan : {bulan} dan tahun : {tahun} !")
        tanggal = masukan_angka("Masukan Tanggal (1 s.d 31): ", 1, 31)
        
    return tanggal, bulan, tahun
```
📖 Penjelasan:
- Pada Script di atas yaitu untuk memastikan bahwa data yang di input, baik tanggal, bulan, tahun adalah valid. 
- Menolak tanggal yang melebihi dari jumlah hari pada bulan tertentu.
  
## 🔍 5. Menghitung Hari dari Tanggal (Zeller's Congruence)

Fungsi ini adalah Logic utama dalam aplikasi Calculato Zeller. 
```python
def hitung_hari(tanggal, bulan, tahun):
    # Penyesuaian bulan dan tahun untuk Zeller
    if bulan == 1 or bulan == 2:
        bulan += 12
        tahun -= 1

    K = tahun % 100
    J = tahun // 100

    h = (tanggal + ((13 * (bulan + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7

    hari_dict = {
        0: "Sabtu",
        1: "Minggu",
        2: "Senin",
        3: "Selasa",
        4: "Rabu",
        5: "Kamis",
        6: "Jumat"
    }

    return hari_dict[h]
```
📖 Penjelasan:
- Script di atas menggunakan Metode **Zeller's Congruence**, yaitu algoritma yang mengubah tanggal menjadi indeks hari (0–6), lalu dipetakan ke nama hari seperti "Senin", "Selasa", dst.

## 🔍 6. Bagian Utama Program
```python
## Main Program
tanggal, bulan, tahun = validasi_input()
hari = hitung_hari(tanggal, bulan, tahun)
print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari {hari}!!")
```
📖 Penjelasan:
- Script di atas digunakan untuk menjalankan programnya.

## ▶️ Contoh Output

```text
Masukan Tanggal (1 s.d 31): 17
Masukan Bulan (1 s.d 12): 8
Masukan tahun (positif) : 1945
Tanggal 17/8/1945 adalah hari Jumat!!
```

## 🚀 Versi Web App

Aplikasi ini dibuatkan juga versi Web nya, cukup buka link berikut:

[![Buka Aplikasi Web](https://img.shields.io/badge/%F0%9F%9A%80%20Buka%20Aplikasi%20Web-blue?logo=streamlit)](https://zellercalculator.streamlit.app/)

🔗 **[https://zellercalculator.streamlit.app/](https://zellercalculator.streamlit.app/)**

---

### 🎯 Apa yang Bisa Kamu Lakukan di Versi Web?

- ✅ Masukkan tanggal, bulan, dan tahun sesuai keinginanmu.
- 🧠 Aplikasi akan langsung menampilkan **hari dalam seminggu** dari tanggal yang kamu input.
- 📱 Dapat diakses lewat **HP, tablet, maupun desktop**.
- 🔒 Kode tidak ditampilkan di Web App — hanya tersedia di GitHub ini.

---

##  📄 Lisensi
Lisensi: MIT License
Bebas digunakan, dimodifikasi, dan dikembangkan, dengan menyertakan atribusi.

##  🤝 Kontribusi
Terbuka untuk kontribusi! Silakan fork repo, buat branch, dan ajukan pull request.
