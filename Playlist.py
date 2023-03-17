import os,time
from Musik import Musik

class Playlist:
  def __init__(self):
    self.__first_song = None

  # TODO: Buat METHOD add_Musik Membuat Objek lagu dan Menambahkan Ke Daftar Putar. Metode ini Memiliki 1 Parameter Yaitu TITLE
  def add_song(self, title):
    new_song = Musik(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song

  # TODO: Buat METHOD find_song yang Mencari Apakah lagu Keluar dari Playlist dan Mengembalikan indeksnya.Method ini mempunyai Parameter juga yaitu TITLE 
  def find_song(self, title):
    curr_song = self.__first_song
    index = 0
    if self.length() is None:
      return -1
    else:
      while curr_song:
        if curr_song.get_title() == title:
          return index
        else:
          index += 1
          curr_song = curr_song.get_next_song()
      return -1

  # TODO:Buat Method remove_song Yang Menghapus lagu dari Playlist. Method ini Mempunyai Parameter TITLE, yaitu lagu yang harus di Hapus 
  def remove_song(self, title):
    curr_song = self.__first_song

    if curr_song.get_title() == title: 
      self.__first_song = curr_song.get_next_song()
      return print(f'Menghapus {title} Dari Playlist')

    else: 
      while curr_song.get_title() != title:
        if curr_song.get_next_song().get_title() == title: 
          curr_song.set_next_song(curr_song.get_next_song())
          return print(f'Menghapus {title} Dari Playlist')
        else: 
          curr_song = curr_song.get_next_song()

  # TODO: Method length, Mengembalikan jumlah lagu Dalam Playlist 
  def length(self):
    index = 0
    curr_song = self.__first_song

    while curr_song != None:
      index += 1
      curr_song = curr_song.get_next_song()
    return index

  # TODO: Method Print_songs,Mencetak Playlist Bernomor di Playlist
  # Contoh:
  # 1. Judul Lagu 1
  # 2. Judul Lagu 2
  # 3. Judul Lagu 3
  def print_songs(self):
    index = 1
    curr_song = self.__first_song

    if curr_song == None:
      print(f"Tidak Ada Musik Didalam Playlist. Silahkan Tambahkan Musik")
      time.sleep(3)
      os.system('cls')
      return None

    while curr_song:
      print(f"{index}. {curr_song.get_title()}")
      index += 1
      curr_song = curr_song.get_next_song()