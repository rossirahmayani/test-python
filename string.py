nama_depan = "Agus"
nama_belakang = "Junaidi"
kota = 'Surabaya'
provinsi = 'Jawa Timur'

nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)
print(kota + ', ' + provinsi)

sapa = "Halo " + nama_lengkap
print(sapa)

# string format
sapa = f"Halo {nama_depan} {nama_belakang}" # f for format
print(sapa)

sapa2 = 'Halo nama saya {} {}'.format(nama_depan, nama_belakang)
print(sapa2)