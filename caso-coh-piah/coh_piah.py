import re


def le_assinatura():
    """
    A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos
    """
    print("\nBem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre com o tamanho médio de palavra: "))
    ttr = float(input("Entre com a relação Type-Token: "))
    hlr = float(input("Entre com a Razão Hapax Legomana: "))
    sal = float(input("Entre com o tamanho médio de sentença: "))
    sac = float(input("Entre com a complexidade média da sentença: "))
    pal = float(input("Entre com o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """
    A funcao le todos os textos a serem comparados e devolve
    uma lista contendo cada texto como um elemento
    """
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input(
            "\nDigite o texto " + str(i) + " (aperte enter para sair): "
        )

    return textos


def separa_sentencas(texto: str):
    """
    A funcao recebe um texto e devolve uma
    lista das sentencas dentro do texto
    """
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca: str):
    """
    A funcao recebe uma sentenca e devolve
    uma lista das frases dentro da sentenca
    """
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase: str):
    """
    A funcao recebe uma frase e devolve
    uma lista das palavras dentro da frase
    """
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e
    devolve o numero de palavras que aparecem uma unica vez
    """
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e
    devolve o numero de palavras diferentes utilizadas
    """
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """
    Essa funcao recebe duas assinaturas de texto e deve
    devolver o grau de similaridade nas assinaturas.
    """
    QTD_DE_SIMILARIDADES = 6
    soma = 0
    for item_a, item_b in zip(as_a, as_b):
        soma += abs(item_a - item_b)
    return soma / QTD_DE_SIMILARIDADES


def calcula_assinatura(texto: str):
    """
    Essa funcao recebe um texto e deve devolver a assinatura do texto.
    """
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    soma_tamanho_sentenca = 0
    for sentenca in sentencas:
        soma_tamanho_sentenca += len(sentenca)
        frases.extend(separa_frases(sentenca))

    soma_tamanho_frase = 0
    for frase in frases:
        soma_tamanho_frase += len(frase)
        palavras.extend(separa_palavras(frase))

    soma_tamanho_palavras = 0
    for palavra in palavras:
        soma_tamanho_palavras += len(palavra)

    total_de_palavras = len(palavras)
    total_de_frases = len(frases)
    total_de_sentencas = len(sentencas)

    tamanho_medio_palavra = soma_tamanho_palavras / total_de_palavras
    tamanho_medio_sentenca = soma_tamanho_sentenca / total_de_sentencas
    complexidade_sentenca = total_de_frases / total_de_sentencas
    tamanho_medio_frase = soma_tamanho_frase / total_de_frases
    relacao_type_token = n_palavras_diferentes(palavras) / total_de_palavras
    razao_hapax_legomana = n_palavras_unicas(palavras) / total_de_palavras

    return [
        round(tamanho_medio_palavra, 3),
        relacao_type_token,
        razao_hapax_legomana,
        tamanho_medio_sentenca,
        complexidade_sentenca,
        tamanho_medio_frase,
    ]


def avalia_textos(textos, ass_cp):
    """
    Essa funcao recebe uma lista de textos e uma assinatura ass_cp
    e deve devolver o numero (1 a n) do texto com maior probabilidade
    de ter sido infectado por COH-PIAH.
    """
    ass = calcula_assinatura(textos[0])
    maior_similaridade = compara_assinatura(ass, ass_cp)
    texto_infectado = 1

    for numero_texto, texto in enumerate(textos, 1):
        ass = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass, ass_cp)
        if similaridade < maior_similaridade:
            maior_similaridade = similaridade
            texto_infectado = numero_texto

    return texto_infectado


def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, ass_cp)
    print(
        f"\nO autor do texto {texto_infectado} está infectado com COH-PIAH\n"
    )


if __name__ == "__main__":
    main()
