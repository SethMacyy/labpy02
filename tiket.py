# Harga tiket
harga_reguler = 50000
harga_vip = 100000

# Input dari user
tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

# Menentukan harga tiket berdasarkan tipe tiket
harga_tiket = harga_reguler if tipe_tiket == "reguler" else harga_vip

# Menghitung harga setelah diskon jika user adalah member
total_harga = harga_tiket * 0.8 if status_member == "ya" else harga_tiket

# Output hasil perhitungan
print(f"Total harga yang harus dibayar: Rp{total_harga}")
