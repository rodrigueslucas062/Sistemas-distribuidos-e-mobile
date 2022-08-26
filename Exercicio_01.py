altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura**2)
print('Seu IMC é de: {:.1f}'.format(imc))