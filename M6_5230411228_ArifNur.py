class Order:
    def __init__(self, ID, name, detail):
        self._ID = ID
        self.name = name
        self.detail = detail

    def SetOrder(self, ID=None, name=None, detail=None):
        if ID is not None:
            self._ID = ID
        if name is not None:
            self.name = name
        if detail is not None:
            self.detail = detail

    def GetOrderDetails(self):
        return {
            "ID": self._ID,
            "Name": self.name,
            "Detail": self.detail
        }
    def display(self):
        print(f"ID: {self._ID}")
        print(f"Name: {self.name}")
        print(f" Detail: {self.detail}")


class Delivery:
    def __init__(self, id, name, information, date, address):
        self.id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

    def ProcessDelivery(self):
        return f"Processing delivery for {self.name} to {self.address} on {self.date}."

    def GetDeliveryDetails(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Information": self.information,
            "Date": self.date,
            "Address": self.address
        }

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f" Information: {self.information}")
        print(f" Date: {self.date}")
        print(f" Address: {self.address}")

def main():
    print(" =    =    =    = Daftar =    =    =    = ")
    print("1 . Pesan ")
    print("2 . Keluar ")
    pilih = int(input("Masukkan Pilihan  : "))
    if pilih == 1:
        nama = input("Masukkan Nama  :")
        tgl = input("Masukkan Tanggal  :")
        alamat = input("Masukkan Alamat :")
        sk = Delivery(id,nama,info,tgl,alamat)
        print(" =    =    =    = Pesan =    =    =    = ")
        print("1 . Bakso       - Rp10000")
        print("2 . Sate        - Rp15000")
        print("3 . Lontong     - Rp8000")
        print("4 . Es Teler    - Rp5000")
        print("5 . Es Campur   - Rp10000")
        pilih = int(input("Masukkan Pilihan   :"))
        if pilih == 1:
            jml = int(input("Masukkan  Jumlah :"))
            info = input("Masukkan Detail Pesanan :")
            print(f" Total Bayar : {jml * 10000}")
            sk.display

        elif pilih == 2:
            jml = int(input("Masukkan  Jumlah :"))
            info = input("Masukkan Detail Pesanan :")
            print(f" Total Bayar : {jml * 15000}")
            sk.display

        elif pilih == 3:
            jml = int(input("Masukkan  Jumlah :"))
            info = input("Masukkan Detail Pesanan :")
            print(f" Total Bayar : {jml * 8000}")
            sk.display

        elif pilih == 4:
            jml = int(input("Masukkan  Jumlah :"))
            info = input("Masukkan Detail Pesanan :")
            print(f" Total Bayar : {jml * 5000}")
            sk.display

        elif pilih == 5:
            jml = int(input("Masukkan  Jumlah :"))
            info = input("Masukkan Detail Pesanan :")
            print(f" Total Bayar : {jml * 10000}")
            sk.display

        else:
            print("Pilihan Tidak Tersedia")

main()










