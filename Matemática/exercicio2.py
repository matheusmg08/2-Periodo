## Exercício 02 (Juros compostos e montante composto)
import math
opcao = 1
while opcao != 5:
    print ("=" *40)
    print("Menu de opções")
    print("1- Descobrir o montante")
    print("2- Descobrir o tempo")
    print("3- Descobrir o capital")
    print("4- Descobrir a taxa")
    print("5- Fim do programa")
    print("=" *40)
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("=" *40)
        print("Descobrir o montante")
        capital = float(input("Informe o valor do capital: "))
        tempo = float(input("Informe o tempo em mês: "))
        taxa = float(input("Informe a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (1 + taxa) ** tempo
        montante = (capital * formula)
        juros = (montante - capital)
        print (f"O valor do montante é de:R$ {montante:.2f}")   
        print (f"O valor do juros é de:R$ {juros:.2f}")

    elif opcao == 2:
        print("=" *40)
        print("Descobrir o tempo")
        capital = float(input("Informe o valor do capital: "))
        montante = float(input("Informe o valor do montante: "))
        taxa = float(input("Informe a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (1 + taxa)
        formula_1 = (montante / capital)
        resultado = math.log(formula_1) / math.log(formula)
        juros = (montante - capital)
        print(f"O tempo é de {resultado:.2f} meses")
        print (f"O valor do juros é de:R$ {juros:.2f}")

    elif opcao == 3:
        print("=" *40)
        print("Descobrir o capital")
        tempo = float(input("Informe o tempo em mês: "))
        montante = float(input("Informe o valor do montante: "))
        taxa = float(input("Informe a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (1 + taxa) ** tempo
        formula_1 = (montante / formula)
        juros = (montante - formula_1)
        print(f"O capital é de:R$ {formula_1:.2f}")
        print (f"O valor do juros é de:R$ {juros:.2f}")

    elif opcao == 4:
        print("=" *40)
        print("Descobrir a taxa")
        montante = float(input("Informe o valor do montante: "))
        tempo = float(input("Informe o tempo em mês: "))
        capital = float(input("Informe o valor do capital: "))
        formula = (montante / capital)
        resultado = formula ** (1/tempo)
        resultado_final = (resultado - 1)
        taxa_final = (resultado_final * 100)
        print(f"A taxa é de {taxa_final:.0f}% ao mês")

    elif opcao == 5:
        print("Fim do programa...")




