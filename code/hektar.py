import pandas as pd
import os
import termcolor

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


tampungan_input = []
# rumus hektar
def hitung():
    while True:
        clear()
        masukan = int(input('Masukan hektar (angka) : '))
        hektar = (masukan*(10000))
        tampungan_input.append(masukan)

        print("""
        - - - - - - - - - - - - - - - - - - -
        | Anjuran jarak taman 20x20 per tancap |
        - - - - - - - - - - - - - - - - - - -
        """)

        masukan2 = int(input("Masukan jarak cm (angka): "))
        jarak = ((hektar/masukan2)*(hektar/masukan2))
        hasil = jarak
        tampungan_input.append(masukan2)
        print()

        # print(int(hasil))

        masukan3 = int(input("Masukan bibit per tancap (angka): "))
        tancap = (hasil*masukan3)
        tampungan_input.append(masukan3)
        print()
        # print(int(tancap))

        akhir = float(((tancap/1000)*27)*(1/1000))
        akhir2 = (akhir)*(15/100)
        akhir3 = int(akhir + akhir2)
        print('kebutuhan benih tanam tumbuh 100%''adalah',(akhir),'per kg\n')
        print('kebutuhan benih tanam tumbuh 85%" + hama 15%''adalah',(akhir3),'per kg\n')
        validasi = input('apakah lahan yang diinputkan sudah sesuai? [Y/T] : ')
        if validasi == "T" or validasi == "t":
            tampungan_input.clear()
            print()
            continue
        elif validasi == "Y" or validasi == "y":
            print()
            break
        else:
            tampungan_input.clear()
            print("Maaf kami tidak dapat memproses!")
            continue

# resume sementara
    print('- - - - '*8)
    print("| yang dibutuhkan  / ha     : ",tampungan_input[0]," "*29,"|")
    print("| jarak (cm) tanam / tancap : ",tampungan_input[1]," "*28,"|")
    print("| jumlah bibit     / tanam  : ",tampungan_input[2]," "*29,"|")
    print('- - - - '*8)
    print('| kebutuhan benih tanam tumbuh 100%''adalah',(akhir),'per kg'," "*7,"|")
    print('| kebutuhan benih tanam tumbuh 85%" + hama 15%''adalah',(akhir3),'per kg',"|")
    print('- - - - '*8)

hitung()

# resume = ("butuh bibit per jarak: "+str(masukan),str(hasil),"bibit per tancap : ", str(tancap))
# print(resume)
