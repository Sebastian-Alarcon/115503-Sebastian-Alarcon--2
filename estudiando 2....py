# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 08:13:18 2019

@author: USUARIO
"""


 # COORDENADAS DE UN CIRCULO [9]
"""Hacer un programa que lea las coordenadas (x1,y1,r1) y (x2,y2,r2)\
 que corresponden al centro y al radio de dos círculos """
 
import math

x1=(int)(input('(circulo número 1)introduzca la coordenada en x: '))
y1=(int)(input('(circulo número 1)introduzca la coordenada en y: '))
r1=(int)(input('(circulo número 1)introduzca el radio: '))

x2=(int)(input('(circulo número 2)introduzca la coordenada en x: '))
y2=(int)(input('(circulo número 2)introduzca la coordenada en y: '))
r2=(int)(input('(circulo número 2)introduzca el radio: '))

a=(int)(input('coord en a: '))
b=(int)(input('coord en b: '))

di1=math.sqrt((x1-a)**2+(y1-b)**2)
di2=math.sqrt((x2-a)**2+(y2-b)**2)

cont=0
if (di1<=r1):
    print('(a,b) esta en el circulo 1')
    cont=cont+1
else:
    print('(a,b) no esta en el circulo 1')
if (di2<=r2):
    print('(a,b) esta en el circulo 2')
    cont=cont+1
else:
    print('(a,b) no esta en el circulo 2')
if (cont==2):
    print('(a,b) esta en los dos circulos')
if (cont==0):
    print('(a,b) no esta en ninguno de los dos circulos')
    
#%%          MATRIZ [20]  
    
m=[]
mat=[]
l=[]
li=[]
filas = int(input("Cantidad de Filas:"))
columnas= int(input("Cantidad de Colomnas:"))

for i in range (filas):
    m.append([0]*columnas)
    mat.append([0]*columnas)
for j in range (filas):
    for c in range(columnas):
         m[c][j] = int(input("Elemento %d,%d:"%(j,c)))
         mat[j][c] = m[c][j]
       
print("Matriz ingresada:",mat)
print("Matriz girada 90 grados:",m)
      
#%%     NUMEROS ORENADOS EN LISTA [17]

lista=[]
lix=[]
lis=[]
numero=(int)(input("digite los elementos de la lista "))
num=int(((numero)**2)**0.5)
conteo=0
while(num>=10):
    residuo=num%10
    lista.append(residuo)
    num=num//10
    conteo=conteo+1
lista.append(num)   


for i in range(1,len(lista)):
    for j in range (len(lista)-i):
        if lista[j]>lista[j+1]:
            x = lista[j]
            lista[j] = lista[j+1]
            lista[j+1]= x
print("Los numeros ordenados son",lista)   

lista_copia = list(lista)
for i in lista_copia:
    if i  not in lis:
        lis.append(i)

(print("la lista si los números repetidos es:",lis))
print("El segudo número más grande es: ",lis[-2])      

#%%       REPETICION DE NUMEROS [15]

c=(int)(input('Cantidad de digitos son ')) 
lista=[] # se guerda la cantidad de elementos a instrudicr por cad
for i in range(c):
    lista.append(input('introduzca el numero'+str(i+1)+':'))

lis=[]
for i in range(len(lista)):#itera para reconocer las veces que se repite 2 
    #un numero
    a=lista.count(lista[i])
    if (a==2):
        cadena='el numero '+lista[i]+' se repite 2 veces en la lista'
        if cadena not in lis:
            lis.append(cadena)
            print('entra')
            
for i in range(len(lis)):
    print(lis[i])
    