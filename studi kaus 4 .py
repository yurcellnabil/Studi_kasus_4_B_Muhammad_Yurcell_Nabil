buku = {
    "judul": "Pemrograman Python Dasar",
    "penulis": "Andi Pratama",
    "tahun_terbit": 2024
}

while True:
    print("MENU BUKU")
    print("1. Tampilkan Data Buku")
    print("2. Tambah Data Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")
    
    pilihan = input("Pilihan (1-5): ")
    
    if pilihan == "1":
        print("Data Buku:")
        print(buku)
        print("Judul:", buku["judul"])
        print("Key:", buku.keys())
        print("Value:", buku.values())
        
    elif pilihan == "2":
        penerbit = input("Masukkan nama penerbit: ")
        buku["penerbit"] = penerbit
        
        print("Hasil Add Penerbit:")
        print(buku)
        
    elif pilihan == "3":
        penulis_baru = input("Masukkan nama penulis baru: ")
        buku.update({"penulis": penulis_baru})
        
        print("Hasil Update Penulis:")
        print(buku)
        
    elif pilihan ==  "4":
        if "penerbit" in buku:
            buku.pop("penerbit")
            print("\nHasil Delete Penerbit:")
            print(buku)
        else:
            print("Key 'penerbit' tidak ditemukan!")
            
    elif pilihan == "5":
        print("Program selesai.")
        break
        
    else:
        print("Pilihan tidak valid!")