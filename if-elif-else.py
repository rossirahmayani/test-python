crewmate = 2
imposter = 2

print("You are crewmate!")
if imposter == 0:
    print("Victory")
if crewmate <= imposter:
    print("Defeated")


win = False
if win == True :
    print("Selamat")
else :
    print("Coba lagi")


blood_type = input('Masukkan golongan darah anda: ')
note = ''
if blood_type == 'A':
    note = "Darah anda dapat didonorkan ke golongan darah A dan AB"
elif blood_type == 'B':
    note = "Darah anda dapat didonorkan ke golongan darah B dan AB"
elif blood_type == 'O':
    note = "Darah anda dapat didonorkan ke golongan darah A, B, O, dan AB"
elif blood_type == 'AB':
    note = "Darah anda dapat didonorkan ke golongan darah AB"
else:
    note = "Masukkan golongan darah yang benar!!!"
    
print("Hasil: " + note)