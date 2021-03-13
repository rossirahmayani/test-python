import function

# list of dictionary
contacts = []
contacts.append({
    "name":"Rossi",
    "email":"rr21@mail.com",
    "phone":"081234567890"
})

# menu program
while True:
    print("=== Menu Kontak ===")
    print("1. Daftar")
    print("2. Tambah")
    print("3. Hapus")
    print("4. Cari")
    print("0. Keluar")

    menu = input("Pilih menu: ")

    if menu == '0':
        break
    elif menu == '1':
        function.get_contact(contacts)
    elif menu == '2':
        function.new_contact(contacts)
    elif menu == '3':
        function.del_contact(contacts)
    elif menu == '4':
        function.find_contact(contacts)
    else:
        print('Menu tidak tersedia.')

print("Program selesai, sampai jumpa.")