# Modul Praktikum 4 Pertemuan ke-9

print("Nama : Miftahu Rizkiyah")
print("NIM : 312010014")
print("Kelas : TI.20.B.1")
print("===========================")
print("Latihan - Modul Praktikum 4")
print()
print()

#Membuat List dengan 5 elemen
daftar=[1,2,3,4,5];
print(daftar[:6]);
#Akses List
print("Menampilkan elemen ke 3");
print(daftar[3]);

print("Ambil nilai elemen ke 2 sampai ke 4");
print(daftar[2:5]);

print("Ambil nilai terakhir");
print(daftar[-1]);

#Ubah element list
print("ubah elemen ke 4 dengan nilai lainnya");
daftar[4]=8;
print(daftar[4]);

print("ubah elemen ke 4 sampai dengan elemen terakhir");
daftar[4:5]=[16,20];
print(daftar[4:6]);

#Tambah Element List
print("ambil 2 bagian dari list pertama(A) dan jadikan list ke2(B)");
baris=daftar[3:4];
print(baris[:2]);

print("tambah list B dengan nilai string")
print(baris.insert(3,"Febro"));

print("================================");

