# Tugas Praktikum Modul 4

print("===================")
print("Nama     : MIFTAHU RIZKIYAH")
print("NIM      : 312010014")
print("Kelas    : TI.20.B.1")
print("===================")


# Buat program sederhana untuk menambahkan data kedalam sebuah list dengan rincian sebagai berikut :
# Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
#Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
# Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)
# Buat flowchart dan penjelasan programnya pada README.md.
# Commit dan push repository ke github.

sanex = []
stop = False

# Mengisi Nilai
while (not stop):
    nama = input("Masukkan Nama : ")
    nim  = input("Masukkan NIM : ")
    tugas = input("Masukkan Nilai Tugas : ")
    uts = input("Masukkan Nilai UTS : ")
    uas = input("Masukkan Nilai UAS : ")
    nilai_akhir = 0.3*float(tugas)*0.35*float(uts)*0.35*float(uas)
    sanex.append([nama, nim, tugas, uts, uas, nilai_akhir])

    tanya = input("Tambah data? (y/n)")
    if (tanya == "n"):
        stop = True

    # Cetak Semua Nilai

print("****")
no = 0
for isi in sanex:
    no += 1
    print(no, isi[0], isi[1], isi[2], isi[3], isi[4], isi[5])