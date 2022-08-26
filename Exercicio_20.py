#Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%.

salario = int(input('Salário: '))

reajuste = salario * 0.25 + salario

print(reajuste)