# calculo de nota final
# trabalho = 10% da nota final
# prova = 60% da nota final
# teste = 30 % da nota final

notaTrab = float(input('Digite a sua nota do trabalho: '))
notaProva = float(input('Digite a sua nota da prova: '))
notaTeste = float(input('Digite a sua nota do teste: '))

notaFinal = (notaTrab * 0.1) + (notaProva * 0.6) + (notaTeste * 0.3)

print("Sua nota final é: ", notaFinal)