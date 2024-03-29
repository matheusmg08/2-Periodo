## Exercício 03 (Descontos simples)
opcao = 1
while opcao != 5:
    print ("=" *40)
    print ("Menu de opções")
    print ("1- Descobrir o desconto")
    print ("2- Descobrir o tempo")
    print ("3- Descobrir a taxa")
    print ("4- Descobrir o valor nominal")
    print ("5- Fim do programa")
    print ("=" *40)
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print ("=" *40)
        print ("Descobrir o desconto")
        valor_nominal = float(input("Digite o valor nominal: R$"))
        tempo = int(input("Digite o tempo em mês: "))
        taxa = float(input("Digite a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (valor_nominal * taxa * tempo)
        print(f"O valor do desconto é de:R$ {formula:.2f}")
    
    elif opcao == 2:
        print("=" *40)
        print("Descobrir o tempo")
        valor_nominal = float(input("Digite o valor nominal: R$"))
        desconto = float(input("Digite o valor do desconto: R$"))
        taxa = float(input("Digite a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (valor_nominal * taxa)
        formula_final = (desconto / formula)
        print(f"O tempo é de aproximadamente {formula_final:.2f} meses")

    elif opcao == 3:
        print("=" *40)
        print("Descobrir a taxa")
        valor_nominal = float(input("Digite o valor nominal: R$"))
        desconto = float(input("Digite o valor do desconto: R$"))
        tempo = int(input("Digite o tempo em mês: "))
        formula = (valor_nominal * tempo)
        formula_final = (desconto / formula)
        taxa_final = (formula_final * 100)
        print(f"A taxa é de {taxa_final}% ao mês")

    elif opcao == 4:
        print("=" *40)
        print("Descobrir o valor nominal")
        desconto = float(input("Digite o valor do desconto: R$"))
        tempo = int(input("Digite o tempo em mês: "))
        taxa = float(input("Digite a taxa de juros ao mês: "))
        taxa = (taxa / 100)
        formula = (taxa * tempo)
        formula_final = (desconto / formula)
        print(f"O valor nominal é de R${formula_final:.2f}")

    elif opcao == 5:
        print("=" *40)
        print("Fim do programa ...")

