
#5. Você foi contratado(a) como cientista de dados de uma associação de skate. 
#Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
#você precisa criar um código que calcula a pontuação dos(as) atletas. 
#Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

#Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar 
#a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
#"Nota da manobra: [media]"

nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))
nota_tres = float(input("Digite a terceira nota: "))
nota_quatro = float(input("Digite a quarta nota: "))
nota_cinco = float(input("Digite a quinta nota: "))
#OU
notas_dois = []
for i in range(1,6):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas_dois.append(nota)

notas = [nota_um, nota_dois, nota_tres, nota_quatro, nota_cinco]
def calculo(notas = list):
    notas.remove(max(notas))
    notas.remove(min(notas))
    

    quant = len(notas)
    num = sum(notas)
    media = num / quant
    return media

print(calculo(notas))



#6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
#você precisa criar uma função que receba uma lista de 4 notas e retorne:

#maior nota
#menor nota
#média
#situação (Aprovado(a) ou Reprovado(a))
#Para testar o comportamento da função, os dados podem ser exibidos em um texto:
#"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota
# de [menor] pontos e foi [situacao]"

notas = []

for i in range(1,5):
    nota = float(input("Digite a {i}ª nota: "))
    notas.append(nota)

def boletim(notas = list):
    maior = max(notas)
    menor = min(notas)

    quant = len(notas)
    soma = sum(notas)
    media = soma / quant
    if media >= 6:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"
    return (maior, menor, media, situacao)

maior, menor, media, situacao = boletim(notas)
print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maior} pontos e a menor nota de {menor} pontos e foi {situacao}")