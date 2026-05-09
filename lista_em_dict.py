loja = {
    'nome': ['Televisão', 'Celular', 'fogão', 'Notebook'],
    'preço': [2000, 3000, 1500, 6000]
}

print(loja)

for chave, valor in loja.items():
    print(f'Chave: {chave}\nElemento:')
    for dado in valor:
        print(dado)

valor = loja.values()

print(valor)

