# Membuat list yang berisi beberapa nama
names = ["Suryaningsih", "Lilis", "Jhon", "prita", "Indah"]

# Memulai perulangan for untuk setiap elemen dalam list 
for name in names:
    # Memeriksa jumlah karakter nama
    if len(name) % 2 == 0:
        # Jika jumlahnya genap maka akan mencetak ini
        print(f"{name} memiliki jumlah huruf genap")
    # Jika kodisi sebelumnya belum terpenuhi
    else: 
        # Jika jumlahnya bukan genap (ganjil) maka akan mencetak ini
        print(f"{name} memiliki jumlah huruf ganjil")