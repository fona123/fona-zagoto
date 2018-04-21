from hitung.texttable import Texttable

def penilaian():
    print('===================================================================================')
    jawab = "y"
    table = Texttable()
    no = 0
    nama = []
    nim = []
    n_tugas = []
    n_uts = []
    n_uas = []
    while (jawab == "y"):
        nama.append(input("Nama :"))
        nim.append(input("Nim :"))
        n_tugas.append(input("Nilai Tugas :"))
        n_uts.append(input("Nilai UTS :"))
        n_uas.append(input("Nilai UAS :"))
        jawab = input("Tambah data (y/t)?")
        no += 1
    for n in range(no):
        akhir = (float(n_tugas[n]) * 30 / 100) + (float(n_uts[n]) * 35 / 100) + (float(n_uas[n]) * 35 / 100)
        table.add_rows([['No', 'Nama', 'Nim', 'Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                        [n + 1, nama[n], nim[n], n_tugas[n], n_uts[n], n_uas[n], akhir]])
    table.set_chars(['=', '|', '=', '='])
    print(table.draw())