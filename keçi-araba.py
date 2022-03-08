# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from operator import truediv
import random
import math



b=int(input("kaçıncı kapıyı seçiyorsunuz"))
def sabit(kapı):
    a=int(0)
    sabit_olasılık=float(0)
    kapilar=[]
    degerler=["Goat","Goat","car"]
    kapilar=degerler
    
    for i in range(0, 1000):
        kapilar=random.sample(kapilar,3)
        print(kapilar)
        acikmi=None
        
        if kapilar[b]!="car":
          acikmi=False
        else:
          acikmi=True
          a+=1
        pass
    
    sabit_olasılık=(a/10)
    print("kazanma şansınız%" +str(sabit_olasılık))
    
    
    
    
def change(kapı):
    a=int(0)
    değişken_olasılık=float(0)
    kapilar=[]
    degerler=["Goat","Goat","car"]
    kapilar=degerler
    
    for i in range(0, 1000):
        kapilar=random.sample(kapilar,3)
        print(kapilar)
        acikmi=None
        
        if kapilar[b]=="car":
            acikmi=False
        elif kapilar[b]=="Goat":
            acikmi=True
            a+=1
        pass 
        
    değişken_olasılık=(a/10)
    print("kazanma şansınız%" +str(değişken_olasılık))      
            
            
change(b)

