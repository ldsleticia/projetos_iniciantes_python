import random

numero_aleatorio = random.randint(1, 6)
pergunta = input("Qual numero entre 1 e 6 eu pensei? ")

while True:
    if pergunta == numero_aleatorio:
        print("Acertou! Parabéns")
    elif pergunta < numero_aleatorio:
        print("Chute muito baixo, aumente mais um pouco")
    else:
        print("Chute muito alto, desça um pouco")
