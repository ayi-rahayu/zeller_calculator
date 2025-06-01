import streamlit as st

def is_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

def jumlah_hari(bulan, tahun):
    if bulan == 2:
        return 29 if is_kabisat(tahun) else 28
    elif bulan in [4, 6, 9, 11]:
        return 30
    return 31

def hitung_hari(tanggal, bulan, tahun):
    if bulan < 3:
        bulan += 12
        tahun -= 1
    K = tahun % 100
    J = tahun // 100
    h = (tanggal + ((13 * (bulan + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7
    hari_dict = ["Sabtu", "Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    return hari_dict[h]

# --- Tampilan App ---
st.set_page_config(page_title="Zeller Calculator", page_icon="📆")

st.title("📅 Zeller Calculator")
st.write("Masukkan tanggal, bulan, dan tahun untuk mengetahui harinya.")

# Input pengguna
tanggal = st.number_input("Tanggal", min_value=1, max_value=31, value=1)
bulan = st.number_input("Bulan", min_value=1, max_value=12, value=1)
tahun = st.number_input("Tahun", min_value=1, value=2024)

# Tombol Proses
if st.button("Hitung Hari"):
    max_hari = jumlah_hari(bulan, tahun)
    if tanggal > max_hari:
        st.error(f"Tanggal melebihi jumlah hari pada bulan {bulan} dan tahun {tahun}.")
    else:
        hari = hitung_hari(tanggal, bulan, tahun)
        st.success(f"🗓️ Tanggal {tanggal}/{bulan}/{tahun} adalah hari **{hari}**!")
