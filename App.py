# Program Manajemen Kontak
import MyLib as lib

# List of Dictionary
daftar_barang = []

# Menu Program
while True:
    print("# Menu")
    print("1. Daftar Barang")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("0. Keluar")

    menu = input("Pilih menu : ")

    if menu == '0':
        break
    elif menu == '1':
        lib.display_barang(daftar_barang)
    elif menu == '2':
        barang = lib.new_barang()
        daftar_barang.append(barang)
    elif menu == '3':
        lib.hapus_barang(daftar_barang)
    elif menu == '4':
        lib.cari_barang(daftar_barang)
    else:
        print("Menu tidak tersedia")

print("Program berakhir. Sampai Jumpa")