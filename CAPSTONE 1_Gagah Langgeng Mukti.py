from tabulate import tabulate
import os

listBarang = [
    [101, 'Jaket', 'Jaket Kulit', 'S', 30, 300000],
    [102, 'Jaket', 'Jaket Kulit', 'M', 30, 300000],
    [103, 'Jaket', 'Jaket Kulit', 'L', 30, 300000],
    [201, 'Kaos', 'Kaos Oversized', 'S', 30, 150000],
    [203, 'Kaos', 'Kaos Oversized', 'L', 30, 150000],
    [204, 'Kaos', 'Kaos Oversized', 'XL', 30, 150000],
    [302, 'Kemeja', 'Kemeja Flanel', 'M', 30, 200000],
    [303, 'Kemeja', 'Kemeja Flanel', 'L', 30, 200000],
    [304, 'Kemeja', 'Kemeja Flanel', 'XL', 30, 200000],
    ]

def clear():
    os.system('cls')

def menu():
    print('\n\t\t\tSELAMAT DATANG DI BLACK MAMBA\n\n'
          'Menu:\n'
          '1. Tampilkan daftar barang\n'
          '2. Pencarian barang\n'
          '3. Tambah barang\n'
          '4. Update barang\n'
          '5. Hapus barang\n'
          '6. Beli barang\n'
          '7. Keluar\n')

def list():
    header = ['No. Item', 'Jenis barang', 'Nama barang', 'Ukuran', 'Stock', 'Harga']
    tabel  = (tabulate(listBarang, headers = header, tablefmt = 'fancy_outline')).upper()
    print(tabel)

# MENU CARI
def cariData(barang):
    ulang = True
    while ulang:
        while True:
            cari = input('Masukkan Jenis/Nama/Ukuran barang yang dicari: ').upper()
            list_cari = []
            for baris in barang:
                if cari.upper() in [baris[i].upper() for i in range(1,4)]:
                    list_cari.append(baris)
            if list_cari:
                header = ['No. Item', 'Jenis barang', 'Nama barang', 'Ukuran', 'Stock', 'Harga']
                tabel  = (tabulate(list_cari, headers = header, tablefmt = 'fancy_outline')).upper()
                print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
                print(tabel)
                break
            else:
                print('Barang tidak ditemukan')
                break
        while True:
            lanjut = input('Cari barang lagi? (Y/T): ').upper()
            if lanjut == 'T':
                ulang = False
                break
            elif lanjut == 'Y':
                break
            else:
                print('Masukkan Y atau T')

# MENU TAMBAH
def tambahData(barang):
    item = []
    ulang = True
    while ulang:
        while True:
            print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
            list()
            print('Item yang akan ditambahkan:\n')
            no_item = input('Masukkan No. Item: ')
            if no_item.isdigit() == False:
                print('Masukkan No. Item dengan benar')
            else:
                no_item_int = int(no_item)
                if any(item_tersedia[0] == no_item_int for item_tersedia in barang):
                    print(f'No. item {no_item_int} sudah ada. Masukkan No. item lain!\n')
                else:
                    item.append(no_item_int)
                    break
        while True:
            jenis = input('Masukkan jenis barang: ').upper()
            item.append(jenis)

            nama = input('Masukkan Nama barang: ').upper()
            item.append(nama)
            break
        while True:
            size = input('Masukkan ukuran: ').upper()
            if size in ['S', 'M', 'L', 'XL']:
                item.append(size)
                break
            else:
                print('Ukuran hanya S/M/L/XL')
        while True:
            stok = input('Masukkan stok: ')
            if stok.isdigit() == False:
                print('Masukkan stok dengan benar')
            else:
                item.append(stok)
                break
        while True:
            harga = input('Masukkan harga: ')
            if harga.isdigit() == False:
                print('Masukkan harga dengan benar')
            else:
                item.append(harga)
                break
        barang.append(item)
        barang.sort(key=lambda x: int(x[0]))
        print(f'\nBarang dengan No. Item {no_item} berhasil ditambah\n')
        print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
        print(tabulate(barang, headers = ['No. Item', 'Jenis barang', 'Nama barang', 'Ukuran', 'Stock', 'Harga'], tablefmt = 'fancy_outline').upper())
        break

    while True:
        lanjut = input('Apakah ada item lain yang ingin ditambahkan ke daftar? (Y/T): ').upper()
        if lanjut == 'T':
            ulang = False
            break
        elif lanjut == 'Y':
            break
        else:
            print('Masukkan Y atau T')

# MENU UPDATE
def updateData(barang):
    ulang = True
    while ulang:
        while True:
            print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
            list()
            update_pilih = int(input('Yang akan diupdate:\n'
                                    '1. Stok\n'
                                    '2. Harga\n'
                                    'Masukkan pilihan (1-2): '))
            if update_pilih == 1 or update_pilih == 2:
                update = int(input('Masukkan no. item barang yang akan diupdate: \n'))
                for i in range (len(barang)):
                    if update == barang[i][0]:
                        while True:
                            if update_pilih == 1:
                                stock_baru = input('Masukkan stok: ')
                                if stock_baru.isdigit() == False:
                                    print('Masukkan angka!')
                                else:
                                    barang[i][-2] = int(stock_baru)
                                    print('Update berhasil')
                                    break
                            elif update_pilih == 2:
                                harga_baru = input('Masukkan harga: ')
                                if harga_baru.isdigit() == False:
                                    print('Masukkan angka!')
                                else:
                                    barang[i][-1] = int(harga_baru)
                                    print('Update berhasil')
                                    break
                        list()
                        break
                else:
                    print(f'No. Item {update} tidak ada dalam daftar')
                    break
                break
            else:
                print('Masukkan pilihan yang benar')
                break
        while True:
            lanjut = input('lanjut update barang ? (Y/T):').upper()
            if lanjut == 'T':
                ulang = False
                break
            elif lanjut == 'Y':
                break
            else:
                print('Masukkan Y atau T')
          
# MENU HAPUS
def hapusData(barang):
    ulang = True
    while ulang:
        while True:
            print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
            list()
            hapus = int(input('Masukkan no. item yang akan dihapus: '))
            item_hapus = False
            for i in range (len(barang)):
                if hapus == barang[i][0]:
                    barang.pop(i)
                    item_hapus = True
                    print('\nBarang berhasil dihapus\n')
                    list()
                    break
            if item_hapus == False:
                print('Barang tidak ditemukan')
            break
        
        while True:
            lanjut = input('Apakah ada item lain yang akan dihapus? (Y/T): ').upper()
            if lanjut == 'T':
                ulang = False
                break
            elif lanjut == 'Y':
                break
            else:
                print('Masukkan Y atau T')

# MENU BELI
def beliBarang(barang):
    cart = []
    ulang = True
    while ulang:
        while True:
            list_beli = []
            print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
            list()
            beli = int(input('Masukkan no. item yang akan dibeli: '))

            for i in range(len(barang)):
                if beli == barang[i][0]:
                    for data in barang[i]:
                        list_beli.append(data)
                    jumlahBeli = int(input('Masukkan jumlah yang akan dibeli: '))

                    if jumlahBeli > list_beli[-2]:
                        print(f'Stok tidak cukup, sisa stok yang tersedia: {list_beli[-2]}')
                        break
                    else:
                        list_beli[-2] = jumlahBeli
                        cart.append(list_beli)
                        header = ['No. Item', 'Jenis barang', 'Nama barang', 'Ukuran', 'Jumlah item', 'Harga']
                        tabel = (tabulate(cart, headers=header, tablefmt='fancy_outline')).upper()
                        print(tabel)
                        barang[i][-2] -= jumlahBeli
                        break
            else:
                print(f'No. item {beli} tidak ditemukan')
            break

        while True:
            lanjut = input('Apakah ada item lain yang ingin dibeli? (Y/T): ').upper()
            if lanjut == 'T':
                ulang = False
                break
            elif lanjut == 'Y':
                break
            else:
                print('Masukkan Y atau T')
                
    print(f'\n\t\t\t  DAFTAR BELANJA\n')
    totalHarga = 0
    cart_final=[[i[2],i[3],i[4],i[5],i[4]*i[5]] for i in cart]
    header_cart = ['Item','Ukuran','Jumlah','Harga Satuan', 'Total']
    tabel  = (tabulate (cart_final, headers=header_cart,tablefmt = 'fancy_outline')).upper()
    print(tabel)
    totalHarga = sum(item[2] * item[3] for item in cart_final)
    while True:
        print(f'Total harga yang harus dibayar: Rp {totalHarga:,d}')
        cash = int(input('Masukkan jumlah uang: '))
        if(cash<totalHarga):
            print(f'Mohon maaf, Anda kekurangan uang sebesar Rp {abs(cash-totalHarga):,d}')
        else:
            print(f'Terima kasih, anda menerima kembalian sebesar Rp {(cash-totalHarga):,d}')
            break

#################################################################################################################

while True:
    try:
        menu()
        Menu = int(input('Masukkan menu (1-7): '))
        
        if Menu == 1:
            clear()
            print('\n\t\t\t  DAFTAR BARANG BLACK MAMBA\n')
            list()

        elif Menu == 2:
            clear()
            cariData(listBarang)

        elif Menu == 3 :
            clear()
            tambahData(listBarang)

        elif Menu == 4:
            clear()
            updateData(listBarang)

        elif Menu == 5:
            clear()
            hapusData(listBarang)

        elif Menu == 6:
            clear()
            beliBarang(listBarang)

        elif Menu == 7:
            print('Terima kasih')
            break
    except:
        print('Masukkan inputan dengan benar')
