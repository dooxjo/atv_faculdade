# frutas=['maça','banana','laraja']
# for f in frutas:
#     print(f)
# ######################################333333333333333333333333333333333333333333
# lista=['joana','maria']

# for i,n in enumerate(lista):
#     print(f'{i}={n}')

# #######################################3333333333333333333333333333333333333333333

# numeros=[4,5,8,2,6]

# resultado=[n ** 2 for n in numeros]

# print(resultado)
# #######################################3333333333333333333333333333333333333333333

# #DICIONARIO
# #{chave: valor for item in sequencia}
# nomes = ["Alice", "Bob", "Carlos", "Diana"]
# notas = [10.0, 8.5, 7.0, 9.5]
# alunos = {nome: nota for nome, nota in zip(nomes, notas)}

# for nome, nota in alunos.items():
#     print(f"{nome}: {nota}")

# #######################################
# nomes = ["Alice", "Bob", "Carlos"]
# notas = [10.0, 8.5, 7.0]
# disciplinas = ["Matemática", "Física", "História"]

# # Criando um dicionário com zip e dict comprehension
# alunos = {
#     nome: {
#         "nota": nota,
#         "disciplina": disciplina
#     }
#     for nome, nota, disciplina in zip(nomes, notas, disciplinas)
# }

# for nome, nota, disciplina in zip(nomes, notas, disciplinas):
#     print(f'{nome}----{disciplina} nota={nota}')

# #######################################33333333333333333333333333333333333333333333333
# numeros = [1, 2, 3, 4, 5]
# pares = [num for num in numeros if num % 2 == 0]
# print(pares)

# #######################################33333333333333333333333333333333333333333333333
# # Iterando sobre chaves:

# dicionario = {'a': 1, 'b': 2, 'c': 3}
# for chave in dicionario:
#     print(chave)
# # Iterando sobre valores:

# for valor in dicionario.values():
#     print(valor)
# # Iterando sobre chaves e valores:

# for chave, valor in dicionario.items():
#     print(f"{chave}: {valor}")

#########################################3333333333333333333333333333333333333333333333
