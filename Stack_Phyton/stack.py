# -*- coding: utf-8 -*-
"""Stack.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17PufjS5WUyM3-V4tidXaaa6yPFjU6si0
"""

tumpukan = [1,2,3,4,5,6,7,8]
print(tumpukan)
 
#memasukan data baru
tumpukan.append(9)
print("data masuk", 9)
print('data sekarang', tumpukan)
 
tumpukan.append(10)
print("data masuk", 10)
print('data sekarang', tumpukan)
 
dataKeluar = tumpukan.pop() # mengeluarkan data yang paling terakhir yaitu 10
print('data yang keluar adalah :',dataKeluar)
print("data terakhir adalah :", tumpukan)
 
# hasil :
# [1, 2, 3, 4, 5, 6, 7, 8]
# data masuk 9
# data sekarang [1, 2, 3, 4, 5, 6, 7, 8, 9]
# data masuk 10
# data sekarang [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# data terakhir adalah [1, 2, 3, 4, 5, 6, 7, 8, 9]