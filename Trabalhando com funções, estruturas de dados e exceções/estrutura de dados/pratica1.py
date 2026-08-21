#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

soma = [sum(num) for num in lista_de_listas]
print(soma)
#2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

terceiro = [item[2] for item in lista_de_tuplas]
print(terceiro)

#3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], 
#crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento 
#como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
lis_tup = []
for i in range(len(lista)):
    lis_tup.append((i, lista[i]))
print(lis_tup)

    