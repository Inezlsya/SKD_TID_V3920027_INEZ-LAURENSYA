# Digunakan untuk mengambil esbuah inputan
key = input("Masukkan Key : ")
# Digunakan untuk menganti key
key = key.replace(" ", "")
# Digunakan untuk membuat text menjadi huruf kapital
key = key.upper()

# Digunakan untuk membuat sebuah fungsi matrix


def matrix(x, y, initial):
    # Digunakan untuk menjalankan ulang perulangan
    return [[initial for i in range(x)] for j in range(y)]


# Digunakan untuk pendeklarasian list dari matrix
result = list()
# Digunakan untuk melakukan perulangan c sebagai pemisalan nilai huruf didalam pada key
for c in key:  # storing key
    # Percabangan jika c tidak ada didalam list maka akan menjalankan program
    if c not in result:
        # Jika nilai c benar maka akan dirubah menjadi i
        if c == 'J':
            # Digunakan untuk menggantikan nilai j
            result.append('I')
        # Jika c bukan j maka akan menjalankan
        else:
            # Digunakan untuk tetap menggunakan huruf aslinya
            result.append(c)
# Pendeklarasian flag jika tidak terjadi
flag = 0
# Digunakan untuk melakukan perulangan i sebagai pemisalan nilai huruf didalam range yang ada untuk menyortir karakter
for i in range(65, 91):
    # Percabangan jika i tidak ada didalam list maka akan menjalankan program
    if chr(i) not in result:
        # Percabangan jika i == adalah karakter ke 73 dan karakter 74 tidak ada didalam list maka akan menjalankan program
        if i == 73 and chr(74) not in result:
            # Digunakan untuk menggantikan nilai i
            result.append("I")
            # Pendeklarasian flag jika terjadi atau ada
            flag = 1
        # Percabangan jika flag tidak ada dan i == adalah karakter ke 73 atau i == adalah karakter 74 maka akan menjalankan program
        elif flag == 0 and i == 73 or i == 74:
            # Menyatakan tidak ada statement
            pass
        # Jika salah maka akan menjalan kan program didalamnya
        else:
            # Digunakan untuk menggantikan menjadi karakter yang sama
            result.append(chr(i))
# Pendeklarasian k bernilai 0 atau kosong
k = 0
# Penginialisasian matriks yang digunakan
my_matrix = matrix(5, 5, 0)
# Digunakan untuk membuat matriks dengan range yang ada
for i in range(0, 5):
    # Digunakan untuk perulangan nilai j pada metriks dengan range yang ada
    for j in range(0, 5):
        # Pernyataan nilai matriks menjadi isi dari k
        my_matrix[i][j] = result[k]
        # Pernyataan jika nilai k sudah ditambahkan
        k += 1

# Digunakan untuk membuat fungsi locindex yang digunakan untuk mencari lokasi index karakter


def locindex(c):
    # Pendeklarasian bahwa loc berisikan list
    loc = list()
    # Percabangan jika nilai c(karakter) sama dengan j maka akan diganti menjadi i
    if c == 'J':
        # Pendeklarasian nilai c(karakter) menjadi huruf i
        c = 'I'
    # Perulangan i dan j untuk mencari lokasi didalam matriks
    for i, j in enumerate(my_matrix):
        # Perulangan j dan l untuk mencari lokasi didalam matriks yang sudah tidak aja huruf j
        for k, l in enumerate(j):
            # Percabangan jika nilai c == i maka akan menjalankan program didalamnya
            if c == l:
                # Digunakan untuk menggantikan karakter pada loc menjadi i
                loc.append(i)
                # Digunakan untuk menggantikan karakter pada loc menjadi k
                loc.append(k)
                # Digunakan untuk menjalankan kembali loc
                return loc


# Digunakan untuk membuat fungsi enkripsi


def enkripsi():
    # Digunakan untuk mengambil inputan yang berjenis string
    msg = str(input("Masukkan Plain Text : "))
    # Digunakan untuk mengubah inputan menjadi huruf besar/kapital
    msg = msg.upper()
    # Digunakan untuk mengubah nilai inputan
    msg = msg.replace(" ", "")
    # Digunakan untuk pendeklarasian nilai karakter i sama dengan 0 atau kosong
    i = 0
    # Perulangan nilai karakter s didalam range yang bernilai range batas letak urutan karakter ditambah 1
    for s in range(0, len(msg)+1, 2):
        # Percabangan jika karakter s kurang dari letak huruf -1 maka akan menjalanka program didalamnya
        if s < len(msg)-1:
            # Percabangan jika nilai karakter s == karakter ditambahkan satu langkah akan menjalankan program dibawah ini
            if msg[s] == msg[s+1]:
                # Pernyataan nilai inputan jika karakter memiliki lebih dari satu maka akan ditambahkan 1 dan x
                msg = msg[:s+1]+'X'+msg[s+1:]
    # Percabangan jika urutan karakter dibagi 2 tidak habis dibagi 0 maka akan menjalankan program didalamnya
    if len(msg) % 2 != 0:
        # Pernyataan nilai inputan akan ditambahkan karakter x
        msg = msg[:]+'X'
    # Digunakan untuk mencetak hasil enkripsi
    print("Hasil Cipher Text : ", end=' ')
    # Digunakan untuk melooping i jika kurang dari lokasi panjang karakter
    while i < len(msg):
        # Pendeklarasian loc sama dengan list
        loc = list()
        # pendeklarasian loc sama dengan locindex dengan lokasi karakter
        loc = locindex(msg[i])
        # Pendeklarasian loc1 sama dengan list
        loc1 = list()
        # pendeklarasian loc1 sama dengan locindex dengan lokasi karakter ditambah 1
        loc1 = locindex(msg[i+1])
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang sama maka
        if loc[1] == loc1[1]:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(
                my_matrix[(loc[0]+1) % 5][loc[1]], my_matrix[(loc1[0]+1) % 5][loc1[1]]), end=' ')
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang sama maka
        elif loc[0] == loc1[0]:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(my_matrix[loc[0]][(
                loc[1]+1) % 5], my_matrix[loc1[0]][(loc1[1]+1) % 5]), end=' ')
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang tidak sama maka
        else:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(
                my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        # Pendeklarasian karakter i ditambahkan dengan 2
        i = i+2


# Digunakan untuk membuat fungsi dekripsi
def dekripsi():
    # Digunakan untuk mengambil inputan yang berjenis string
    msg = str(input("Masukkan Cipher Text : "))
    # Digunakan untuk mengubah inputan menjadi huruf besar/kapital
    msg = msg.upper()
    # Digunakan untuk mengubah nilai inputan
    msg = msg.replace(" ", "")
    # Digunakan untuk pendeklarasian nilai karakter i sama dengan 0 atau kosong
    print("Hasil Plain Text : ", end=' ')
    # Digunakan untuk pendeklarasian nilai karakter i sama dengan 0 atau kosong
    i = 0
    # Digunakan untuk melooping i jika kurang dari lokasi panjang karakter
    while i < len(msg):
        # Pendeklarasian loc sama dengan list
        loc = list()
        # pendeklarasian loc sama dengan locindex dengan lokasi karakter
        loc = locindex(msg[i])
        # Pendeklarasian loc1 sama dengan list
        loc1 = list()
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang sama maka
        loc1 = locindex(msg[i+1])
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang sama maka
        if loc[1] == loc1[1]:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(
                my_matrix[(loc[0]-1) % 5][loc[1]], my_matrix[(loc1[0]-1) % 5][loc1[1]]), end=' ')
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang sama maka
        elif loc[0] == loc1[0]:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(my_matrix[loc[0]][(
                loc[1]-1) % 5], my_matrix[loc1[0]][(loc1[1]-1) % 5]), end=' ')
        # Percabangan jika terdapat loc dan loc1 memiliki nilai yang tidak sama maka
        else:
            # Digunakan untuk mencetak hasil dari perhitungan matemarika pada matriks
            print("{}{}".format(
                my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        # Pendeklarasian karakter i ditambahkan dengan 2
        i = i+2


# Digunakan untuk melakukan perulangan menu
while(1):
    # Digunakan untuk mencetak pilihan menu
    print("\n \n 1. Enkripsi \n 2. Dekripsi \n 3. Keluar \n")
    # Digunakan untuk menginputkan pilihan menu
    choice = int(input("Masukkan Pilihan : "))
    # Percabangan jika memilih 1 maka akan menjalankan program didalamnya
    if choice == 1:
        # Digunakan untuk menjalankan fungsi enkripsi
        enkripsi()
    # Percabangan jika memilih 2 maka akan menjalankan program didalamnya
    elif choice == 2:
        # Digunakan untuk menjalankan fungsi dekripsi
        dekripsi()
    # Percabangan jika memilih 3 maka akan menjalankan program didalamnya
    elif choice == 3:
        # Digunakan untuk mengakhiri program
        exit()
    # Percabangan jika memilih 1 maka akan menjalankan program didalamnya
    else:
        # Digunakan untuk mencetak tulisan peringatan
        print("Tolong Pilih Menu Dengan Benar")
        print()
