#1. Escreva um código que lê a lista abaixo e faça:
#A leitura do tamanho da lista
#A leitura do maior e menor valor
#A soma dos valores da lista

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

def leitura(valores):
    tamanho = len(valores)
    maior = max(valores)
    menor = min(valores)
    soma = sum(valores)
    
    return (tamanho, maior, menor, soma)

tamanho, maior, menor, soma = leitura(lista)

print(f"A lista possui {tamanho} números em que o maior número é {maior} e o menor número é {menor}. \n A soma dos valores presentes nela é igual a {soma}")


#2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
# Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:
#Tabuada do 7:
#7 x 0 = 0
#7 x 1 = 7
#[...]
#7 x 10 = 70
def tabuada(x):
    for i in range(11):
        valor = i * x
        print(f"{x} x {i} = {valor}")


num = int(input("Digite um número"))

tabuada(num)


#3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
#[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

lista_dois = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplos_tres(numeros):
    multiplos = []
    for i in numeros:
        if i % 3 == 0:
            multiplos.append(i)
        else:
            continue
    return(multiplos)

print(multiplos_tres(lista_dois))



#4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
#Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = map(lambda x: pow(x, 2), numeros)
quadrado = list(quadrado)
print(quadrado)

## OU
numero_dois = lambda x: x ** 2

valor = list(map(numero_dois, numeros))

print(valor)