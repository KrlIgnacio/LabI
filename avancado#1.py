a = float(input('Armazene um valor float em A:'))
b = float(input('Armazene um valor inteiro em B:'))

opM = a * b
opD = a / b
opSoma = a + b
opSub = a - b
opPot = a ** b

print(a, 'multiplicado por',b, 'é', '%.2f' %opM)
print(a, 'dividido por',b, 'é', '%.2f' %opD)
print(a, 'mais',b, 'é', '%.2f' %opSoma, 'e', a, 'menos', b, 'é', '%.2f' %opSub)
print(a, 'elevado a', b, 'é', '%.2f' %opPot)