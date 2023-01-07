# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:10:03 2023

@author: Asomiddinov Hamza Sharofiiddin o'g'li
"""

#   TARMOQLANISH
#  Shu vaqtgacha yozgan dasturlarimizga e'tibor bersangiz, dasturimiz yuqoridan pastga qarab qatorma-qator bajarilib keldi. Bu chiziqli dastur deyiladi. Voqelikda esa aksar dasturlar ma'lum bir shart bajarilishi (yoki bajarilmaganiga) ko'ra kodning bir qismidan boshqa qismiga "sakrab" o'tishi tabiiy hol. Dasturlashda bu tarmoqlanish deb ataladi. 

#   if OPERATORI
#  Ushbu darsimizda biz if operatori yordamida shunday shartlarni yozishni, tekshirishni va tekshiruv natijasiga ko'ra kodning turli qismlarini bajarishni o'rganamiz. 
avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
        
ism = 'Ali'
ism.lower() == 'ali'

ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")
    
javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")
else:
    print("Javob to'g'ri")

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=20: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')

login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")

from datetime import datetime
current_datetime = datetime.today()

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if current_datetime.year-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")

#   BIR QATOR if/else

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")

#       UY ISHI

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
cars != "gm"

uylogin = input("login kiriting:")
if uylogin.lower() == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {uylogin}")

ason = input("Birinchi sonni kiriting:")
bson = input("Birinchi sonni kiriting:")
if ason==bson :
    print("Sonlar teng")

uyson = int(input("Istalgan sonni kiriting:"))
if uyson<0 :
    print("Manfiy son")
else:
    print("Musbat son")

uymusbat = int(input("Son kiriting:"))
if uymusbat >0:
    print(uymusbat**0.5)
else:
    print("Musbat son kiriting")
