# Média ponderada dos estudantes onde N1 tem o peso 3, N2 tem o peso 2 e N3 tem o peso 5

N1 = float(input("Digite a primeira nota do estudante: "))
N2 = float(input("Digite a segunda nota do estudante: "))
N3  = float(input("Digite a terceira nota do estudante: "))


media_ponderada = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10

media_estudante = media_ponderada(N1, N2, N3)
print(media_estudante)