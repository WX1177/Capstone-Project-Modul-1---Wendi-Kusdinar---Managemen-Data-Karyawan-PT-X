from tabulate import tabulate

# Menginisialisasi data karyawan dengan NIK sebagai primary key
employees = {
    'X001': {
        'Nama': 'Mardiana',
        'Posisi': 'Sales Engineer',
        'Bagian': 'Marketing',
        'Domisili': 'Bandung'
    },
    'X002': {
        'Nama': 'Ana Sumardi',
        'Posisi': 'Manager',
        'Bagian': 'Marketing',
        'Domisili': 'Garut'
    },
    'X003': {
        'Nama': 'Johan',
        'Posisi': 'Supervisor',
        'Bagian': 'Keuangan',
        'Domisili': 'Subang'
    },
    'X004': {
        'Nama': 'Ronny Hermawan',
        'Posisi': 'Manager',
        'Bagian': 'I T',
        'Domisili': 'Bandung'
    },
    'X005': {
        'Nama': 'Sandi Agustian',
        'Posisi': 'Supervisor',
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
    print("\t4. Menghapus Data Karyawan")
    print("\t5. Merubah Data Karyawan")
    print("\t6. Keluar Dari Program")
    print()

def display_employees():
    if not employees:
        print("Tidak ada data karyawan untuk ditampilkan.\n")
        return
    
    # Menyusun data untuk tabel
    report_data = [[nik, data['Nama'].title(), data['Posisi'].title(), data['Bagian'].title(), data['Domisili'].title()] for nik, data in employees.items()]

    # Menentukan header tabel
    headers = ["NIK", "NAMA", "POSISI", "BAGIAN", "DOMISILI"]

    # Menentukan panjang border
    border_length = 67  # Sesuaikan panjang border

    # Menampilkan tabel
    print("=" * border_length)  # Garis batas atas
    print(f"{'LAPORAN DATA KARYAWAN':^67}")  # Judul di tengah
    print("=" * border_length)  # Garis batas bawah
    print(tabulate(report_data, headers=headers, tablefmt="fancy_grid", stralign="center"))
    print()  # Baris kosong setelah tabel

def search_employee():
    while True:
        print("============================================")
        print("            MENCARI DATA KARYAWAN")
        print("============================================")
        print("Cari berdasarkan:")
        print("1. NIK")
        print("2. Nama")
        print("3. Posisi")
        print("4. Bagian")
        print("5. Domisili")
        print("6. Kembali ke Menu Utama")
        print()

        pilihan = input("Masukkan pilihan (1-6): ").strip()

        if pilihan == '1':
            keyword = input("Masukkan NIK yang ingin dicari (Format: X001): ").strip().upper()
            if not validate_nik(keyword):
                print("Terjadi kesalahan: Format NIK tidak valid. NIK harus dimulai dengan 'X' diikuti oleh tiga digit angka, contoh: X001.\n")
                continue
            results = {nik: data for nik, data in employees.items() if keyword == nik}
        elif pilihan == '2':
            keyword = input("Masukkan Nama yang ingin dicari: ").strip().lower()
            results = {nik: data for nik, data in employees.items() if keyword in data['Nama'].lower()}
        elif pilihan == '3':
            keyword = input("Masukkan Posisi yang ingin dicari: ").strip().lower()
            results = {nik: data for nik, data in employees.items() if keyword in data['Posisi'].lower()}
        elif pilihan == '4':
            keyword = input("Masukkan Bagian yang ingin dicari: ").strip().lower()
            results = {nik: data for nik, data in employees.items() if keyword in data['Bagian'].lower()}
        elif pilihan == '5':
            keyword = input("Masukkan Domisili yang ingin dicari: ").strip().lower()
            results = {nik: data for nik, data in employees.items() if keyword in data['Domisili'].lower()}
        elif pilihan == '6':
            print("Kembali ke Menu Utama.\n")
            break  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
            continue

        if pilihan in ['1', '2', '3', '4', '5']:
            if results:
                print(f"\nHasil Pencarian ({len(results)} ditemukan):")
                report_data = [[nik, data['Nama'].title(), data['Posisi'].title(), data['Bagian'].title(), data['Domisili'].title()] for nik, data in results.items()]
                headers = ["NIK", "Nama", "Posisi", "Bagian", "Domisili"]
                print(tabulate(report_data, headers=headers, tablefmt="fancy_grid", stralign="center"))
                print()
            else:
                print("Tidak ditemukan data karyawan yang sesuai dengan pencarian.\n")

def add_employee():
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
            if nik in employees:
                print("Terjadi kesalahan: NIK sudah ada. Silakan gunakan NIK yang berbeda.\n")
                continue
            break
        elif nik == '2':
            print("Kembali ke Menu Utama.\n")
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

    nama = get_non_empty_input("Masukkan Nama: ")
    posisi = get_non_empty_input("Masukkan Posisi: ")
    bagian = get_non_empty_input("Masukkan Bagian: ")
    domisili = get_non_empty_input("Masukkan Domisili: ")

    employees[nik] = {
        'Nama': nama.title(),
        'Posisi': posisi.title(),
        'Bagian': bagian.title(),
        'Domisili': domisili.title()
    }
    print("Data karyawan berhasil ditambahkan.\n")
    display_employees()

    # Pilihan untuk kembali ke menu utama
    input("Tekan Enter untuk kembali ke menu utama...")

def delete_employee():
    print("============================================")
    print("            MENGHAPUS DATA KARYAWAN")
    print("============================================")
    while True:
        print("1. Masukkan NIK Karyawan yang ingin dihapus (Format: X###):")
        print("2. Tampilkan Laporan Data Karyawan")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan (1-3): ").strip()

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
                continue  # Kembali ke menu delete_employee
            
            display_employees()  # Tampilkan laporan setelah penghapusan
            input("Tekan Enter untuk kembali ke menu utama...")
            return  # Kembali ke menu utama
        
        elif pilihan == '2':
            display_employees()
        elif pilihan == '3':
            print("Kembali ke Menu Utama.\n")
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

def edit_employee():
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

            print("Pilih data yang ingin diubah:")
            print("1. Nama")
            print("2. Posisi")
            print("3. Bagian")
            print("4. Domisili")
            print("5. Semua Data")
            print("6. Kembali ke Menu Utama")
            sub_pilihan = input("Masukkan pilihan (1-6): ").strip()

            if sub_pilihan == '1':
                nama_baru = get_non_empty_input("Masukkan Nama Baru: ")
                konfirmasi = input(f"Apakah Anda yakin ingin mengubah nama menjadi '{nama_baru.title()}'? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    employees[nik]['Nama'] = nama_baru.title()
                    print("Nama karyawan berhasil diubah.\n")
                else:
                    print("Perubahan nama dibatalkan.\n")
                    continue  # Kembali ke menu edit_employee
            elif sub_pilihan == '2':
                posisi_baru = get_non_empty_input("Masukkan Posisi Baru: ")
                konfirmasi = input(f"Apakah Anda yakin ingin mengubah posisi menjadi '{posisi_baru.title()}'? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    employees[nik]['Posisi'] = posisi_baru.title()
                    print("Posisi karyawan berhasil diubah.\n")
                else:
                    print("Perubahan posisi dibatalkan.\n")
                    continue  # Kembali ke menu edit_employee
            elif sub_pilihan == '3':
                bagian_baru = get_non_empty_input("Masukkan Bagian Baru: ")
                konfirmasi = input(f"Apakah Anda yakin ingin mengubah bagian menjadi '{bagian_baru.title()}'? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    employees[nik]['Bagian'] = bagian_baru.title()
                    print("Bagian karyawan berhasil diubah.\n")
                else:
                    print("Perubahan bagian dibatalkan.\n")
                    continue  # Kembali ke menu edit_employee
            elif sub_pilihan == '4':
                domisili_baru = get_non_empty_input("Masukkan Domisili Baru: ")
                konfirmasi = input(f"Apakah Anda yakin ingin mengubah domisili menjadi '{domisili_baru.title()}'? (y/n): ").strip().lower()
                if konfirmasi == 'y':
                    employees[nik]['Domisili'] = domisili_baru.title()
                    print("Domisili karyawan berhasil diubah.\n")
                else:
                    print("Perubahan domisili dibatalkan.\n")
                    continue  # Kembali ke menu edit_employee
            elif sub_pilihan == '5':
                nama_baru = get_non_empty_input("Masukkan Nama Baru: ")
                konfirmasi_nama = input(f"Apakah Anda yakin ingin mengubah nama menjadi '{nama_baru.title()}'? (y/n): ").strip().lower()
                if konfirmasi_nama == 'y':
                    posisi_baru = get_non_empty_input("Masukkan Posisi Baru: ")
                    konfirmasi_posisi = input(f"Apakah Anda yakin ingin mengubah posisi menjadi '{posisi_baru.title()}'? (y/n): ").strip().lower()
                    if konfirmasi_posisi == 'y':
                        bagian_baru = get_non_empty_input("Masukkan Bagian Baru: ")
                        konfirmasi_bagian = input(f"Apakah Anda yakin ingin mengubah bagian menjadi '{bagian_baru.title()}'? (y/n): ").strip().lower()
                        if konfirmasi_bagian == 'y':
                            domisili_baru = get_non_empty_input("Masukkan Domisili Baru: ")
                            konfirmasi_domisili = input(f"Apakah Anda yakin ingin mengubah domisili menjadi '{domisili_baru.title()}'? (y/n): ").strip().lower()
                            if konfirmasi_domisili == 'y':
                                employees[nik] = {
                                    'Nama': nama_baru.title(),
                                    'Posisi': posisi_baru.title(),
                                    'Bagian': bagian_baru.title(),
                                    'Domisili': domisili_baru.title()
                                }
                                print("Semua data karyawan berhasil diubah.\n")
                            else:
                                print("Perubahan domisili dibatalkan.\n")
                                continue  # Kembali ke menu edit_employee
                        else:
                            print("Perubahan bagian dibatalkan.\n")
                            continue  # Kembali ke menu edit_employee
                    else:
                        print("Perubahan posisi dibatalkan.\n")
                        continue  # Kembali ke menu edit_employee
                else:
                    print("Perubahan nama dibatalkan.\n")
                    continue  # Kembali ke menu edit_employee
            elif sub_pilihan == '6':
                print("Kembali ke Menu Utama.\n")
                return  # Kembali ke menu utama
            else:
                print("Pilihan tidak valid.\n")
                continue  # Kembali ke menu edit_employee

            display_employees()  # Tampilkan laporan setelah perubahan
            input("Tekan Enter untuk kembali ke menu utama...")
            return  # Kembali ke menu utama
        elif pilihan == '2':
            display_employees()  # Tampilkan laporan data karyawan
        elif pilihan == '3':
            print("Kembali ke Menu Utama.\n")
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Main program
while True:
    display_menu()
    choice = input("Masukkan pilihan (1-6): ").strip()
    
    if choice == '1':
        display_employees()
    elif choice == '2':
        search_employee()
    elif choice == '3':
        add_employee()
    elif choice == '4':
        delete_employee()
    elif choice == '5':
        edit_employee()
    elif choice == '6':
        print("Terima kasih! Program selesai.")
        break  # Keluar dari program
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")
