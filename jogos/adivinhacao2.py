import random

def jogar():
    
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2)Médio (3)Difícil")

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total = 3
    elif (nivel ==2):
        total = 2
    else:
        total = 1

    numero_secreto = round(random.randrange(1,100))
    pontos = 1000


    for rodada in range(1, total + 1):
        print(f'Tentativa {rodada} de {total}')
        chute_str = input("Digite o seu número: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100.')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if (maior):
             print('Chute maior que o número!')
            elif (menor):
             print('Chute menor que o número!')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print(f'O número secreto é {numero_secreto}')

