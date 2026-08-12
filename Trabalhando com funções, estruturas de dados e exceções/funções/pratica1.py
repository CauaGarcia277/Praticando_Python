##Calcular a média de um estudante, onde é possível alterar os dados sem impedir que os cálculos sejam refeitos

#Notas do estudante

notas = [8.5, 9.0, 6.0, 10.0]

def media(notas):
    quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    print(media)


media(notas)


##Utilizando return

##Calcular a média de um estudante, onde é possível alterar os dados sem impedir que os cálculos sejam refeitos

#Notas do estudante

notas = [8.5, 9.0, 6.0, 10.0]
def media_2(notas: list) -> float:

    calculo = sum(notas) / len(notas)
    return calculo

valor = media_2(notas)

print(valor)