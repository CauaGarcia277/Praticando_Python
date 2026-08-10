#2. Escreva um código para importar a biblioteca numpy com o alias np.
import numpy as np
from random import choice, randrange

from math import pow
#3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

for i in range(0, 1):
    print(choice(lista))


##4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.

print(randrange(100))

##5. Crie um programa que solicite à pessoa usuária digitar 
## dois números inteiros e calcular a potência do 1º número elevado ao 2º.

##num1 = int(input("Digite um número: "))
#num2 = int(input("Digite o segundo número: "))

#print(f"A potência do primeiro número: {num1}, elevado ao segundo número: {num2} é igual a = {pow(num1, num2)}")


## 6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
## A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com
## a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva
## para ela o número sorteado.

sorteio = int(input("Digite o número de participantes: "))

print(f"O participante sorteado foi {randrange(1, sorteio)}")



##7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa.
## O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe
## uma mensagem junto a esse token gerado aleatoriamente.
while True:
    sorteio = randrange(9998)

    if sorteio % 2 == 0:
        nome = input("Digite seu nome: ")
        print(f"Olá {nome}, seu Token é {sorteio}")
        break
    else:
        continue

##Filtrando por par no randrange()

nome_2 = input("Digite seu nome: ")

token = randrange(1000, 10000, 2)

print(f"Olá {nome}, seu Token é {token}")



