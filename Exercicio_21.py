#Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.

salario = int(input('Salário: '))
aumento = float(input('% de aumento: '))

reajuste = salario * aumento

print(reajuste)