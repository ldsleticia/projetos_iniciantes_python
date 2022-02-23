import random

numero_aleatorio = random.randint(1, 6)
resposta = 0

while resposta != numero_aleatorio:
    try:
        print()
        resposta = int(input("Qual numero entre 1 e 6 eu pensei? "))
        print()
        if resposta < numero_aleatorio:
            print("Chute muito baixo, aumente um pouco")
        elif resposta > numero_aleatorio:
            print("Chute muito alto, abaixe um pouco")
        else:
            print("Acertou! Parabéns")
    except:
        print("Digite apenas números")
