#Forma1
#import exemplo021 as ex
#retorno = exemplo021.autenticacao
#retorno = ex.autenticacao()
#Forma2
from exemplo021 import autenticacao
user = input("Digite login: ")
pwd = input("Digite a senha: ")
retorno = autenticacao(user, pwd)
if retorno == True:
    print("Acesso autorizado")
else:
    print("Acesso negado")

