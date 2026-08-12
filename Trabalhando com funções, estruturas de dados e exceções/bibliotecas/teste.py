from random import randint

sorteio = randint(1, 100)
tentativas = 1
while True:
    escolha = int(input("Adivinhe o número! Escolha entre 1 e 100: "))

    if escolha < sorteio:
        print(f"O número é maior que {escolha}")
        tentativas = tentativas + 1

    elif escolha > sorteio:
        print(f"O valor é menor que {escolha}")
        tentativas = tentativas + 1

    elif escolha == sorteio:
        print(f"Parábens, acertou o número {escolha} em {tentativas} tentativas!")
        break