# -*- coding:utf-8 -*-

print("#-----Vamos calcular as raízes de uma equação do segundo grau -----#")

a = float(input("Digite o coeficiente a= "))

b = float(input("Digite o coeficiente b= "))

c = float(input("Digite o coeficiente c= "))

delta = b ** 2 - 4*a*c

print("delta = ", delta)

raizdelta=delta ** 0.5

print("raiz de delta = ", raizdelta)

x1=(-b+raizdelta)/(2*a)

print("x1 = ", x1)

x2=(-b-raizdelta)/(2*a)

print("x2 = ", x2)
