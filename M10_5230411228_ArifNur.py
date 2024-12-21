import mysql.connector

conn = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = '',
    database = 'penjualan'
)

cur = conn.cursor()
# cur.execute("CREATE DATABASE Penjualan")

# Membuat Table Baran Pegawai
# cur.execute("""CREATE TABLE Pegawai (
#              NIK CHAR(5) NOT NULL PRIMARY KEY,
#              Nama VARCHAR(50),
#              Alamat VARCHAR(255)
#              )""")

# # Membuat Table Transaksi
# cur.execute("""CREATE TABLE Transaksi (
#             No_Transaksi VARCHAR(255),
#             Detail_Transaksi VARCHAR(255)
#             )""")

# # Membuat Table Struk
# cur.execute("""CREATE TABLE Struk (
#             No_Transaksi VARCHAR(255),
#             Nama VARCHAR(50),
#             Nama_Produk VARCHAR(255),
#             Jumlah_Produk VARCHAR(255),
#             Total_Harga VARCHAR(255)
#             )""")

# # Membuat Table Produk
# cur.execute("""CREATE TABLE Produk (
#             Kode_Produk CHAR(5) NOT NULL PRIMARY KEY,
#             Nama_Produk VARCHAR(255),
#             Jenis_Produk VARCHAR(255),
#              Harga VARCHAR(255)
#             )""")

# # Membuat Table Snack
# cur.execute("""CREATE TABLE Snack (
#             Nama_Snack CHAR(255),
#             Harga VARCHAR(255),
#             )""")


# # Membuat Table Minuman
# cur.execute("""CREATE TABLE Minuman (
#             Nama_Minuman CHAR(255),
#             Harga VARCHAR(255),
#             )""")


# # Membuat Table Makanan
# cur.execute("""CREATE TABLE Makanan (
#             Nama_Makanan CHAR(255),
#             Harga VARCHAR(255),
#             )""")








#Add Foreign Keys
cur.execute("""ALTER TABLE transaksi
            ADD FOREIGN KEY (No_Transaksi)
            REFERENCES struk(No_Transaksi)""")

cur.execute("""ALTER TABLE struk
            ADD FOREIGN KEY (No_Transaksi)
            REFERENCES transaksi(No_Transaksi)""")

cur.execute("""ALTER TABLE struk
            ADD FOREIGN KEY (Nama)
            REFERENCES pegawai(Nama)""")

cur.execute("""ALTER TABLE struk
            ADD FOREIGN KEY (Nama_Produk)
            REFERENCES Produk(Nama_Produk)""")

