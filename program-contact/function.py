
def get_contact(contacts):
    print("=================================")
    for c in contacts:
        print(f"Nama    : {c['name']}")
        print(f"Email   : {c['email']}")
        print(f"Telepon : {c['phone']}")
        print("=================================")


def new_contact(contacts):
    name = input("Nama : ")
    email = input("Email : ")
    phone = input("Telepon : ")

    contact = {
        'name' : name,
        'email' : email,
        'phone' : phone
    }
    
    contacts.append(contact)
    print("Kontak sudah ditambahkan")

def del_contact(contacts):
    phone = input("Cari Telepon : ")
    index = -1

    for i in range(0, len(contacts)):
        con = contacts[i]
        if (phone == con["phone"]):
            index = i
            break
    
    if(index == -1):
        print("Kontak tidak ditemukan")
    else:
        del contacts[index]
        print("Kontak sudah dihapus")


def find_contact(contacts):
    src = input("Cari Nama : ")
    for c in contacts:
        name = c['name']
        if (name.lower().find(src.lower())) != -1:
            print('Hasil pencarian')
            print(f"Nama    : {c['name']}")
            print(f"Email   : {c['email']}")
            print(f"Telepon : {c['phone']}")
