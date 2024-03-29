def autenticacao(usuario, senha):
    if usuario == "admin" and senha == "123":
        return True
    else:
        return False
    
retorno = autenticacao("admin", "123")
if retorno == True:
    print("Acesso autorizado")
else:
    print("Acesso negado")
