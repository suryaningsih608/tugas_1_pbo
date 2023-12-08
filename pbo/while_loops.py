# Melacak indeks saat ini selama perulangan
counter = 0
# : Membuat list names yang berisi beberapa nama
names = ["Suryaningsih", "Lilis", "Jhon", "prita", "Indah"]

# Memulai perulangan while yang akan berlangsung selama nilai counter kurang dari panjang (jumlah elemen) dari list names.
while counter < len(names):
    #  Mengambil nilai dari list names pada indeks yang ditunjukkan oleh nilai counter saat ini dan menyimpannya dalam variabel name.
    name = names[counter]
    # Memeriksa apakah panjang (jumlah karakter)
    if len(name) % 2 == 0:
        # Jika panjang nama adalah bilangan genap, pernyataan ini akan mencetak pesan
        print(f"{name} memiliki jumlah huruf genap")
    # Jika kodisi sebelumnya belum terpenuhi
    else:
        # Jika panjang nama bukan bilangan genap, pernyataan ini akan mencetak pesan 
        print(f"{name} memiliki jumlah huruf ganjil")
    # Meningkatkan nilai 
    counter += 1