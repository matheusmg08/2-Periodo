#Estrutura de dados
notas = [8.0,5.5,6.5]
#print (notas[1])
#tam = len(notas)
#print(tam)
media = (notas[0] + notas[1] + notas[2]) /3
print(f"Média: {media:.2f}")

media2 = (notas[0] + notas[1] + notas[2]) /len(notas)
print(f"Média: {media:.2f}")
print("=" *60)

#Exemplo2
notas3 = [8.0,5.5,1.5,9,10]
soma = 0
for indice in range(len(notas3)):
    print(indice, end='>>>>')
    print(notas3[indice])
    soma = soma + (notas3[indice])
media = soma / len(notas3)
print(f"A média é: {media}")










