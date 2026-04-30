##Lendo quantidade de valores na lista

nome = "Daniel"
nota_um = 9.0
nota_dois = 7.5

lista = [nome, nota_um, nota_dois, 10, 2, 123.2]

print(len(lista))

##Partição

print(lista[1:4]) ##Inicio do elemento 1(nota_um) e fim sendo o 2, pois o fim é mais um
print(lista[:4]) ##Inicio até o final especificado
print(lista[4:])##Inicio especificado até o final

##Append, adiciona no final da lita
nota_oito = 30
lista.append(nota_oito)
print(lista)

##Extend, adiciona mais de um elemento
lista.extend([500, 21313, 1.1])
print(lista)

##Remove
lista.remove(1.1)
print(lista)

##Pop para tirar um valor específico por posição
lista.pop(0)
print(lista)

##Insert para inserir em uma posição específica
lista.insert(2, 'Teste')
print(lista)

##Index para retornar a posição do vaslor
lista = lista.index('Teste')
print(lista)

##Sort para organizar
teste = ['Amora', 'Beterraba', 'Ameixa', 'Cenoura']

teste.sort()
print(teste)
