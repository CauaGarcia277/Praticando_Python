nome = "Daniel"
nota_um = 9.0
nota_dois = 7.5


lista = [nome, nota_um, nota_dois]

print(lista)

##Selecionando o nome
print(lista[0])

##Selecionando tudo da lista com for
for i in lista:
    print(i)

##Modificando um valor da lista
lista[2] = 8.2
print(lista[2])


##Manipulando os valores
media = (lista[1] + lista[2])/ 3

lista.append(media) ##Adicionando na lista
print(lista)

##Transformando string em lista usando .split

exemplo = 'Separando, por, virgula, cada, palavra'
exemplo = exemplo.split(',')
print(exemplo)

exemplo_dois = 'Separando as palavras sem nenhuma restrição'
exemplo_dois = exemplo_dois.split()
print(exemplo_dois)

##Removendo
lista.remove('Daniel')
print(lista)
