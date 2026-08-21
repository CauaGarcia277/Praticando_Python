medias = [8, 10, 4, 6]
nomes = [("Joao", "as"), ("Pedro", "s"), ("Jose", "as"), ("Ana", "As")]
situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]

print(situacao)

#boletim = list(zip(medias, situacao))
#print(boletim)

lista_completa = [medias, situacao, nomes]
print(lista_completa)

coluna = ["Média", "Notas"]


dicionario = {coluna[i]: lista_completa[i] for i in range(len(coluna))}

print(dicionario)

dicionario["Estudantes"] = [lista_completa[2][i][0] for i in range(len(lista_completa[0]))]
print(dicionario)
