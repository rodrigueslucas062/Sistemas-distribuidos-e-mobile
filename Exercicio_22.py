#Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário tem gratificação de 5% sobre o salário base e paga imposto de 7% também sobre o salário base.

salario = int(input('Salário: '))

gratificação = salario * 0.05
imposto = salario * 0.07

bolsa = salario + gratificação - imposto

print(bolsa)