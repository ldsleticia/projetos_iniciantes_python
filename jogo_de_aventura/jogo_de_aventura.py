def iniciar():
    print("A humanidade vive em cidades virtuais")


def escolhe_destino():
    lugar_selecionado = int(
        input(
            "Vocês têm duas opções: entrar na matrix e tentar ajuda ou continuar a busca pelo portal no mundo real. "
            "Digite 0 para matrix ou 1 para mundo real "
        )
    )
    if lugar_selecionado == 0:
        print("Faça uma boa viagem pela matrix")
    elif lugar_selecionado == 1:
        print("Você continua no mundo real, espero que se divirta")
    else:
        print("Você precisa escolher uma opção válida")
