from random import choice, randrange

frutas = ["maçã", "banana", "uva", "pêra", 

          "manga", "coco", "melancia", "mamão",

          "laranja", "abacaxi", "kiwi", "ameixa"]

escolhidas = []
for i in range(0, 3):
    escolhidas.append(choice(frutas))

print(escolhidas)


## 9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, 
## identificando quais resultaram em um número inteiro. A lista é a seguinte:



numeros = [2, 8, 15, 23, 91, 112, 256]
inteiros = []
nao_inteiros = []
for i in numeros:
    num1 = i / 2
    if i / 2 == num1 and num1 * 2 == i:
        inteiros.append(i)
        continue
    else:
        nao_inteiros.append(i)

print(inteiros, nao_inteiros)