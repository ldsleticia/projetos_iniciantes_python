from curses.ascii import isdigit
import random

numero_aleatorio = random.randint(1, 6)
print(numero_aleatorio)


def verifica_resposta():
    pass


try:
    while True:
        print()
        resposta = int(input("Qual numero entre 1 e 6 eu pensei? "))
        print()
        if resposta < numero_aleatorio:
            print("Chute muito baixo, aumente um pouco")
        elif resposta > numero_aleatorio:
            print("Chute muito alto, abaixe um pouco")
        elif resposta == numero_aleatorio:
            print("Acertou! Parabéns")
            break
except:
    print("Digite apenas números")
    while True:
        print()
        resposta = int(input("Qual numero entre 1 e 6 eu pensei? "))
        print()
        if resposta < numero_aleatorio:
            print("Chute muito baixo, aumente um pouco")
        elif resposta > numero_aleatorio:
            print("Chute muito alto, abaixe um pouco")
        elif resposta == numero_aleatorio:
            print("Acertou! Parabéns")
            break
