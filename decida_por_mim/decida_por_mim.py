import random

frases = [
    "Só vai",
    "Não acho boa ideia",
    "Talvez dê certo",
    "Talvez dê errado",
    "Não julgo",
    "Não julgo, faria o mesmo",
    "Não julgo mas não faria o mesmo",
    "Ouvi dizer que isso não é bom",
    "Ouvi dizer que isso é bom",
    "Gosto de você, mas as vezes você me irrita",
    "Você realmente acha que daria certo?",
    "É meu jeito ninja de ser",
    "O fracasso não é razão para você desistir, desde que continue acreditando",
    "As coisas mais importantes não estão escritas num livro, é preciso aprendê-las vivenciando-as sozinho",
]

while True:
    try:
        resposta = input(
            "Me pergunte o que quiser e te darei uma resposta. Se quiser sair do nosso bate papo, digite sair "
        )
        if resposta == "sair" or resposta == "Sair":
            print("Obrigada por jogar comigo")
        # elif resposta:
        #     print(random.choices(frases))
    except ValueError:
        print(42)
