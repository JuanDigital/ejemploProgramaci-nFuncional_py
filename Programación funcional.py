#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:47:37 2021

@author: juandigital
"""

lista= range(5)
for i in lista:
    print(i)
    
#listas por comprención

listaMultiplicadaPor1000=[j*1000 for j in range (10)]
print(listaMultiplicadaPor1000)

#regresa dos elementos

listaM=[(k,k*1000,k*k) for k in range (10)]
print(listaM)

#entscheidungsproblem
#calculo lambda
#función tipo lambda

multiplica= lambda a,b: a*b
resultado=multiplica(2, 5)
print('lambda',resultado)
    