notas = {
    "1 trimestre" : 8.5,
    "2 trimestre" : 9.5,
    "3 trimestre": 7
}


soma = sum(notas.values())

qtd_notas = len(notas)

media = soma / qtd_notas

print(round(media, 1))
