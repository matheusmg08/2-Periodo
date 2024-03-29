#criar uma matriz N X M preenchidas com zeros
#N equivale ao número de linhas
#M eaquivale ao número de colunas
# E imprimir na forma de matriz
#N = 5
#M = 4
n = 5
m = 4
matriz = []
for linha in range(n):
    matriz.append([0] *m)
    #matriz.append([0,0,0,0])

print("---------------")
for linha in range(n):
    for coluna in range(m):
        print(matriz[linha][coluna], end='\t')
    print()

#Adicione elementos de forma aleatória em uma matriz NXM e retorne e quantidade de numeros pares!
import random
n = 5
m = 4
pares = 0
matriz_sorteado = []
for linha in range(n):
    sorteado = random.randint(1,100)
    matriz_sorteado.append([sorteado] *m)  
    print (matriz_sorteado)
   



   


