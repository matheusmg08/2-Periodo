"""
Armazenar as notas de 10 alunos em uma lista. A
nota de cada aluno será informada pelo teclado.
"""
n_alunos = 10
notas = []
for i in range(n_alunos):
    aluno = float(input(f"Me informe a nota: "))
    notas.append(aluno)
print(f'As notas foram {notas}!')
#Função (sum) faz a soma dos valores presentes na lista, e (len) devolve a quantidade de valores presentes na lista
media = sum(notas)/len(notas)
print(f"Média final: {media}")













