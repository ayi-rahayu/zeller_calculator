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

## 🔍 Fungsi `is_kabisat`

Fungsi ini digunakan untuk menentukan apakah suatu tahun adalah tahun kabisat atau bukan.

```python
def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

📖 Penjelasan:
- Tahun yang habis dibagi 4 adalah kabisat,
- Kecuali jika juga habis dibagi 100 (bukan kabisat),
- Kecuali lagi jika habis dibagi 400 (tetap kabisat).






