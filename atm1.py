saldo_umum = 0
saldo_tabungan = 0

def Informasi_Saldo():
        print("Jumlah Saldo Umum Anda Saat ini Rp. {}".format(saldo_umum))
        print("Jumlah Saldo Tabungan Anda Saat ini Rp. {}".format(saldo_tabungan))

def Ambil_Saldo_Umum(tarik_tunai):
        global saldo_umum
        saldo_umum=saldo_umum-tarik_tunai
        print("Sisa Saldo Umum anda Rp. {}".format(saldo_umum))
        print("")


def Ambil_Saldo_Tabungan(tarik_tabungan):
        global saldo_tabungan
        saldo_tabungan=saldo_tabungan-tarik_tabungan
        print("Sisa Saldo Tabungan anda Rp. {}".format(saldo_tabungan))
        print("")

    
def Saldo_Umum(tambah_umum):
        global saldo_umum
        saldo_umum=saldo_umum+tambah_umum
        print("saldo umum ada saat ini Rp. {}".format(saldo_umum))
        print("")

def Saldo_Tabungan(Tambah_Tabungan):
        global saldo_tabungan
        saldo_tabungan=saldo_tabungan+Tambah_Tabungan
        print("saldo tabungan ada saat ini Rp. {}".format(saldo_tabungan))
        print("")

opsi = None
jumlah = None
option = None
tambah_umum = None
Tambah_Tabungan = None

while True:
        print ("=== APLIKASI PENCATATAN UANG DIGITAL ===")
        print ("1. Infromasi Saldo")
        print ("2. Tambah Saldo")
        print ("3. Ambil Saldo")
        print ("4. Keluar")
        print ("========================================")
        pilih=int(input("Pilih Menu : "))
        if pilih == 1:
           Informasi_Saldo()

        elif pilih == 2:
            print("")
            print("1. Umum \n2. Tabungan")
            opsi = int(input("pilih penyimpanan:"))
            if opsi == 1:
               jumlah=int(input("Nominal Uang yang Akan Ditambahkan pada Saldo Umum Rp. "))
               Saldo_Umum(jumlah)

            else:
               jumlah=int(input("Nominal Uang yang Akan Ditambahkan pada Saldo Tabungan Rp. "))
               Saldo_Tabungan(jumlah)

        elif pilih == 3:
            print("")
            print("1. Umum \n2. Tabungan")
            option = int(input("pilih penyimpanan:"))
            if option == 1:
                print("")
                jumlah = int(input("Nominal Yang Akan Ditarik pada Saldo Umum Rp."))
                Ambil_Saldo_Umum(jumlah)

            else: 
                print("")
                jumlah = int(input("Nominal Yang Akan Ditarik pada Saldo Tabungan Rp."))
                Ambil_Saldo_Tabungan(jumlah)

        elif pilih == 4:
                print("")
                print("Terimakasih")
                print("")
        
        else:
            print("")
            print("Pilihan ada salah")
            print("")