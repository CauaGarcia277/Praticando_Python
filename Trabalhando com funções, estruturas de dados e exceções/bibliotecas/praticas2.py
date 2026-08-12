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

from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]
# iniciando uma lista vazia para receber as raízes
raiz = []

for i in numeros:
   raiz.append(sqrt(i))

print(raiz)

for i in range(len(raiz)):
    if raiz[i] // 1 == raiz[i]:
        print(f"O número {numeros[i]} possui a raiz inteira = {raiz[i]}")



