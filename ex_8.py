# nota final = Grau A + Grau B
# Grau A = 33% da nota final e Grau B = 67% da nota final
# Nota Grau A = atividade prática(45%) + atividade teórica(55%)
# Nota Grau B = prova lab(60%) + teste(20%) + trabalho(20%)

atP = float(input('Digite a sua nota da Atividade Prática do Grau A: '))
atT = float(input('Digite a sua nota da Atividade Teórica do Grau A: '))
grauA = (atP * 0.45) + (atT * 0.55)
print('\nSua nota no Grau A: ', grauA)

provaLab = float(input('\nDigite a sua nota da Prova em Laboratório do Grau B: '))
testeT = float(input('Digite a sua nota do Teste Teórico do Grau B: '))
trab = float(input('Digite a sua nota do Trabalho Extraclasse do Grau B: '))
grauB = (provaLab * 0.6) + (testeT * 0.2) + (trab * 0.2)
print('\nSua nota do Grau B: ', grauB)

notaFinal = (grauA * 0.33) + (grauB * 0.67)

print('\nNota Final: %.2f'% notaFinal)



