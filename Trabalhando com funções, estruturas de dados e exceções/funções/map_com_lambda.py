##Criar uma função que faz um qualitativo (Ponto extra) na média dos estudantes

notas = [6.0, 7.0, 9.0, 5.5, 8.0]

qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)

notas_atualizadas = list(notas_atualizadas)

print(notas_atualizadas)