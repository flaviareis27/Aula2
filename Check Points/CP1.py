# colocando valor
cp1 = float(input("Ensira o valor do checkpoint 1: "))
cp2 = float(input("Ensira o valor do checkpoint 2: "))
cp3 = float(input("Ensira o valor do checkpoint 3: "))
sp1 = float(input("Ensira o valor do sprint 1: "))
sp2 = float(input("Ensira o valor do sprint 2: "))
gs = float(input("Ensira o valor do gs: "))

# menor cp
menor_cp = cp1
if cp2 <= cp1 and cp2 <= cp3:
    menor_cp = cp2
if cp3 <= cp2 and cp3 <= cp1:
    menor_cp = cp3

# media
media = ((cp1 + cp2 + cp3 + sp1 + sp2 - menor_cp) / 4) * 0.4 + gs * 0.6
media_peso = media * 0.4
print(f"O valor da média com peso é de {media_peso:.2f}")
print(f"O valor da média sem peso é de {media: .2f}")