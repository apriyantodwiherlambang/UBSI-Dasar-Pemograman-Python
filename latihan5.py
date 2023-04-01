print("TOKO MAINAN ANAK")
print("*****************")

NamaPembeli = input("Masukan Nama Pembeli : ")
KodeMainan  = input("Kode Mainan : ")
HargaMainan = eval(input("Harga Mainan : "))
JumlahMainan = eval(input("Jumlah Mainan : "))
Total = HargaMainan * JumlahMainan
Diskon = int(10/100 * Total)
TotalBayar = Total - Diskon

print("Nama Pembeli : " +str(NamaPembeli))
print("Kode Mainan : " +str(KodeMainan))
print("Harga : " ,int(HargaMainan))
print("Jumlah Beli : " ,int(JumlahMainan))

print("Anda Mendapatkan Diskon 10%")

print("Total Sebelum Diskon : ",(Total))
print("Total Diskon : ",(Diskon))
print("Total Bayar Setelah Mendapatkan Diskon : ",(TotalBayar))