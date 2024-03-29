"""
4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos.
"""
import random
lista = []
lancamentos = 50
face = 6
tmp = 0
for x in range(lancamentos):
    vetor = random.randint(1,6)
    lista.append(vetor)
            
for y in lista:
    if y == 6:
        tmp += 1

percentual = (tmp / lancamentos) *100
print(f'O número 6, aparece {tmp} vezes, e a porcentagem é {percentual:.1f}%')


