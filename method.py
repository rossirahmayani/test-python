nama = []

#deklarasi nama method
def print_nama(): #sebelum dipanggil methd harus dibuat dulu
    print("-------------")
    for n in nama:
        print(n)


nama.append('Spongebob')
print_nama() #panggil method

nama.append('Patrick')
print_nama()


#method dgn param
def hello(name):
    print(f"Hello {name}")

hello("Squidward")
hello("Gary")


#with default value
def add(a=0,b=0): #urutan default value --> non default dulu baru default
    hasil = a + b
    print(f"{a} + {b} = {hasil}")


add(1,2)
add(1)
add()
add(b=2) #kalo mau bolak balik sebutin variabel param nya
add(b=2, a=4)


#argument list
def multiply(awal, *list_angka): #kalo mau banyak param, argument list jd param terakhir dan cm bisa 1
    total = awal
    for angka in list_angka:
        total = total * angka
    return (awal, list_angka, total)        #balikin nilai



awal, list_angka, hasil = multiply(1,2,3,4,5)
print(f'Total {awal} dikali dengan {list_angka} = {hasil}')

awal, list_angka, hasil = multiply(2,4,6,8)
print(f'Total {awal} dikali dengan {list_angka} = {hasil}')

