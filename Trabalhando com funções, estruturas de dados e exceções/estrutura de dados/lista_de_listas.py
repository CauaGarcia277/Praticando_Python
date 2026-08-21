teste = [1, 2, 3, 4, 5, 6, 7, 8, 9]


lista = []
for i in range(0, len(teste), 3):
    lista.append([teste[i], teste[i + 1], teste[i+2]] )

print(lista[0][2])



notas = [[8, 8, 10], [10, 5, 2], [8, 4, 6], [5,10, 9], [10, 3, 4]]

def media(lista: list):
    calculo = sum(lista) / len(lista)

    return calculo

medias = [round(media(nota), 1) for nota in notas]

print(medias)

estudantes = [("João", "Jq123"), ("Maria", "M123"), ("Carlos", "C124"), ("Julia", "J542"), ("Pedro", "P432")]


nomes = [nome[0] for nome in estudantes]

print(nomes)

boletim = list(zip(nomes, medias))

print(boletim)

candidatos = [estudante[0] for estudante in boletim if estudante[1] >= 8.0]

print(candidatos)