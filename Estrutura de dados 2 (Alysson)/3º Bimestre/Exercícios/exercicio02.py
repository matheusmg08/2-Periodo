"""
2- Faça um programa que preencha por leitura um vetor de 10 posições, e conta quantos valores diferentes existem no vetor.
"""
lista = []
for x in range (10):
    valor = int(input("Digite um número: "))
    if valor not in lista:
        lista.append(valor)
print(f'Existem {len(lista)} valores diferentes na lista')



