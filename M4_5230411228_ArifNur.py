debitur = []
pinjaman = []

class Debitur:
    def  __init__(self, name,KTP,LimitPinjaman):
        self.name = name
        self.__KTP = KTP
        self._LimitPinjaman = LimitPinjaman

    def get_nama(self):
        return self.name

    def set_name(self,name) :
        self.name = name

    def get_KTP(self):
        return self.__KTP

    def set_KTP(self,KTP):
        self.__KTP = KTP

    def get_LimitPinjaman(self):
        return self._LimitPinjaman

    def set_LimitPinjaman(self,LimitPinjaman) :
        self._LimitPinjaman = LimitPinjaman

class Pinjaman(Debitur):
    def __init__(self, nama, pinjaman, bunga, bulan):
        self.nama = nama
        self.pinjaman = pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran = self.Hitung_Angsuran()

    def Hitung_Angsuran(self):
        Angsuran_Pokok = self.pinjaman * self.bunga / 100
        Angsuran_Bulanan = Angsuran_Pokok / self.bulan
        return Angsuran_Pokok + Angsuran_Bulanan


debitur.append(Debitur("ArifNur", "123", 1000000))
debitur.append(Debitur("Bambang", "987", 500000))
debitur.append(Debitur("Bobi"   , "111", 2000000))
debitur.append(Debitur("Johnson", "222", 1500000))
debitur.append(Debitur("Miko"   , "333", 2500000))

def Aplikasi():
    print("=============== Aplikasi ===============")
    print("")
    print("1. Kelola Debitur")
    print("2. Pinjaman")
    print("0. Keluar")
    print("")
    

# OPSI KELOLA DEBITUR
def KelolaDebitur():
    print("=============== Kelola Debitur ===============")
    print("1. Tampilkan Semua Debitur")
    print("2. Cari Debitur")
    print("3. Tambah Debitur")
    print("------------------------------")
    print("")

#ISI OPSI KELOLA DEBITUR
def TampilDebitur() :
    print("=============== Daftar Debitur ===============")
    print("")
    print("Nama Debitur|       KTP      |Limit Pinjaman")
    print("----------------------------------------------")
    for i in debitur:
        print(f"{i.get_nama()}         {i.get_KTP()}      {i.get_LimitPinjaman()}")
      

def cari() :
    nama = input("Masukkan nama debitur: ")
    print("-------------------------------------")
    for i in debitur:
                if i.get_nama() == nama:
                    print(f"Debitur ditemukan: {i.get_nama()}")
                    print(f"KTP: {i.get_KTP()}") 
                    print(f"Limit Pinjaman: {i.get_LimitPinjaman()}")
                    break
    else:
                print("Debitur tidak ditemukan")       

def TambahDebitur():
    nama = input("Masukkan nama debitur: ")
    KTP = int(input("Masukkan KTP debitur: "))
    limit_pinjaman = int(input("Masukkan limit pinjaman debitur: "))
    for i in debitur:
                if i.get_KTP() == KTP:
                    print("Error: KTP sudah ada")
                    break
    else:
                debitur.append(Debitur(nama, KTP, limit_pinjaman))

#OPSI PINJAMAN
def MenuPinjaman():
    print("=============== Menu Pinjaman ===============")
    print("")
    print("1. Tambah Pinjaman")
    print("2. Tampilkan Pinjaman")
    print("--------------------")

def TambahPinjaman():
    nama = input("Masukkan nama debitur: ")
    pinjaman = int(input("Masukkan jumlah pinjaman: "))
    bunga = int(input("Masukkan bunga: "))
    bulan = int(input("Masukkan jangka :waktu pinjaman: "))
    for i in debitur:
                if i.get_nama() == nama:
                    if pinjaman > i.get_LimitPinjaman():
                        print("Error  Jumlah pinjaman melebihi limit")
                        break
                    else:
                        pinjaman.append(Pinjaman(nama, pinjaman, bunga, bulan))
                        break
    else:
                print("Error  Debitur tidak ditemukan")

def TampilPinjaman():
        print("Nama |       Pinjaman      |        Bunga         |        Bulan          |          Angsuran")
        print("-------------------------------------------------------------------------------------")
        for i in pinjaman:
                print(f"{i.nama}         {i.pinjaman}       {i.bunga}         {i.bulan}         {i.angsuran}")


def main():

 while True :
    Aplikasi()
    opsi = int(input("Pilih Menu :  "))
    if opsi == 1 :
       KelolaDebitur()
       opsi2 = int(input("Pilih Menu :  "))
       if opsi2 == 1 :
        TampilDebitur()
       elif opsi2 == 2 :
        cari()
       elif opsi2 == 3 :
        TambahDebitur() 
    

    elif opsi == 2 :
        MenuPinjaman()
        opsi2 = int(input("Pilih Menu : "))
        if opsi2 == 1 :
         TambahPinjaman()
        elif opsi2 == 2 :
         TampilPinjaman()    

    elif opsi == 3 :
        break

    else :  print("Pilihan Tidak Tersedia")

main()    