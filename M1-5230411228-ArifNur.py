def main():
    while True:
        phi = 3.14
        r = int(input("Masukkan panjang jari-jari  :"))
        t = int(input("Masukkan tinggi tabung :"))
        print("-------operasi-------  ")
        print("1.Hitung Volume")
        print("2.Hitung Luas permukaan")
        operasi = int(input("Pilih operasi :"))
        if operasi == 1 :
            Volume = phi * (r*r) * t
            print("Volume tabung = ", Volume)
            print("------------------------")
            print("------------------------")

        elif operasi == 2 :
            Lp = 2 * phi * r *(r + t)
            print("Luas Permukaan tabung = ", Lp)    
            print("------------------------")
            print("------------------------")


main()
