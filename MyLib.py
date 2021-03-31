# Function Manajemen Kontak
import pandas as pd
from operator import itemgetter

def display_barang(daftar_barang):
    daftar_barang.sort(key=itemgetter('id'))
    
    for barang in daftar_barang:
        print("===============================")
        print(f"ID : {barang['id']}")
        print(f"Nama Barang : {barang['nama']}")
        print(f"Harga : {barang['harga']}")
        print("===============================")

    '''pandas data frame (beta)'''
    # print("===============================")
    # df = pd.DataFrame(daftar_barang)
    # print(df)
    # print("===============================")
    '''if you read this, pls teach me how remove index in pandas data frame :D'''

def new_barang():
    id = int(input("ID Barang : "))
    nama = input("Nama Barang : ").upper()
    harga = int(input("Harga Barang : "))
    barang = {
        'id': id,
        'nama': nama,
        'harga': harga
    }
    return barang

def hapus_barang(daftar_barang):
    id = int(input("ID Barang yang akan dihapus : "))
    index = -1
    for i in range(0, len(daftar_barang)):
        barang = daftar_barang[i]
        if id == barang['id']:
            index = 1
            break
    if index == -1:
        print("Data tidak ditemukan.")
    else:
        del daftar_barang[index]
        print("Berhasil menghapus data barang.")

def cari_barang(daftar_barang):
    nama_yg_dicari = input("Nama Barang yang dicari : ").upper()

    for barang in daftar_barang:
        nama = barang['nama']
        if nama.find(nama_yg_dicari) != -1:
            print("===============================")
            print(f"ID : {barang['id']}")
            print(f"Nama Barang : {barang['nama']}")
            print(f"Harga : {barang['harga']}")
            print("===============================")