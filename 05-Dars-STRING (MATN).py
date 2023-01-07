# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:38:41 2022

@author: Asomiddinov Hamza Sharofiiddin o'g'li
"""

shahar = "Қўқон"
viloyat = 'Фарғона'

matn = "Men yangi 📱 oldim"
print(matn)

ism = 'Hamza'
familiya = 'Asomiiddnov'
print("Mening ismim " + ism)

print(ism + ' ' + familiya)

#  f-string

ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

#  Maxsus belgilar

print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')

#  STRING Metodlari

print(ism_sharif.upper()) #BARCHA HARHLARNI KATTA QILADI
print(ism_sharif.lower()) #BARCHA HARHLARNI KICHIK QILADI
print(ism_sharif.title()) #BARCHA SO'ZLARNING BIRINCHI HARFINI KATTA QILADI
print(ism_sharif.capitalize()) #BIRINCHI SO'ZNI BIRINCHI SO'ZINI KATTA QILADI

ism_sharif = ism_sharif#.lower #O'ZGARUVCHINI METODGA O'ZGARTIRISH


meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman") # Matn boshidagi bo'shliqni olib tashlaydi
print("Men " + meva.rstrip() + " yaxshi ko'raman") # Matn oxiridagi bo'shliqni olib tashlaydi
print("Men " + meva.strip() + " yaxshi ko'raman")  # Matn boshi va oxiridagi bo'shliqni olib tashlaydi
print("Men " + meva + " yaxshi ko'raman")


# INPUT

#Ism = input("Ismingizni kiriting:")
#print('Assalomu alaykum ' + Ism.title())

#Ism = input("Ismingizni kiriting:\n>>>")
#print('Assalomu alaykum ' + Ism.title())

#       UY ISHI
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha+" ko'chasi, \n"+mahalla+" mahallasi, \n"+tuman+" tumani, \n"+viloyat+" viloyati\n")

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.lower())

kocha2 = input("ko'changizni kiriting:\n>>>")
mahalla2 = input("mahallangizni kiriting:\n>>>")
tuman2 = input("tumaningizni kiriting:\n>>>")
viloyat2 = input("viloyatingizni kiriting:\n>>>")

manzil2 = f"{kocha2} ko'chasi, {mahalla2} mahallasi, {tuman2} tumani, {viloyat2} viloyati"
print(manzil2)