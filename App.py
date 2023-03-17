import os, time
os.system('cls')
from Playlist import Playlist
playlist = Playlist()

while True:
  # Prints welcome message and options menu
  print('''
  \t  Playlist Youtube 🎶  
    Powered by LinkedList\u2122 technology
  =====================================
  Pilihan :
  1: Lihat Playlist
  2: Menambahkan Musik Kedalam Playlist
  3: Menghapus Musik Dari Playlist
  4: Mencari Musik Didalam Playlist
  5: Melihat Jumlah Musik Dalam Playlist
  6: Selesai
  =====================================
  ''')

  # Prints Selamat datang dan Menu Pilihan
  user_selection = int(input('  Masukkan Pilihan Yang Anda Inginkan: '))

  # Pilihan 1: Liat Playlist
  if user_selection == 1:
    time.sleep(1)
    os.system('cls')
    playlist.print_songs()

  # Pilihan 2: Menambahkan Lagu Pada Playlist
  elif user_selection == 2:
    time.sleep(1)
    os.system('cls')
    song_title = input('Judul Musik Apa Yang Ingin Kamu Tambahkan? ')
    playlist.add_song(song_title)
    time.sleep(1)
    os.system('cls')

  # Pilihan 3: Menghapus Lagu Pada Playlist
  elif user_selection == 3:
    time.sleep(1)
    os.system('cls')
    song_title = input('Judul Musik Apa Yang Ingin Kamu Hapus? ')
    print(playlist.remove_song(song_title))
    time.sleep(1)
    os.system('cls')

  # Pilihan 4: Mencari lagu Pada Playlist
  elif user_selection == 4:
    time.sleep(1)
    os.system('cls')
    song_title = input('Judul Musik Apa Yang Ingin Kamu Cari? ')
    index = playlist.find_song(song_title)
    
    if index == -1:
      print(f"Judul Musik {song_title} Tidak Ada Didalam Playlist.")
      time.sleep(3)
      os.system('cls')
    else:
      print(f"Judul Musik {song_title} Berada Pada Nomor {index+1}")
      time.sleep(3)
      os.system('cls')

  # Pilihan 5: Kembali Ke Deretan Playlist
  elif user_selection == 5:
    time.sleep(1)
    os.system('cls')
    print(f"Terdapat {playlist.length()} Judul Musik Dalam Playlist.")
    time.sleep(3)
    os.system('cls')

  # Pilihan 6: Keluar Dari Playlist
  elif user_selection == 6:
    time.sleep(1)
    os.system('cls')
    print(f"Terima Kasih.")
    time.sleep(3)
    os.system('cls')
    break
    
  # Input Tidak Valid
  else:
    print('Pilihan Tidak Valid Silahkan Masukkan Pilihan Dengan Benar!!!.\n')
    time.sleep(1)
    os.system('cls')
