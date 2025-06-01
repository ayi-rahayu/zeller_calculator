def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari(bulan, tahun):
    if bulan == 2 : 
        return 29 if is_kabisat(tahun) else 28
    elif bulan in [4,6,9,11]: 
        return 30
    else:
        return 31
    
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

## Main Program
tanggal, bulan, tahun = validasi_input()
hari = hitung_hari(tanggal, bulan, tahun)
print(f"Tanggal {tanggal}/{bulan}/{tahun} adalah hari {hari}!!")