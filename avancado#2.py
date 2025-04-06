# formula de Báskara
# calcular o delta
# x1 é raiz positiva
# x2 é a raiz negativa

a = float(input('Digite um valor para A:'))
b = float(input('Digite um valor para B:'))
c = float(input('Digite um valor para C:'))

delta = (b**2) - 4*a*c

if a == 0:
    print('O valor de A deve ser diferente de zero!')
    
elif delta < 0:
    print('Não existe raiz real.')
    
elif delta == 0:
    x1 = -b / (2*a)
    print('Raiz: ', x1)
    
else:
    delta = delta ** (1/2)
    x1 =(-b + delta) / (2*a)
    x2 = (-b - delta) / (2*a)
    print('Raiz positiva: ', x1)
    print('Raiz negativa: ', x2)