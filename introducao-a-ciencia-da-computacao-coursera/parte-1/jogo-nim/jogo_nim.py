def computador_escolhe_jogada(n, m):
    pecas_removidas = 1
    while pecas_removidas < m and (n - pecas_removidas) % (m + 1) != 0:
        pecas_removidas += 1

    print(
        "O computador tirou",
        pecas_removidas,
        "peças." if pecas_removidas > 1 else "peça.",
    )
    if n > pecas_removidas:
        print("Agora restam", n - pecas_removidas, "peças no tabuleiro.\n")
    else:
        print("Fim do jogo! O computador ganhou!\n")
    return pecas_removidas


def usuario_escolhe_jogada(n, m):
    pecas_removidas = int(input("Quantas peças você vai tirar? "))
    if m > n:
        m = n
    while pecas_removidas < 1 or pecas_removidas > m:
        pecas_removidas = int(
            input("\nOops! Jogada inválida! Tente de novo. ")
        )

    print(
        "\nVocê tirou",
        pecas_removidas,
        "peças." if pecas_removidas > 1 else "peça.",
    )
    if n > pecas_removidas:
        print("Agora restam", n - pecas_removidas, "peças no tabuleiro.\n")
    else:
        print("Parabéns! Você ganhou!")
    return pecas_removidas


def partida():
    total_pecas = int(input("\nQuantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    pecas_removidas = 0
    vencedor = ""

    if total_pecas % (m + 1) == 0:
        print("\nVocê começa!\n")
    else:
        print("\nComputador começa!\n")
        pecas_removidas = computador_escolhe_jogada(total_pecas, m)
        total_pecas -= pecas_removidas

    while total_pecas > 0:
        pecas_removidas = usuario_escolhe_jogada(total_pecas, m)
        total_pecas -= pecas_removidas
        if total_pecas <= 0:
            vencedor = "usuario"
        pecas_removidas = computador_escolhe_jogada(total_pecas, m)
        total_pecas -= pecas_removidas
        if total_pecas <= 0:
            vencedor = "computador"

    return vencedor


def campeonato():
    placar = {"usuario": 0, "computador": 0}
    for x in range(1, 4):
        print("\n**** Rodada {} ****".format(x))
        vencedor = partida()
        placar[vencedor] += 1
    print("\n**** Final do Campeonato ****\n")
    print(
        "Placar: Você",
        placar["usuario"],
        "X",
        placar["computador"],
        "Computador\n\n",
    )


def main():
    print("\nBem-vindo ao jogo do NIM! Escolha: \n")
    tipo_de_jogo = input(
        "1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n\n"
    )

    if tipo_de_jogo == "1":
        partida()
    elif tipo_de_jogo == "2":
        campeonato()


main()
