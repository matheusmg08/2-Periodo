"""
Faça um programa que leia o nome de 5 pessoas digitados pelo(a) usuário(a) e armazene em uma lista de nomes. No final imprima na tela uma mensagem de Boas Vindas para cada nome armazenado.
Ex:
nomes = ["Turing", "Ada", "Linus", "Dijkstra", "Berners-Lee" ]
Seja bem-vindo(a) Turing
Seja bem-vindo(a) Ada
Seja bem-vindo(a) Linus
Seja bem-vindo(a) Dijkstra
Seja bem-vindo(a) Berners-Lee
"""
nomes = 5
lista_nomes = []
for i in range(nomes):
    tmp = input(f"Digite o {i+1} º nome: ")
    lista_nomes.append(tmp)
print("=" *20)
for y in lista_nomes:
    print(f"Seja bem-vindo {y.upper()} !")
"""
Outra maneira
for x range(len(lista_nomes)):
    print(f"Seja bem-vindo(a) {lista_nomes[x].upper()}")
"""




    


