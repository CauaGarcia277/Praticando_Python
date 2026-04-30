##Criando dicionário
mercado_dict = {
    1: 'Feijão',
    2: 'Beterraba',
    3: 'Cogumelo'
}

print(mercado_dict[2])

cadastro = {
    'matrícula': 10002,
    'nome': 'João',
    'Turma': '2F',
    'data_cadastro': '22/10/2020'
}

##Buscando valores pela chave
print(cadastro['nome'])

##Modificando um valor
cadastro['nome'] = 'Pedro'
print(cadastro)

##Cadastrando uma nova chave e valor
cadastro['modalidade'] = 'EAD'
print(cadastro)

##Removendo
cadastro.pop('Turma')
print(cadastro)

##Usando Items para retornar uma lista de chave-valor
metodo_items = cadastro.items()
print(metodo_items)

##Keys retorna apenas as chaves
metodo_keys = cadastro.keys()
print(metodo_keys)

##Values para retornar valores
metodo_values = cadastro.values()
print(metodo_values)

##Usando laços de repetição
for chaves in cadastro.keys(): ##Chave faz referencia a keys
    print(chaves)

for i in cadastro.values():
    print(i)


##Buscando todas as chaves e matrículas do cadastro
for chave, valor in cadastro.items():
    print(f'Chave: {chave} Valor: {valor}')