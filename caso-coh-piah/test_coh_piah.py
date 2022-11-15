
from coh_piah import calcula_assinatura
from data import ass_lista, textos


def test_function_calcula_assinatura_tamanho_medio_palavra():
    for ass, texto in zip(ass_lista, textos):
        ass_received = calcula_assinatura(texto)
        assert isinstance(ass_received, list)
        assert ass_received[0] == ass[0]


def test_function_calcula_assinatura_completo():
    ass_received = calcula_assinatura(textos[3])
    assert ass_lista[3] == ass_received
