# list
nama = ["Maya", "Claudine", "Nana", "Junna", "Mahiru", "Karen", "Futaba", "Kaoruko"]
nama.append("Hikari")

print(nama)
print(len(nama))
print(nama[4])
print(nama[5])
print(nama[6])


nama.remove("Karen")
print(nama[4])
print(nama[5])
print(nama[6])


nama[4] = "Karen"
print(nama[4])
print(nama[5])
print(nama[6])


# tuple
provinsi_pulau_jawa = ("Banten", "DKI Jakarta", "Jawa Barat", "Jawa Tengah", "DI Yogyakarta", "Jawa Timur") # tidak bisa diubah isinya
print(provinsi_pulau_jawa)
print(len(provinsi_pulau_jawa))
print(provinsi_pulau_jawa[2])

# set
provinsi_pulau_sumatera = {'Riau', 'Sumatera Barat', 'Sumatera Selatan', 'Bengkulu', 'Bengkulu'} # data harus unique, urutan bisa berubah, no index
print(len(provinsi_pulau_sumatera))
print(provinsi_pulau_sumatera)
provinsi_pulau_sumatera.add('Jambi')
print(provinsi_pulau_sumatera)
provinsi_pulau_sumatera.remove('Bengkulu')
print(provinsi_pulau_sumatera)


# dictionary
alamat = {'Kota':'Padang', 'Provinsi':'Sumatera Barat'}
print("Kota     : " + alamat["Kota"])
print("Provinsi : " + alamat["Provinsi"])

print(alamat.items())

for key, value in alamat.items():
    print(f'{key} : {value}')

alamat["Negara"] = "Indonesia"
print(alamat.items())

del alamat["Kota"]
print(alamat.items())

