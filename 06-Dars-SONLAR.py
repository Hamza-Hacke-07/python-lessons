# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:04:20 2022

@author: Asomiddinov Hamza Sharofiiddin o'g'li
"""

a = 20  # Sonlar musbat yoko
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)

pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")

a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi

a = 2
b = 3.0
# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))

aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")

PI = 3.14159
raduis = 21.2

x, y, z = 10, -7.25, -30

# ism = 'Jobir'
# yosh = 36
# xabar = ism + ' ' + yosh + ' yoshda'
# print(xabar)

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)

ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz

from datetime import datetime
current_datetime = datetime.now()

#1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#2 foydalanuvchi yoshini xisoblaymiz
yosh = current_datetime.year - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")

#1.1 foydalanuvchining tug'ilgan yilini so'raymiz
t_yil = input("Tug'ilgan yilingizni kiriting: ")
#1.2 t_yil o'zgaruvchini int ga aylantiramiz
t_yil = int(t_yil)
#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2022 - t_yil # 
#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")

#       UY ISHI
istalgan_son = int(input("Istalgan sonni kiriting:\n>>> "))
print(str(istalgan_son) + ' sonining kvadrati ' + str(istalgan_son*istalgan_son) + ' soniga teng')
print(str(istalgan_son) + ' sonining kubi ' + str(istalgan_son*istalgan_son*istalgan_son) + ' soniga teng')

uyyosh = int(input("Yoshingiz nechada?\n>>>"))
print("Siz " + str(current_datetime.year-uyyosh) + " yilda tug'ulgansiz" )

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
aa = str(float(a))
bb = str(float(b))
print( aa + '+' + bb + "=" + str(a+b))
print( aa + '-' + bb + "=" + str(a-b))
print( aa + '*' + bb + "=" + str(a*b))
print( aa + '/' + bb + "=" + str(a/b))