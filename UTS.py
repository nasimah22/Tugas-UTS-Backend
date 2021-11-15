daftar_sepatu = ["Sneakers","Boots","Converse"]
daftar_sandal = ["Casual","Strappy","Velcro"]
daftar_kaoskaki = ["Ankle length","Quarter length","Knee length"]
# pada tipe data List, kita dapat mengakses data yang kita inginkan menggunakan index
keranjang = [] #Disebut juga variable global dimana untuk menyimpan data

#def merupakan Fungsi pada Python. karena dengan fungsi, kita dapat memecah 
# program besar menjadi sub program yang lebih sederhana. dan kita bisa memanggil kembali fungsi tersebut.
def pilihan_pesanan():
    print("---Daftar Pesanan---")
    print("--------------------")
    print(" 1.  |   Sepatu   | ")
    print(" 2.  |   Sandal   | ")
    print(" 3.  |   Kaoskaki | ")
    print("--------------------")
    list = int(input("Pilih pesanan anda : "))
    if list == 1:
        list_sepatu()
    elif list == 2:
        list_sandal()
    elif list == 3:
        list_kaoskaki()
    else:
        print("Pilihan pesanan tidak ditemukan") #Dimana jika untuk semua kondisi tidak ada yang terpenuhi
#if else berguna untuk mengecek kondisi yang outputnya true or false        

def list_sepatu():
    print("----Daftar Sepatu----") #Print = Perintah untuk mencetak string
    print("---------------------")
    print(" 1. | Sneakers  | 1x ")
    print(" 2. | Boots     | 1x ")
    print(" 3. | Converse  | 1x ")
    print("---------------------")
    sepatu = int(input("Pilih jenis sepatu yang ingin dipesan [1/2/3]: "))
    if sepatu == 1:
        print(" | Sneakers   | 1x")
        keranjang.append(daftar_sepatu[0]) 
    elif sepatu == 2:
        print(" | Boots      | 1x")
        keranjang.append(daftar_sepatu[1])
    elif sepatu == 3:
        print(" | Converse   | 1x")
        keranjang.append(daftar_sepatu[2])
    tambah()

def list_sandal():
    print("-----Daftar Sandal-----")
    print("-----------------    --")
    print(" 1. |    Casual   | 1x ")
    print(" 2. |    Strappy  | 1x ")
    print(" 3. |    Velcro   | 1x ")
    print("-----------------------")
    sandal = int(input("Pilih jenis sandal yang ingin dipesan [1/2/3]: "))
    if sandal == 1:
        print(" |   Casual   | 1x")
        keranjang.append(daftar_sandal[0])
    elif sandal == 2:
        print(" |   Strappy   | 1x")
        keranjang.append(daftar_sandal[1])
    elif sandal == 3:
        print(" |   Velcro   | 1x")
        keranjang.append(daftar_sandal[2])
    tambah()
    
def list_kaoskaki():
    print("-------Daftar Kaoskaki-------")
    print("-----------------------------")
    print(" 1. |   Ankle length    | 1x ")
    print(" 2. |   Quarter length  | 1x ")
    print(" 3. |   Knee length     | 1x ")
    print("-----------------------------")
    harga = int(input("Pilih jenis kaoskaki yang ingin dipesan [1/2/3]: "))
    if harga == 1:
        print(" |   Ankle length    | 1x")
        keranjang.append(daftar_kaoskaki[0])
    elif harga == 2:
        print(" |   Quarter length  | 1x")
        keranjang.append(daftar_kaoskaki[1])
    elif harga == 3:
        print(" |   Knee length     | 1x")
        keranjang.append(daftar_kaoskaki[2])
    tambah()

def selesai():
        print("--------------------------")
        print("Anda memesan : {}".format(",".join([str(pesanan) for pesanan in keranjang]))) #melakukan perulangan
        #For :untuk mengulang suatu proses yang telah diketahui jumlahnya.
        print("--------------------------")
        print("Terimakasih Pesanan anda akan segera dikirimkan")
        print()


def tambah():
    tambahan = input("Apakah ada tambahan lagi [y/n]: ")
    if tambahan == "y": #Blok main yang terdapat pada python
        pilihan_pesanan()
    elif tambahan == "n":
        selesai()
    else:
        print("Pilihan tidak ditemukan")

pilihan_pesanan()