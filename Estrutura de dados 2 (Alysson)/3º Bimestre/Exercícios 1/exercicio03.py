"""
3- Faça um programa que preencha por leitura um vetor de 5 posições, e informe a posição em que um valor x (lido do teclado) aparece pela primeira vez no vetor. Caso o valor x não seja encontrado, o programa deve imprimir o valor -1
"""
lista = []
for x in range (5):
    vetor = int(input("Digite um valor: "))
    lista.append(vetor)
valor_x = 5
nao_achou = True
for i in range(len(lista)):
    y = lista[i]
    if y == valor_x:
        print (f'O valor 5 aparece no índice: 5{i}')
        nao_achou = False
if nao_achou == True:
        print (f'O valor é -1')

