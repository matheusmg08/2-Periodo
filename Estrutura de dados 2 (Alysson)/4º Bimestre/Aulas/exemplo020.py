def a():
    print("inicio A")
    for i in range (5):
        print(f"A: {i}")
    print("fim A")
    return None
def b():
    print("Função b")
    print ("B1 e B2")
    print("Fim b")

print("Inicio main") #main principal
a() #chamar a função A
print("Invocar a função a() novamente")
a()
print("Fim main")

