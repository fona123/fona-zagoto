
def spp():
    bulan = int(input('jumlah bulan yang akan di bayar :'))
    jumlah = 550000 * bulan
    print('spp yang akan di bayar {} \n + biaya server 5000 \n total yang harus dibayar {}'.format(jumlah, jumlah + 5000))

def uas_uts():
    mat = int(input('jumlah matakuliah yang akan di bayar :'))
    jumlah = 50000 * mat
    print('biaya yang akan dibayar {}\n+ biaya server 5000\n total yang harus dibayar {}'.format(jumlah, jumlah + 5000))

def sppdan():
    bulan =int(input('jummlah bulan yang akan dibayar :'))
    mat = int(input('jummlah matakuliah yang akan dibayar :'))
    jubulan = bulan * 550000
    jumat = mat *50000
    ser = 5000
    print('spp yang dibayar {}\nujian yang dibayar {}\n biaya server {} total yang harus dibayar {}'.format(jubulan, jumat, ser, jubulan + jumat +ser))



def pembayaran():
    print('==============================================\n\t---pilihan pembayaran---')
    print('\t1. spp\n\t2. uts \n\t3. uas \n\t4. spp dan uts\n\t5. spp dan uas')
    pilih = input('pilih :')
    if(pilih == '1'):
        spp()
    elif(pilih == '2'):
        uas_uts()
    elif(pilih == '3'):
        uas_uts()
    elif(pilih == '4'):
        sppdan()
    elif(pilih == '5'):
        sppdan()
    else:
        print('input salah')
    print('==============================================')
