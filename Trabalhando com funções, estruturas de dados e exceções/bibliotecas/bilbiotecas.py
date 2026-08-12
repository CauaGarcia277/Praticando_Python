import matplotlib.pyplot as plt

estudantes = ["Diego", "Carlos", "Eduardo"]

notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height = notas)
plt.show()

## Funcões de uma biblioteca
from random import randrange, sample


lista = []

for i in range(0, 20): ##Irá rodar 20 vezes
  lista.append(randrange(100)) ##Irá adicionar a lista um valor de 100 20 vezes.

print(sample(lista, 5))

