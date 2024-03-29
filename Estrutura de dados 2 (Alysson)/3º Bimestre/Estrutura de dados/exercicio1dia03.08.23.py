"""
Crie duas listas em python, uma para armazenar o nome e outra lista para armazenar a idade de 5 pessoas. Posteriormente indique mais pessoas que tem 18 anos ou mais e quanto pessoas são menores de idade.
Ex:
José, 10 anos
Joaquim, 19 anos
Jailton, 30 anos
Juarez, 5 anos
João, 18 anos
--> são maiores de idade: Joaquim, Jailton, Joao
--> são menores de idade: Jose, Juarez
"""
nomes = []
idades = []
for i in range(5):
    nomes.append(input("Digite o nome: "))
    idade = int(input(f"Digite a idade de {nomes[i]}: "))
    idades.append(idade)


maiores = "--> São maiores de idade: "
menores = "--> São menores de idade: "
for j in range(len(idades)):
    if idades[j] >= 18:
        tmp = nomes[j]
        maiores = maiores + tmp + ", "
    else:
        tmp = nomes[j]
        menores = menores + tmp + ", "
print(maiores)
print (menores)










