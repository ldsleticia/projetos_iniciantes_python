def pula_linha():
    print()


def iniciar():
    print("A humanidade vive em cidades virtuais em aparente harmonia")
    pula_linha()
    print(
        "Infelizmente essa harmonia é só aparente e o destino da humanidade "
        "está em perigo"
    )
    print(
        "Você foi recrutado para um esquadrão especial para descobrir o que está acontecendo e salvar nossa espécie"
    )
    pula_linha()

    while True:
        try:
            aceitar = int(
                input(
                    "Você aceita participar do esquadrão? \n"
                    "Digite 0 para sim e 1 para não "
                )
            )
            if aceitar == 0:
                pula_linha()
                print(
                    "Obrigada por aceitar a missão, contamos com você para nossa salvação"
                )
                return escolhe_destino()
                break
            elif aceitar == 1:
                pula_linha()
                print(
                    "Sua memória será apagada e você não se lembrará no nosso contato"
                )
                break
            else:
                pula_linha()
                print("Escolha inválida")
                break
        except ValueError:
            print("Digite apenas números")


def escolhe_destino():
    lugar_selecionado = int(
        input(
            "Você têm duas opções: entrar na matrix e tentar ajuda ou continuar a busca pelo portal no mundo real. \n"
            "Digite 0 para matrix ou 1 para mundo real "
        )
    )
    if lugar_selecionado == 0:
        pula_linha()
        print("Faça uma boa viagem pela matrix")
        return primeiro_encontro_matrix()
    elif lugar_selecionado == 1:
        pula_linha()
        print("Você continua no mundo real, espero que se divirta")
        primeiro_encontro_mundo_real()
        return
    else:
        return "Você precisa escolher uma opção válida"


def primeiro_encontro_matrix():
    pula_linha()
    print("Você encontrou um desconhecido que diz poder te ajudar")
    confiar = int(
        input(
            "Deseja confiar no desconhecido? \n "
            "Digite 0 para confiar e 1 para ignorar "
        )
    )


def primeiro_encontro_mundo_real():
    pula_linha()
    print(
        "Você encontra um vilarejo aparentemente abandonado. \n" "e decide inspecionar"
    )
    contato = int(
        input(
            "Inspecionando a cidade, você se depara com alguns humanos modificados. \n"
            "Tenta contato com eles ou apenas passam pelo vilarejo? \n"
            "Digite 0 para contato ou 1 para passar direto "
        )
    )


iniciar()
