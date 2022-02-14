import random

while True:
    print()
    pergunta = input(
        "Voce quer continuar rolando os dados? Caso não queira, digite não "
    )
    print()
    valor_aleatorio = random.randint(1, 6)
    print(f"valor gerado foi {valor_aleatorio}")
    if pergunta == "não" or pergunta == "Não" or pergunta == "nao" or pergunta == "Nao":
        break
