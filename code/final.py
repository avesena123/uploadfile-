# - - - - - Login serius jadi - - - - -
import termcolor
import getpass
import hashlib #enkripsi password
import os
import time
import hektar

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def admin():
    clear()
    termcolor.cprint("--- Silakan Login ---","magenta")
    admin = input(termcolor.colored("username : ","magenta"))
    validasi2 = False

    with open("admin_database.txt") as baca:
        for line in baca:
            xadmin,xpasswordadmin,xid= line.split(",")
            if admin in xadmin:
                ulang = 1
                while ulang <= 3:
                    password = getpass.getpass(termcolor.colored("password : ", "blue"))
                    if password in xpasswordadmin:
                        for i in range(3):
                            termcolor.cprint("*","red", end="", flush=True)
                            time.sleep(0.1)
                        clear()
                        termcolor.cprint("> Halo gan!","magenta")
                        validasi2 = True
                        break
                    else:
                        termcolor.cprint(f"password salah! {ulang}x","red")
                        ulang += 1
    return validasi2


def login():
    clear()
    termcolor.cprint("--- Silakan login ---","magenta")
    user = input(termcolor.colored("username : ","blue"))
    validasi1 = False

    with open("login_database.txt","r") as baca:
        for line in baca:
            xuser,xpassword,xid= line.split(",")
            if user == xuser:
                ulang = 1
                while ulang <= 3:
                    password = getpass.getpass(termcolor.colored("password : ","blue"))
                    password = password.encode("ascii")
                    password = hashlib.md5(password).hexdigest()
                    if password == xpassword:
                        for i in range(3):
                            termcolor.cprint("*","red", end="", flush=True)
                            time.sleep(0.1)
                        clear()
                        termcolor.cprint("> Ok!","magenta")
                        validasi1 = True
                        break
                    else:
                        termcolor.cprint(f"password salah! {ulang}x","red")
                        ulang += 1
    return validasi1

def registrasi():
    #user; password; valid_id -> auto, untuk mencek apakah data sudah ada di database lalu ditambahkan secara auto
    termcolor.cprint("= = = = Silakan input data = = = =","magenta")
    with open('login_database.txt', 'r') as baca:
        valid_user = []
        valid_id = 0
        for line in baca:
            xuser, xpassword, xid = line.split(',')
            valid_user.append(xuser)
            valid_id += 1
    while True:
        user = input(termcolor.colored('username : '.title(), "blue"))
        if user in valid_user or user == "":
            termcolor.cprint("> username terdaftar/tidak valid!","red")
        else:
            break
    while True:
        password1 = getpass.getpass(termcolor.colored('input password :'.title(), "blue"))
        if password1 == "" or len(password1) <= 3:
            termcolor.cprint("password terlalu lemah!, minimal 4 character","red")
        else:
            break
    atasi_infinitloop = 1
    while True:
        password2 = getpass.getpass(termcolor.colored('confirm password :'.title(), "blue"))
        if password2 != password1:
            termcolor.cprint(f"password tidak sesuai! {atasi_infinitloop}x","red")
            atasi_infinitloop += 1
            if atasi_infinitloop >= 4:
                exit("> Regitrasi gagal!")
        else:
            password1 = password2.encode()
            password1 = hashlib.md5(password1).hexdigest()
            break
    for i in range(3):
        termcolor.cprint("*","red", end="", flush=True)
        time.sleep(0.1)
    clear()
    
    # write ke login_database.txt
    with open('login_database.txt', 'a') as tulis:
        tulis.write(f"{user},{password1},{valid_id}\n")
        termcolor.cprint("selamat registrasi berhasil!","yellow")

def menu_user():
    termcolor.cprint("==== silahkan pilih fitur ===\n","blue")
    print("1. Perhitungan Kebutuhan Panen")
    print("2. Rekomendasi Pupuk")
    print("3. Perhitungan Bulan Panen")
    print("4. Resume fitur\n")

    answer = input("Masukan nomor : ")

    if answer == "1":
        print()
        termcolor.cprint("Tunggu Sebentar","blue")
        for i in range(3):
            termcolor.cprint("*","red", end="", flush=True)
            time.sleep(0.1)
        time.sleep(1.5)
        clear()
        hektar.hitung()
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    elif answer == "4":
        pass
    else:
        termcolor.cprint("Maaf fitur tidak tersedia!","red")
        time.sleep(1.5)
        clear()
        return menu_user()

def menu_admin():
    termcolor.cprint("==== silahkan pilih fitur ===\n","blue")
    print("1. Edit Rekomendasi Pupuk")
    print("2. Edit Perhitungan Bulan Panen")
    print("3. Lihat Resume User\n")

    answer = input("Masukan nomor : ")

    if answer == "1":
        pass
    elif answer == "2":
        pass
    elif answer == "3":
        pass
    else:
        termcolor.cprint("Maaf fitur tidak tersedia!","red")
        time.sleep(1.5)
        clear()
        return menu_admin()

def main():
    clear()
    print("<<< Selamat datang di aplikasi TaniKey >>>\n")
    print("Silakan pilih :\n1. admin\n2. login\n3. registrasi\n")
    answer = input("> ")
    validasi1 = False
    validasi2 = False

    if answer == "1" or answer == "admin":
        clear()
        validasi2 = admin()
    elif answer == "2" or answer == "login":
        clear()
        validasi1 = login()
    elif answer == "3" or answer == "registrasi":
        clear()
        registrasi()
        tanya = input(termcolor.colored("Apakah ingin lanjut login? [y/n]: ","blue"))
        if tanya == "y" or tanya == "Y":
            validasi1= login() #True/False
    else:
        print("Maaf kami tidak dapat memproses")
        time.sleep(3)
        return main()
    if validasi1:
        termcolor.cprint("Selamat anda berhasil login!","blue")
        time.sleep(2)
        clear()
        menu_user()
    if validasi2:
        termcolor.cprint("Selamat gan berhasil login!","blue")
        time.sleep(2)
        clear()    
        menu_admin()

    else:
        termcolor.cprint("Login ditolak","red")

#operasi aplikasi
# if __name__ == "__main__":
main()
    