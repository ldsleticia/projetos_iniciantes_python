import random

while True:
    print()
    pergunta = input(
        "Voce quer continuar rolando os dados? Digite sim para continuar ou não se quiser parar o jogo "
    )
    print()
    if pergunta != "sim" and pergunta != "nao":
        print("Não entendi o que voce disse, por favor insira uma entrada correta")
    elif (
        pergunta == "não" or pergunta == "Não" or pergunta == "nao" or pergunta == "Nao"
    ):
        print("Obrigada por jogar com nossos dados")
        break
    else:
        valor_aleatorio = random.randint(1, 6)
        print(f"valor gerado foi {valor_aleatorio}")
    if pergunta == "não" or pergunta == "Não" or pergunta == "nao" or pergunta == "Nao":
        print("Obrigada por jogar com nossos dados")
        break
