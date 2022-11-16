def sao_multiplicaveis(m1, m2):
    cols_m1 = len(m1[0])
    lines_m2 = len(m2)
    if cols_m1 == lines_m2:
        return True
    else:
        return False
