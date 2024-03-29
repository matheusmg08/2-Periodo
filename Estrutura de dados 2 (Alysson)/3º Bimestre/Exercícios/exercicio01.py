"""
1- Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
"""
print('A:')
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]
maior = max(lista)
print(f"O maior elemento é: {maior}")
print("-" *50)
print('B:')
menor = min(lista)
print(f"O menor elemento é {menor}")
print("-" *50)
print('C:')
pares = "Os números pares são: "
for x in lista:
    if x % 2 == 0:
        x = str(x)
        pares = pares + x + " ,"
print(pares[:-2])
print("-" *50)
print("D:")
tmp = 0
for x in lista:
    if x == 12:
        tmp += 1
print(f"O número {lista[0]} aparece {tmp} vezes")
print("-" *50)
print("E:")
soma = 0
for x in lista:
    soma = soma + x
    media = soma / (len(lista))
print(f"A média é {media:.2f}")
print ("-" *50)
print("F:")
soma = 0
for x in lista:
    if x < 0:
        soma = soma + x
print(f'A soma entre os elementos negativos é: {soma}')



