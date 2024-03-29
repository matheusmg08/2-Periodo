clientes = {}
clientes["000.000.000.00"] = ["Joaquim" , 20]
clientes["111.111.111.11"] = "Tereza"

#recuperar apenas o registro com cpf 111.111.111.11
valor = clientes ["111.111.111.11"]
print (valor)
#recuperar o outro registo
valor = clientes["000.000.000.00"]
print (valor)
#percorrer
chaves = clientes.keys()
print (chaves)
for cpf in clientes.keys():
    print(f"CPF: {cpf}")
    valor = clientes[cpf]
    print (valor)
# outra forma de criar um dicionário
produtos = {"mouse": {"cor:": "preto", "preco": 65.99}, "teclado": {"cor":"branco", "preco": 70}}
produtos ["mouse"] ["cor"]
