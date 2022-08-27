#Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.

deposito = int(input('Depósito: '))
juros = float(input('Juros: '))

rendimento = deposito + (deposito * juros/100)

print(deposito, rendimento)