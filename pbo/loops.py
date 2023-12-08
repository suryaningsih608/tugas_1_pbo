# Memulai perulangan for dengan variabel iterasi s, yang akan mengambil nilai dari 1 hingga 100.
for s in range(1, 101):
     # Memeriksa apakah nilai s merupakan kelipatan 10.
    if s % 10 == 0:
      # Jika nilai s adalah kelipatan 10, pernyataan ini akan mencetak string "Suryaningsih" sebanyak tiga kali
      print("Suryaningsih\nSuryaningsih\nSuryaningsih")
    # Jika kodisi sebelumnya belum terpenuhi
    else: 
      #  Jika nilai s bukan kelipatan 10, maka pernyataan ini akan mencetak nilai s..
      print(s)