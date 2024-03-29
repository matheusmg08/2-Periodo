segredo = 'CANETAS'.strip() #strip corrige erros de espaços
acertos = []
erros = []
#inicializar a lista
for _ in range(len(segredo)):
    acertos.append('_')
while '_' in acertos:
    chute = input('Qual a letra?').upper()
    posicao = 0
    for letra in segredo:
        if chute == letra.upper():
            acertos [posicao] = chute
        posicao = posicao + 1
    if (chute not in acertos) and (chute not in erros):
        erros.append(chute)
    print(f'Acertos: {acertos}')
    print(f'Erros: {erros}')
    print(f'Vidas = {11- len(erros)}')
    if len(erros) > 10:
        print("Enforcou! game over")
        break
if len(erros) <= 10:
    print('Você acertou a palavra!!!')





