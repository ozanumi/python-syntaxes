"""
menunjukan semua syntax python
"""
from geometry.segitiga import hitung_luas_segitiga
from geometry.persegi_panjang import hitung_luas_panjang
print ('hi')

#menghitung luas segitiga

alas = 10
tinggi = 30
luas_segitiga = alas * tinggi/2
print (luas_segitiga)

#menggunakan logika percabangan

if luas_segitiga < 30 :
    print ('kecil')
elif luas_segitiga == 30:
    print ('pas')
else:
    print ('gede')

# perulangan
print ('dengan for')

for  i in range (0,10):
    print (i+1 , luas_segitiga)

#modularisasi tahap 1 : pembuatan fungsi



print(hitung_luas_segitiga('segitiga w',5,15))
print(hitung_luas_segitiga('segitiga o',3,6))


#modularisasi tahap 2 : pembuatan package

print (hitung_luas_panjang('persegi 1',10,2))
print (hitung_luas_panjang('persegi 2',5,3))
