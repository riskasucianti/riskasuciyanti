print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA")
print("==========================================")
print()

def hitungLuasSegitiga(a, t):
    return round(0.5 * a * t,2)

alas = float(input("Input Alas Segitiga :"))
tinggi = float(input("Input Tinggi Segitiga :"))

print('Luas Segitiga =', hitungLuasSegitiga(alas, tinggi))
print()

print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA")
print("==========================================")
print()

def hitungPersegiPanjang(p,l):
    return round(p * 1,2)

 panjang= float(input('input panjang :'))
 lebar= float(input('input lebar :'))
print('Luas persegi panjang =',hitungPersegiPanjang(panjang, lebar))