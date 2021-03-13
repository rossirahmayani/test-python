# while loop
num = 3
count = 0
while num > 0:
    count = count + 1
    print(f"masuk perulangan ke: {count} ")
    num = num - 1


# for loop
nama = ["Maya", "Claudine", "Nana", "Kaoruko", "Futaba", "Mahiru", "Junna", "Hikari", "Karen"]

print("Papa Kirin memanggil: ")
print("======================")
for n in nama:
    print(f" * | {n}            ")
    print("----------------------")


# range
nomor = range(1, 6) #[1,2,3,4,5]
for no in nomor:
    print(no)


# continue
for i in range(1, 20):
    if i % 2 == 0:
        continue    # skip looping
    print(i)

# break
for i in range(1, 20):
    if i == 5:
        print("break")
        break       # stop looping

    print(i)


nama = []
umur = []
banyak = int(input("Berapa banyak data? "))
for i in range(0, banyak):
    print(f"Data ke {i}")
    input_nama = input("Nama: ")
    input_umur = input("Umur: ")
    nama.append(input_nama)
    umur.append(input_umur)

for i in range(0, len(nama)):
    print(f"{nama[i]} berumur {umur[i]} tahun")




