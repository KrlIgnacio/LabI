# area triangulo = (base x altura)/2 - var B e C
# perimetro retangulo = 2 X (base + altura) - var A, B, C e D
# area circulo = area = 3,14 x E^2

a = int(input("Digite o valor da variável A: "))
b = int(input("Digite o valor da variável B: "))
c = int(input("Digite o valor da variável C: "))
d = int(input("Digite o valor da variável D: "))
e = int(input("Digite o valor da variável E: "))

areaT = (b * c) / 2
print('A área de um triângulo com base ',b, 'e altura', c, 'é igual a: ', areaT)

base = a + b
altura = c + d
perimetroR = 2 * (base + altura)
print('O perímetro de um retângulo com base ',base, 'e altura', altura, 'é igual a: ', perimetroR)

areaC = float
areaC = 3.14 * (e **2)
print('A área de um círculo com raio ',e, 'é igual a: ', areaC)
