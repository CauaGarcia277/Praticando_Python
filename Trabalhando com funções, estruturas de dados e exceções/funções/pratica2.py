##Calcular a média de um estudante, onde é possível alterar os dados sem impedir que os cálculos sejam refeitos
## E retornar se foi aprovado com média maior ou igual a 6, caso contrário será reprovado

##Notas do estudante

notas = [6.0, 7.0, 9.0, 5.0]


def boletim(lista):
    media = sum(lista) / len(lista)

    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    return (situacao, media)


print(f"O aluno(a) foi {boletim(notas)[0]} com a média: {boletim(notas)[1]}")
## OU
situacao, media = boletim(notas)
print(f"O aluno(a) foi {situacao} com a média: {media}")