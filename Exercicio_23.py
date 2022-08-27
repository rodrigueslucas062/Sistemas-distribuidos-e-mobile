#Faça um programa que receba o salário base de um funcionário, calcule e mostre seu salário a receber, sabendo-se que o funcionário tem gratificação de R$ 50,00 e paga imposto de 10% sobre o salário base.

salario = int(input('Salário: '))

gratificação = salario + 50.0
imposto = salario * 0.1

bolsa = gratificação - imposto

print(bolsa)