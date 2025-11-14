# char_intersection.py

frase1 = input().split()
frase2 = input().split()

comuns = []

for palavra in frase1:
    if palavra in frase2 and palavra not in comuns:
        comuns.append(palavra)

comuns.sort()

print(" ".join(comuns))
