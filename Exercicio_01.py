#Escreva um programa que leia do usuário sua altura e peso e calcule o seu IMC.

altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / (altura**2)
print('Seu IMC é de: {:.1f}'.format(imc))