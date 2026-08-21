#4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso 
# o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
lista = [item[1] for item in aluguel if item[0] == 'Apartamento']
print(lista)

#5. Crie um dicionário usando o dict comprehension em que as chaves estão 
# na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] 
#e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

mes = {meses[i]: despesa[i] for i in range(len(despesa))}
print(mes)

#6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa 
# filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas 
# as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de 
# um código:

vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
quantia = [valores[1] for valores in vendas if valores[0] == '2022' and valores[1] >= 6000]

print(quantia)


