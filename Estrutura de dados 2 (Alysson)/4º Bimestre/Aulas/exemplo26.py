def sem_parametros():
    #sem retorno
    print("Comando 1")
    for i in range(10):
        print(i)
    print("Comando 2")

def sem_parametros_com_retorno():
    print("Comando 3")
    valor = input("Digite s ou n: ")
    if valor == "s":
        return 100
    
    print("Comando 4")

def com_parametro_sem_retorno(valor1, valor2):
    #função vai comparar de valor1 == valor2
    if valor1 == valor2:
        return "São iguais"
    else:
        return "São diferentes"

if __name__== "__main__":
    print("Inicio")
    #sem parametros() #a função vai ser chamada (invocada)
    #numero = sem_parametros_com_retorno()
    #print("Depois da chamada da função")
    #print(numero)
    auxiliar = sem_parametros_com_retorno("chapeuzinho vermelho", "chapeuzinho")
    print(auxiliar)
