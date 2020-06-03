## Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal. 


# -*- coding: utf-8 -*-

"""
Calculadora
Autor: Celso
Função: Fazer contas: Soma, divisão, multiplicação e subtração.
"""
print ("CALCULADORA V2.0")
sair = False

while sair == False:

	num1 = input ("Digite o primeiro número ")
	num1 = int(num1)
	operador = input ("Digite o operador +, -, / ou *: ")
	num2 = input ("Digite o segundo número ")
	num2 = int(num2)
	# + soma

	if operador == "+":
		operacao = num1 + num2
	# -  subtração
	if operador == "-":
		operacao = num1 - num2
	#  / divisão
	if operador == "/":
		operacao = num1 / num2
	# * multiplicação
	if operador == "*":
		operacao = num1 * num2

	print ("O resultado é: ")
	print (operacao)

	teste = input ("Deseja sair (n/s): ")
	if teste == "s":
		sair = True
