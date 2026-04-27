semestre = 1

while semestre <= 2:
    print(f"Notas do {semestre} semestre")
    semestre += 1

    #Colocando valor
    cp1 = float(input("Insira a nota do checkpoint 1: "))
    cp2 = float(input("Insira a nota do checkpoint 2: "))
    cp3 = float(input("Insira a nota do checkpoint 3: "))
    sp1 = float(input("Insira a nota da sprint 1: "))
    sp2 = float(input("Insira a nota da sprint 2: "))
    gs = float(input("Insira a nota da global solution: "))

    #Media
    if cp1 <= cp2 and cp1 <= cp3:
        menor_cp = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor_cp = cp2
    else:
        menor_cp = cp3

    media = ((cp1 + cp2 + cp3 + sp1 + sp2 - menor_cp) / 4) * 0.4 + gs * 0.6
    media_peso = media * 0.4
    print(f"O valor da média com peso é de {media_peso:.1f}")
    print(f"O valor da média sem peso é de {media:.1f}")