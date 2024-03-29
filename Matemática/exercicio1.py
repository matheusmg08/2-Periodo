## Exercício 01 (Juros simples e montante simples)
opcao = 1
while opcao != 5:
    print ("=" *40)
    print("Menu de opções")
    print("1- Descobrir o capital")
    print("2- Descobrir o tempo")
    print("3- Descobrir o juros")
    print("4- Descobrir a taxa")
    print("5- Fim do programa")
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("=" *40)
        print("Descobrir o capital")
        tempo = float(input("Informe o tempo em mês: "))
        taxa = float(input("Informe a taxa de juros ao mês: "))
        juros = float(input("Informe o valor do juros: "))
        taxa = (taxa / 100)
        formula = (taxa * tempo)
        formula_final = (juros / formula)
        montante = (formula_final + juros)
        print (f"O valor do capital é de:R$ {formula_final:.2f}")
        print (f"O valor do montante é de:R$ {montante:.3f}")    
        
    elif opcao == 2:
        print("=" *40)
        print("Descobrir o tempo")
        juros = float(input("Informe o valor do juros: "))
        capital = float(input("Informe o valor do capital: "))
        taxa = float(input("Informe a taxa de juros em mês: "))
        taxa = (taxa / 100)
        formula = (capital * taxa)
        formula_final = (juros / formula)
        montante = (capital + juros)
        print (f"O tempo é de: {formula_final:.2f} meses")
        print (f"O valor do montante é de:R$ {montante:.3f}")

    elif opcao == 3:
        print("=" *40)
        print("Descobrir o valor do juros")
        capital = float(input("Informe o valor do capital: "))
        tempo = float(input("Informe o tempo em mês: "))
        taxa = float(input("Informe a taxa de juros em mês: "))
        taxa = (taxa / 100)
        formula = (capital * taxa * tempo)
        montante = (formula + capital)
        print (f"O valor do juros é de: R${formula:.2f}")
        print (f"O valor do montante é de:R$ {montante:.3f}")

    elif opcao == 4:
        print("=" *40)
        print("Descobrir a taxa de juros")
        juros = float(input("Informe o valor do juros: "))
        capital = float(input("Informe o valor do capital: "))
        tempo = float(input("Informe o tempo em mês: "))
        formula = (capital * tempo)
        formula_final = (juros / formula)
        print (formula_final)
        taxa_final = (formula_final * 100)
        montante = (juros + capital)
        print (f"A taxa de juros é de {taxa_final}% ao mês")
        print (f"O montante é de:R$ {montante:.3f}")
    else:
        print("=" *40)
        print("Fim do programa...")








    


        
