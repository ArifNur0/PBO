jepang = []
korea = []
inggris = []

# 
class Music :
    def __init__(self, Judul, Penyanyi, Genre):
        self.Judul = Judul
        self.Penyanyi = Penyanyi
        self.Genre = Genre

class JapaneseSong(Music):
    def __init__(self, Judul, Penyanyi, Genre):
        super().__init__(Judul, Penyanyi, Genre)

    def Add() :
        global jepang
        Judul = input("Masukkan Judul Music: ")
        Penyanyi = (input("Masukkan Nama penyanyi : "))
        Genre = (input("Masukkan Genre  Music : "))
        jepang.append(JapaneseSong(Judul,Penyanyi,Genre))

    def Delete() :
        global jepang
        if len(jepang) > 0 :
            del jepang[-1]

class KoreanSong(Music):
    def __init__(self, Judul, Penyanyi, Genre):
        super().__init__(Judul, Penyanyi, Genre)

    def Add():
        global korea
        Judul = input("Masukkan Judul Music: ")
        Penyanyi = (input("Masukkan Nama penyanyi : "))
        Genre = (input("Masukkan Genre  Music : "))
        korea.append(KoreanSong(Judul,Penyanyi,Genre))

    def Delete():
        global korea
        if len(korea) > 0 :
            del korea[-1]

class EnglishSong(Music):
    def __init__(self, Judul, Penyanyi, Genre):
        super().__init__(Judul, Penyanyi, Genre)

    def Add():
        global inggris
        Judul = input("Masukkan Judul Music: ")
        Penyanyi = (input("Masukkan Nama penyanyi : "))
        Genre = (input("Masukkan Genre  Music : "))
        inggris.append(EnglishSong(Judul,Penyanyi,Genre))


    def Delete():
        global inggris
        if len(inggris) > 0 :
            del inggris[-1]

jepang.append(JapaneseSong("Sparkle           ", "Radwimps      ", "J-Song"))
jepang.append(JapaneseSong("Suzume            ", "Radwimps      ", "J-Song"))
jepang.append(JapaneseSong("Kick Back         ", "Kenshi Yonezu ", "J-Song"))
jepang.append(JapaneseSong("Musica            ", "Brandy Senki  ", "J-Song"))
jepang.append(JapaneseSong("Idol              ", "Yoasobi      ", "J-Song"))

korea.append(KoreanSong("Why Why          ", "Shanon Williams", "K-Song"))
korea.append(KoreanSong("UP               ", "Karina        ", "K-Song"))
korea.append(KoreanSong("I AM             ", "IVE           ", "K-Song"))
korea.append(KoreanSong("Supernova        ", "AESPA         ", "K-Song"))
korea.append(KoreanSong("Supershy         ", "NewJeans      ", "K-Song"))

inggris.append(EnglishSong("Cradles            ", "Sub Urban       ", "E-Song"))
inggris.append(EnglishSong("The Cigarrete Duet ", "Princess Chelsea", "E-Song"))
inggris.append(EnglishSong("Forever Young      ", "Aplhaville      ", "E-Song"))
inggris.append(EnglishSong("Judas              ", "Lady Gaga       ", "E-Song"))
inggris.append(EnglishSong("Impossible         ", "James Arthur    ", "E-Song"))

def CariPenyanyi():
    global jepang, korea, inggris
    penyanyi = input("Masukkan nama penyanyi: ")
    for i in range(len(jepang)):
        if penyanyi in jepang[i].Penyanyi:
            print("Judul                          Penyanyi              Genre")
            print("------------------------------------------------")
            print(f"{jepang[i].Judul}  {jepang[i].Penyanyi}  {jepang[i].Genre}")
            print("\n")
    for i in range(len(korea)):
        if penyanyi in korea[i].Penyanyi:
            print("Judul                      Penyanyi              Genre")
            print("------------------------------------------------")
            print(f"{korea[i].Judul}  {korea[i].Penyanyi}  {korea[i].Genre}")
            print("\n")
    for i in range(len(inggris)):
        if penyanyi in inggris[i].Penyanyi:
            print("Judul                        Penyanyi              Genre")
            print("------------------------------------------------")
            print(f"{inggris[i].Judul}  {inggris[i].Penyanyi}  {inggris[i].Genre}")
                
def TampilUrut() :
    global jepang, korea, inggris
    print("Judul                          Penyanyi              Genre")
    print("------------------------------------------------")
    for i in range(len(jepang)):
        print(f"{jepang[i].Judul}  {jepang[i].Penyanyi}  {jepang[i].Genre}")
    for i in range(len(korea)):
        print(f"{korea[i].Judul}  {korea[i].Penyanyi}  {korea[i].Genre}")
    for i in range(len(inggris)):
        print(f"{inggris[i].Judul}  {inggris[i].Penyanyi}  {inggris[i].Genre}")

def HapusMusic():
    global jepang, korea, inggris
    judul = input("Masukkan judul lagu yang ingin dihapus: ")
    for i in range(len(jepang)):
        if judul in jepang[i].Judul:
            del jepang[i]
    for i in range(len(korea)):
        if judul in korea[i].Judul:
            del korea[i]        
    for i in range(len(inggris)):
        if judul in inggris[i].Judul:
            del inggris[i]


def main():
   while True: 
    print("==== ==== ==== PlayList Music ==== ==== ====")
    print("1. Japanese Song ")
    print("2. Korean Song ")
    print("3. English Song ")
    print("4. Display Song List ")
    print("5. Search Song ")
    print("6. Exit ")
    pilih = int(input("Masukkan Pilihan Anda : "))
    if pilih == 1 :
        print("==== ==== ==== Japanese Song ==== ==== ====")
        print("1. Add Song ")
        print("2. Delete Song ")
        print("3. Display Song List")
        print("4. Kembali")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1 :
            global jepang
            Judul = input("Masukkan Judul Music: ")
            Penyanyi = (input("Masukkan Nama penyanyi : "))
            Genre = (input("Masukkan Genre  Music : "))
            jepang.append(JapaneseSong(Judul,Penyanyi,Genre))

        elif pilih == 2 :
            HapusMusic()

        elif pilih == 3 :
            print("==== ==== ==== Japanese Song ==== ==== ====")
            print("Judul               |           Penyanyi          |     Genre")
            print("------------------------------------------------")
            for i in range(len(jepang)):
                print(f"{jepang[i].Judul}           {jepang[i].Penyanyi}            {jepang[i].Genre}")

    elif pilih == 2 :
        print("==== ==== ==== Korean Song ==== ==== ====")
        print("1. Add Song ")
        print("2. Delete Song ")
        print("3. Display Song List")
        print("4. Kembali")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1 :
            global korea
            Judul = input("Masukkan Judul Music: ")
            Penyanyi = (input("Masukkan Nama penyanyi : "))
            Genre = (input("Masukkan Genre  Music : "))
            korea.append(KoreanSong(Judul,Penyanyi,Genre))

        elif  pilih == 2 :
            HapusMusic()

        elif pilih == 3 :
            print("==== ==== ==== Korean Song ==== ==== ====")
            print("Judul               |           Penyanyi          |     Genre")
            print("------------------------------------------------")
            for i in range(len(korea)):
                print(f"{korea[i].Judul}            {korea[i].Penyanyi}             {korea[i].Genre}")

    elif pilih == 3 :
        print("==== ==== ==== English Song ==== ==== ====")
        print("1. Add Song ")
        print("2. Delete Song ")
        print("3. Display Song List")
        print("4. Kembali")
        pilih = int(input("Masukkan Pilihan Anda : "))
        if pilih == 1 :
            global inggris
            Judul = input("Masukkan Judul Music: ")
            Penyanyi = (input("Masukkan Nama penyanyi : "))
            Genre = (input("Masukkan Genre  Music : "))
            inggris.append(EnglishSong(Judul,Penyanyi,Genre))


        elif pilih == 2 :
            HapusMusic()

        elif pilih == 3 :
            print("==== ==== ==== English Song ==== ==== ====")
            print("Judul               |           Penyanyi          |     Genre")
            print("------------------------------------------------")
            for i in range(len(inggris)):
                print(f"{inggris[i].Judul}          {inggris[i].Penyanyi}           {inggris[i].Genre}")
       

    elif pilih == 4 :
        TampilUrut()
        # print("==== ==== ==== Display Song List ==== ==== ====")
        # print("Judul               |           Penyanyi          |     Genre")
        # print("------------------------------------------------")
        # for i in range(len(jepang)):
        #     print(f"{jepang[i].Judul}           {jepang[i].Penyanyi}            {jepang[i].Genre}")
        # for i in range(len(korea)):
        #     print(f"{korea[i].Judul}            {korea[i].Penyanyi}             {korea[i].Genre}")
        # for i in range(len(inggris)):
        #     print(f"{inggris[i].Judul}          {inggris[i].Penyanyi}           {inggris[i].Genre}")
                


    elif pilih == 5 :
        CariPenyanyi()

    elif pilih == 6 :
        break
    else : 
        print("Maaf , Pilihan Anda Tidak Ada Dalam Menu")




main()
