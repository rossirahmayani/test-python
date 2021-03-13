# input data
print("Masukkan nama anda: ")
nama = input() # tipe data string

print(f"Hello {nama}, selamat datang di Indomaret")


# input number
print("Nama barang: ")
barang = input()


print("Harga: ")
harga = int(input())

print("Jumlah: ")
jumlah = int(input())

total = harga * jumlah
print(f"{barang} :   {harga} x {jumlah} = {total}")
