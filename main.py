from hitung.penilaian import *
from hitung.pembayaran import *
from hitung.calculator import *
import getpass
username = 'fona'
password = '12345678'



def menu():
    print("=================================================================")
    print("\n\t---pilihan---\n\t1. penilaian mahasiswa\n\t2. pembayaran mahasiswa\n\t3. calculator")
    pilih = input("\tsilahkan pilih :")
    if (pilih == '1'):
        penilaian()
    elif(pilih == '2'):
        pembayaran()
    elif(pilih == '3'):
        calculator()
    else:
        exit()
    tanya()

def tanya():
    tanyain = input('kembali ke menu [Y/N]')
    if(tanyain == 'y' or 'Y'):
        menu()
    else:
        exit()

us = input('username :')
ps = getpass._raw_input('password :')

if(us == username and ps == password):
    menu()
else:
    exit()
