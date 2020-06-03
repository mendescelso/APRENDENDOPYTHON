## Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

nota1 = int(input('Digite a primeira nota '))
nota2 = int(input('Digite a segunda nota '))
notas = nota1+nota2
media = notas/2
if media >=6:
    print('Você foi aprovado ')
else:
    print('Você não foi aprovado ')


