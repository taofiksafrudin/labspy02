a = input("Masukan Bilangan A :")
b = input("Masukan Bilangan B :")
c = input("Masukan Bilinagn C :")

if a > b and a > c:
    terbesar = a
else:
    if b > c and b > a:
        terbesar = b
    else:
        terbesar = c

print("Jadi Bilangan Terbesar Adalah :",terbesar)