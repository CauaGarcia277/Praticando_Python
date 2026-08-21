#9. Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. 
# Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: 
# estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

#A empresa sempre está abrindo novas filiais, de modo que a tabela está constantemente recebendo novos 
# registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

#A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com 
# a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
estados_unicos = list(set(estados))

lista_de_listas = []

for estado in estados_unicos:
    lista = [uf for uf in estados if uf == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário em que a chave é o nome de cada estado único e o valor é a contagem de elementos
contagem_valores = {estados_unicos[i]: len(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(contagem_valores)


funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]


# Armazenando os estados sem repetição de valor
estados_unicos = list(set([tupla[0] for tupla in funcionarios]))

# Criando uma lista de listas com valores de funcionários de cada estado
lista_de_listas = []
for estado in estados_unicos:
    lista = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    lista_de_listas.append(lista)
print(lista_de_listas)

# Criando um dicionário com dados agrupados de funcionário por estado
agrupamento_por_estado = {estados_unicos[i]: lista_de_listas[i] for i in range(len(estados_unicos))}
print(agrupamento_por_estado)

# Criando um dicionário com a soma de funcionários por estado
soma_por_estado = {estados_unicos[i]: sum(lista_de_listas[i]) for i in range(len(estados_unicos))}
print(soma_por_estado)




    

    