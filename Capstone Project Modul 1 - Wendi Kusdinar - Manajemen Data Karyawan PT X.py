from tabulate import tabulate

employees = {
    'X001': {
        'Nama': 'Mardiana',
        'Jabatan': 'Sales Engineer',
        'Bagian': 'Marketing',
        'Domisili': 'Bandung'
    },
    'X002': {
        'Nama': 'Ana Sumardi',
        'Jabatan': 'Manager',
        'Bagian': 'Marketing',
        'Domisili': 'Garut'
    },
    'X003': {
        'Nama': 'Johan',
        'Jabatan': 'Supervisor',
        'Bagian': 'Keuangan',
        'Domisili': 'Subang'
    },
    'X004': {
        'Nama': 'Ronny Hermawan',
        'Jabatan': 'Manager',
        'Bagian': 'I T',
        'Domisili': 'Bandung'
    },
    'X005': {
        'Nama': 'Sandi Agustian',
        'Jabatan': 'Supervisor',
        'Bagian': 'Produksi',
        'Domisili': 'Purwakarta'
    }
}

def validate_nik(nik):
    """Memvalidasi format NIK."""    
    return nik.startswith('X') and nik[1:].isdigit() and len(nik) == 4

def get_non_empty_input(prompt):
    """Mendapatkan input dari pengguna dan memastikan input tidak kosong."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input tidak boleh kosong. Silakan coba lagi.")

def display_menu():
    print("============================================")
    print("            DATA KARYAWAN PT X")
    print("============================================")
    print("\t1. Laporan Data Karyawan")
    print("\t2. Mencari Data Karyawan")
    print("\t3. Menambah Data Karyawan")
    print("\t4. Merubah Data Karyawan")
    print("\t5. Menghapus Data Karyawan")
    print("\t6. Keluar Dari Program")
    print()


def display_employees():
    try:
        try:
            if not employees:
                print("Tidak ada data karyawan untuk ditampilkan.\n")
                return

            report_data = [[nik, data['Nama'].title(), data['Jabatan'].title(), data['Bagian'].title(), data['Domisili'].title()] for nik, data in employees.items()]
           
            headers = ["NIK", "NAMA", "JABATAN", "BAGIAN", "DOMISILI"]
            
            border_length = 67
            print("=" * border_length)
            print(f"{'LAPORAN DATA KARYAWAN':^67}")
            print("=" * border_length)
            print(tabulate(report_data, headers=headers, tablefmt="fancy_grid", stralign="center"))
            print()
        except Exception as e:
            print(f"Terjadi kesalahan saat memproses data karyawan: {e}\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan data: {e}\n")

def search_employee():
    try:
        while True:
            print("============================================")
            print("            MENCARI DATA KARYAWAN")
            print("============================================")
            print("Cari berdasarkan:")
            print("1. NIK")
            print("2. Nama")
            print("3. Jabatan")
            print("4. Bagian")
            print("5. Domisili")
            print("6. Tampilkan Laporan Data Karyawan")
            print("7. Kembali ke Menu Utama")
            print()

            pilihan = input("Masukkan pilihan (1-7): ").strip()

            if pilihan == '1':
                keyword = input("Masukkan NIK yang ingin dicari (Format: X###, contoh: X001): ").strip().upper()
                if not validate_nik(keyword):
                    print("Terjadi kesalahan: Format NIK tidak valid. NIK harus dimulai dengan 'X' diikuti oleh tiga digit angka, contoh: X001.\n")
                    continue
                results = {nik: data for nik, data in employees.items() if keyword == nik}
            elif pilihan == '2':
                keyword = input("Masukkan Nama yang ingin dicari: ").strip().lower()
                results = {nik: data for nik, data in employees.items() if keyword in data['Nama'].lower()}
            elif pilihan == '3':
                keyword = input("Masukkan Jabatan yang ingin dicari: ").strip().lower()
                results = {nik: data for nik, data in employees.items() if keyword in data['Jabatan'].lower()}
            elif pilihan == '4':
                keyword = input("Masukkan Bagian yang ingin dicari: ").strip().lower()
                results = {nik: data for nik, data in employees.items() if keyword in data['Bagian'].lower()}
            elif pilihan == '5':
                keyword = input("Masukkan Domisili yang ingin dicari: ").strip().lower()
                results = {nik: data for nik, data in employees.items() if keyword in data['Domisili'].lower()}
            elif pilihan == '6':
                display_employees() 
            elif pilihan == '7':
                print("Kembali ke Menu Utama.\n")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")
                continue

            if pilihan in ['1', '2', '3', '4', '5']:
                if results:
                    print(f"\nHasil Pencarian ({len(results)} ditemukan):")
                    report_data = [[nik, data['Nama'].title(), data['Jabatan'].title(), data['Bagian'].title(), data['Domisili'].title()] for nik, data in results.items()]
                    headers = ["NIK", "NAMA", "JABATAN", "BAGIAN", "DOMISILI"]
                    print(tabulate(report_data, headers=headers, tablefmt="fancy_grid", stralign="center"))
                    print()
                else:
                    print("Tidak ditemukan data karyawan yang sesuai dengan pencarian.\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat mencari data: {e}\n")


def add_employee():
    try:
        print("============================================")
        print("            MENAMBAH DATA KARYAWAN")
        print("============================================")
        
        while True:
            print("1. Masukkan NIK Baru (Format: X###):")
            print("2. Kembali ke Menu Utama")
            nik = input("Masukkan pilihan (1-2): ").strip()

            if nik == '1':
                nik = input("Masukkan NIK Baru (Format: X###): ").strip().upper()
                
                if not nik:
                    print("NIK tidak boleh kosong. Silakan coba lagi.")
                    continue
                
                if not validate_nik(nik):
                    print("Terjadi kesalahan: Format NIK tidak valid. Harus dimulai dengan 'X' diikuti oleh tiga digit angka (misalnya, X006).\n")
                    continue            
               
                if int(nik[1:]) < 1:
                    print("Terjadi kesalahan: NIK tidak boleh kurang dari X001. Silakan gunakan NIK yang valid.\n")
                    continue
                
                if nik in employees:
                    print("Terjadi kesalahan: NIK sudah ada. Silakan gunakan NIK yang berbeda.\n")
                    continue
                nama = get_non_empty_input("Masukkan Nama Lengkap: ")
                posisi = get_non_empty_input("Masukkan Jabatan: ")
                bagian = get_non_empty_input("Masukkan Bagian: ")
                domisili = get_non_empty_input("Masukkan Domisili: ")
                
                employees[nik] = {
                    'Nama': nama.title(),
                    'Jabatan': posisi.title(),
                    'Bagian': bagian.title(),
                    'Domisili': domisili.title()
                }
                print("Data karyawan berhasil ditambahkan.\n")
                display_employees()

            elif nik == '2':
                print("Kembali ke Menu Utama.\n")
                return
            
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menambahkan data karyawan: {e}\n")



def edit_employee():
    try:
        print("============================================")
        print("            MERUBAH DATA KARYAWAN")
        print("============================================")
        while True:
            print("1. Masukkan NIK Karyawan yang ingin diubah (Format: X###):")
            print("2. Tampilkan Laporan Data Karyawan")
            print("3. Kembali ke Menu Utama")
            pilihan = input("Masukkan pilihan (1-3): ").strip()

            if pilihan == '1':
                nik = input("Masukkan NIK Karyawan yang ingin diubah (Format: X###): ").strip().upper()
                if not validate_nik(nik):
                    print("Terjadi kesalahan: Format NIK tidak valid. NIK harus dimulai dengan 'X' diikuti oleh tiga digit angka, contoh: X001.\n")
                    continue
                if nik not in employees:
                    print("Terjadi kesalahan: NIK tidak ditemukan.\n")
                    continue
                    
                data_lama = employees[nik]
                print("Pilih data yang ingin diubah:")
                print("1. Nama")
                print("2. Jabatan")
                print("3. Bagian")
                print("4. Domisili")
                print("5. Semua Data")
                print("6. Kembali ke Menu Utama")
                sub_pilihan = input("Masukkan pilihan (1-6): ").strip()

                if sub_pilihan == '1':
                    nama_baru = get_non_empty_input("Masukkan Nama Baru: ")                    
                    konfirmasi = input(f"Apakah Anda yakin ingin mengubah nama dari '{data_lama['Nama']}' menjadi '{nama_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        employees[nik]['Nama'] = nama_baru.title()
                        print("Nama karyawan berhasil diubah.\n")
                    else:
                        print("Perubahan nama dibatalkan.\n")
                        continue
                elif sub_pilihan == '2':
                    posisi_baru = get_non_empty_input("Masukkan Jabatan Baru: ")
                    konfirmasi = input(f"Apakah Anda yakin ingin mengubah posisi dari '{data_lama['Jabatan']}' menjadi '{posisi_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        employees[nik]['Jabatan'] = posisi_baru.title()
                        print("Jabatan karyawan berhasil diubah.\n")
                    else:
                        print("Perubahan posisi dibatalkan.\n")
                        continue 
                elif sub_pilihan == '3':
                    bagian_baru = get_non_empty_input("Masukkan Bagian Baru: ")                   
                    konfirmasi = input(f"Apakah Anda yakin ingin mengubah bagian dari '{data_lama['Bagian']}' menjadi '{bagian_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        employees[nik]['Bagian'] = bagian_baru.title()
                        print("Bagian karyawan berhasil diubah.\n")
                    else:
                        print("Perubahan bagian dibatalkan.\n")
                        continue
                elif sub_pilihan == '4':
                    domisili_baru = get_non_empty_input("Masukkan Domisili Baru: ")                    
                    konfirmasi = input(f"Apakah Anda yakin ingin mengubah domisili dari '{data_lama['Domisili']}' menjadi '{domisili_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi == 'y':
                        employees[nik]['Domisili'] = domisili_baru.title()
                        print("Domisili karyawan berhasil diubah.\n")
                    else:
                        print("Perubahan domisili dibatalkan.\n")
                        continue
                elif sub_pilihan == '5':
                    nama_baru = get_non_empty_input("Masukkan Nama Baru: ")
                    konfirmasi_nama = input(f"Apakah Anda yakin ingin mengubah nama dari '{data_lama['Nama']}' menjadi '{nama_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi_nama == 'y':
                        posisi_baru = get_non_empty_input("Masukkan Jabatan Baru: ")
                        konfirmasi_posisi = input(f"Apakah Anda yakin ingin mengubah posisi dari '{data_lama['Jabatan']}' menjadi '{posisi_baru.title()}'? (y/n): ").strip().lower()
                        if konfirmasi_posisi == 'y':
                            bagian_baru = get_non_empty_input("Masukkan Bagian Baru: ")
                            konfirmasi_bagian = input(f"Apakah Anda yakin ingin mengubah bagian dari '{data_lama['Bagian']}' menjadi '{bagian_baru.title()}'? (y/n): ").strip().lower()
                            if konfirmasi_bagian == 'y':
                                domisili_baru = get_non_empty_input("Masukkan Domisili Baru: ")
                                konfirmasi_domisili = input(f"Apakah Anda yakin ingin mengubah domisili dari '{data_lama['Domisili']}' menjadi '{domisili_baru.title()}'? (y/n): ").strip().lower()
                                if konfirmasi_domisili == 'y':
                                    employees[nik] = {
                                        'Nama': nama_baru.title(),
                                        'Jabatan': posisi_baru.title(),
                                        'Bagian': bagian_baru.title(),
                                        'Domisili': domisili_baru.title()
                                    }
                                    print("Semua data karyawan berhasil diubah.\n")
                                else:
                                    print("Perubahan domisili dibatalkan.\n")
                                    continue  
                            else:
                                print("Perubahan bagian dibatalkan.\n")
                                continue  
                        else:
                            print("Perubahan posisi dibatalkan.\n")
                            continue  
                    else:
                        print("Perubahan nama dibatalkan.\n")
                        continue 
                elif sub_pilihan == '6':
                    print("Kembali ke Menu Utama.\n")
                    return  
                else:
                    print("Pilihan tidak valid.\n")
                    continue  
                display_employees()
                
            elif pilihan == '2':
                display_employees() 
            elif pilihan == '3':
                print("Kembali ke Menu Utama.\n")
                return
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n") 
    except Exception as e:
        print(f"Terjadi kesalahan saat mengubah data karyawan: {e}\n")
        
def delete_employee():
    try:
        print("============================================")
        print("            MENGHAPUS DATA KARYAWAN")
        print("============================================")
        while True:
            print("1. Masukkan NIK Karyawan yang ingin dihapus (Format: X###):")
            print("2. Tampilkan Laporan Data Karyawan")
            print("3. Menghapus Semua Data Karyawan")
            print("4. Kembali ke Menu Utama")
            pilihan = input("Masukkan pilihan (1-4): ").strip()

            if pilihan == '1':
                nik = input("Masukkan NIK Karyawan yang ingin dihapus (Format: X###): ").strip().upper()
                if not validate_nik(nik):
                    print("Terjadi kesalahan: Format NIK tidak valid. NIK harus dimulai dengan 'X' diikuti oleh tiga digit angka, contoh: X001.\n")
                    continue
                if nik not in employees:
                    print("Terjadi kesalahan: NIK tidak ditemukan.\n")
                    continue
                
                confirm = input(f"Apakah Anda yakin ingin menghapus data karyawan dengan NIK {nik}? (y/n): ").strip().lower()
                if confirm == 'y':
                    del employees[nik]
                    print("Data karyawan berhasil dihapus.\n")
                else:
                    print("Penghapusan dibatalkan.\n")
                    continue
                display_employees()
                
            elif pilihan == '2':
                display_employees()

            elif pilihan == '3':
                confirm_all = input("Apakah Anda yakin ingin menghapus semua data karyawan? (y/n): ").strip().lower()
                if confirm_all == 'y':
                    employees.clear()
                    print("Semua data karyawan berhasil dihapus.\n")
                else:
                    print("Penghapusan semua data dibatalkan.\n")
                display_employees()

            elif pilihan == '4':
                print("Kembali ke Menu Utama.\n")
                return
            else:
                print("Pilihan tidak valid. Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghapus data karyawan: {e}\n")

#Menjalankan program utama
while True:
    display_menu()
    try:
        choice = input("Masukkan pilihan (1-6): ").strip()

        if choice == '1':
            display_employees()
        elif choice == '2':
            search_employee()
        elif choice == '3':
            add_employee()
        elif choice == '4':
            edit_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Terima kasih! Program sudah selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
    except Exception as e:
        print(f"Terjadi kesalahan pada menu utama: {e}. Silakan coba lagi.")
