print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total = 3
rodada = 1

while (rodada <= total):
    print(f'Tentativa {rodada} de {total}')
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
     if (maior):
        print('Chute maior que o número!')
     elif (menor):
        print('Chute menor que o número!')

    rodada = rodada + 1