##1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel:
#[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. 
#Com esses valores, faça um programa que calcule a média de gastos.
# Dica: use as funções built-in sum() e len().


gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

soma = sum(gastos)
total = len(gastos)
media = soma / total

print(media)


##Usando def e laço de repetição
def media(gastos):
    soma = 0
    for i in gastos:
        soma = soma + i
    print(soma)
    total = len(gastos)
    
    media = soma / total
    return print(media)
media(gastos)



#14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
#  A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área 
# dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área 
# dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
#Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade 
# biológica. Dica: use as funções built-in sum() e len().
area = {'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

for chave, valor in area.items():
    print(chave)
    valor = sum(valor) / len(valor)
    print(valor)


##15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as)
#  de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

setor = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

##Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule 
# a média de idade de cada setor, a idade média geral entre todos os setores e quantas 
# pessoas estão acima da idade média geral.

##Media de cada setor:

for chave, valor in setor.items():
    print(chave)
    valor = sum(valor) / len(valor)
    print(valor)

##Media entre os setores
media_geral = 0
for chave, valor in setor.items():
    print(chave)
    media = sum(valor) / len(valor)
    media_geral = media + media_geral

media_geral = media_geral / 4
print(media_geral)

##Pessoas que estao acima da média geral

for chave, valor in setor.items():
    print(chave)
    for idade in valor:
        if idade >= media_geral:
            print(f'Idade: {idade} está acima da média geral')
        else:
            continue
