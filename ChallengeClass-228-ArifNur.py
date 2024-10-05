#buatlah class DaftarMenu
#Menampilkan daftar menu makanan
#menampilkan daftar menu minuman
#menambahkan menu makanan dan minuman

# Arif Nur Rahman 
# NPM 5230411228

class DaftarMenu:
    def __init__(self,Makanan,Minuman,Harga):
        self.Makanan = Makanan
        self.Minuman = Minuman
        self.Harga = Harga

    
    def MenuMakanan(self,Makanan,Harga) :
        print("Makanan :{self.Makanan} --- {self.Harga}")
    def MenuMinuman(self,Minuman,Harga ) :
        print("Minuman :{self.Minuman} --- {self.Harga}")
 

while True :
            List_Makanan  = [
                    ("Nasi Goreng", 15000),
                    ("Mie Goreng ", 10000),
                    ("Gado-Gado  ", 8000),
                    ("Sate       ",10000 ),
                    ("Bakso      ",12000 )
                    ]
            List_Minuman = [
                    ("Jus Jeruk", 5000 ),
                    ("Jus Apel ", 5000 ),
                    ("Jus Melon", 5000 ),
                    ("Es Teh   ", 3000 ),
                    ("Es Kopi  ", 3000 )
            ]
            print("===Daftar Pilihan===")
            print("1. Lihat  Menu Makanan")
            print("2. Lihat Menu Minuman")
            print("3. Tambah Menu")
            print("4. Keluar")

            opsi = int(input("Masukkan  Pilihan Anda : "))

            if opsi == 1 :
                print("===Daftar Menu Makanan===")    
                for i in range(len(List_Makanan)):
                    print(f"{i+1}. {List_Makanan[i][0]} --- {List_Makanan[i][1]}")
                print("---------------------")       
                    

            elif opsi == 2 : 
                print("===Daftar Menu Minuman===")
                for i in range(len(List_Minuman)):
                    print(f"{i+1}. {List_Minuman[i][0]} --- {List_Minuman[i][1]}")
                print("---------------------")

            elif opsi == 3 :
                print("===Tambah Menu===")
                print("1.Tambah Menu Makanan")
                print("2.Tambah Menu Minuman")
                opsi2 = int(input("Masukkan Pilihan Anda : "))
                if opsi2 == 1 :
                    Jumlah_Tambahan = int(input("Masukkan Jumlah  :"))
                    for i in range(Jumlah_Tambahan) :
                        Makanan = input("Masukkan Nama Makanan :")
                        Harga = int(input("Masukkan Harga :"))
                        List_Makanan.append((Makanan,Harga))
                        print(f"{Makanan} Berhasil Ditambahkan")
                        print("===Daftar Menu Makanan===")    
                        for i in range(len(List_Makanan)):
                            print(f"{i+1}. {List_Makanan[i][0]} --- {List_Makanan[i][1]}")
                            print("---------------------")
                elif opsi2 == 2:
                    Jumlah_Tambahan = int(input("Masukkan Jumlah  :"))
                    for i in range(Jumlah_Tambahan):
                        Minuman = input("Masukkan Nama Minuman :")
                        Harga = int(input("Masukkan Harga :"))
                        List_Minuman.append((Minuman,Harga))
                        print(f"{Minuman} Berhasil Ditambahkan")
                        print("===Daftar Menu Minuman===")
                        for i in range(len(List_Minuman)):
                            print(f"{i+1}. {List_Minuman[i][0]} --- {List_Minuman[i][1]}")
                        print("---------------------")
                            


    
            





