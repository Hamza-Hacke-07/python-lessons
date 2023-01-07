# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:37:45 2022

@author: Asomiddinov Hamza Sharofiiddin o'g'li
"""

#   for BILAN TANISHAMIZ
#  Dasturlash davomida kodimizning biror qismini bir necha marta takrorlash talab etilishi mumkin. Misol uchun, ro'yxat ichidagi har bir elementni alohida qatordan konsolga chiqarish, yoki bo'lmasa har bir elementni kvdartaga oshirish va hokazo. Mana shunday vaziyatlarda bizga for operatori yordam beradi. Dasturlashda bu tsikl (loop) deb ataladi. 
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print("Salom ", mehmon)
    
#   for QANDAY ISHLAYDI
#  Yuqoridagi kodda 2-qator bu tsikl boshi deyiladi. Aynan shu qator kodimiz nech marta takrorlanishini aniqlaydi. Bizning holatimizda tsikl mehmonlar ro'yxati ichidagi elementlar tugagunga qadar takrorlanadi. Tsikl boshlanishi ikki nuqta (:) bilan tugaydi. Undan keyingi 3 va 4-qatorlar bu tsiklning badani deyiladi.
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 31 Dekabr kuni oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi\n")

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    
    print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)    
print(mehmonlar)

#   for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)

#   for va input()
#  for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)

#       UY ISHI
uyismi = ["Ali","Vali","Hasan","Husan","Olim","Zolim"]
for ism in uyismi:
    print("Salom ", ism)
print("Kod "+str(len(uyismi))+" marta qaytarildi")

uytoq = list(range(11,100,2))
for toqkubi in uytoq:
    print(f"{toqkubi} ning kubi {toqkubi**3} ga teng")
    
kinolar = [] # bo'sh ro'yxat
print("5 ta eng sevimli kinolaringizni kiriting:")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    kinolar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(kinolar)

suhbatdosh_soni = int(input("Bugun nechta odam bilan uchrashganini kiriting:\n>>>"))
suhbatdosh = []
for suhbat in range(suhbatdosh_soni):
    suhbatdosh.append(input(f"{suhbat+1}-suhbatdoshingizni ismini kiriting:\n>>>"))

print(suhbatdosh)