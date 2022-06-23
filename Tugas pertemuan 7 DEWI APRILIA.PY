# NAMA  : DEWI APRILIA
# NIM   : 210101012
# KELAS : 21A1-SISTEM INFORMASI
# MATKUL: BAHASA PEMROGRAMAN

print('PROGRAM PENDETEKSI DEMAM\n'
      '===========================================')
nama = input('Masukan Nama Anda : ')
menu = 0
while menu != 'n':
    gejala = input('Apakah Anda Merasakan Gejala Berikut ini?\n'
                '1. Demam/Suhu badan tinggi\n'
                '2. Sakit Kepala\n'
                '3. Nyeri Pada Sendi Otot dan Tulang\n'
                '4. Mual dan Muntah\n'
                '===========================================\n'
                'Ya (y) / Tidak (n) : ')
    if gejala == 'y':
        gejala2 = input('Apakah Anda Merasakan Gejala Berikut ini?\n'
                     '1. Menggigil sedang sampai berat\n'
                     '2. Tubuh Kelelahan\n'
                     '3. Banyak Berkeringat\n'
                     '4. Diare\n'
                     '===========================================\n'
                     'Ya (y) / Tidak (n) : ')
        if gejala2 == 'y':
            print(f'Halo {nama}, hasil awal diagnosis kamu adalah Gejala Malaria')
            menu = input('Apakah Anda ingin melanjutkan diagnosis? (y) / (n) : ')
        elif gejala2 == 'n':
            gejala3 = input('Apakah Anda Merasakan Gejala Berikut ini?\n'
                         '1. Hilang Nafsu Makan\n'
                         '2. Nyeri Pada Bagian Belakang Mata\n'
                         '3. Ruam Kemerahan\n'
                         '===========================================\n'
                         'Ya (y) / Tidak (n) : ')
            if gejala3 == 'y':
                print(f'Halo {nama}, hasil awal diagnosis kamu adalah Gejala demam berdarah')
                menu = input('Apakah Anda ingin melanjutkan diagnosis? (y) / (n) : ')
            elif gejala3 == 'n':
                print('Sepertinya Anda Sedang Banyak Hutang :(')
                menu = input('Apakah Anda ingin melanjutkan diagnosis? (y) / (n) : ')
    elif gejala == 'n':
        print('Sepertinya Anda Butuh Jalan-Jalan :)')
        menu = input('Apakah Anda ingin melanjutkan diagnosis? (y) / (n) : ')
else:
    print(f'Terimakasih {nama}, Semoga Sehat Selalu :)')
    