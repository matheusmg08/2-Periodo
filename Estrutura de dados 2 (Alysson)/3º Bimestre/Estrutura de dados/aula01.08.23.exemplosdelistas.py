"""
Exemplos de Listas (Vetor(array))
Listas (são estruturas dinâmicas, aumenta ou diminui de tamanho de acordo com dados armazenados)
Vetor (mantém o tamanho fixo, porém o Python não tem Vetor estático
"""
numeros = [1,4,9,16,25]
numeros[1] = 6
#print(numeros[1])
#consultar o último elemento
print(numeros[-1])
#outra forma
print(numeros[len(numeros)-1])
#união de listas
outra_lista = [36,49,64,]
nova_lista = numeros + outra_lista
print(nova_lista)
#adicionar novos elementos na lista
nova_lista.append(9*9)
print(nova_lista)
#corrigir o elemento da posição 1
nova_lista[1] = 2**2
print(nova_lista)
#percorrer a lista exibindo apenas os valores
for valor in nova_lista:
    print(valor)
#trazer o indice e valor
for indice in range(len(nova_lista)):
    valor = nova_lista[indice]
    print(f'Indice = {indice}, valor = {valor}')
#outra forma de trazer indice e valor
for indice, valor in enumerate(nova_lista):
    print(f'Indice = {indice}, valor = {valor}')
    





