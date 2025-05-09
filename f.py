def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def cadastrar_alunos():
    alunos = []

    while True:
        nome = input("Nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        disciplinas = []
        while True:
            disciplina = input("Nome da disciplina (ou 'pronto' para encerrar): ")
            if disciplina.lower() == 'pronto':
                break

            try:
                nota = float(input(f"Nota de {disciplina}: "))
                disciplinas.append((disciplina, nota))
            except ValueError:
                print("Nota inválida. Por favor, insira um número.")

        alunos.append((nome, disciplinas))

    criar_dicionario_alunos(alunos)
    



def criar_dicionario_alunos(alunos):
    alunos_dict = {
        nome: {
            'disciplinas': {disciplina: nota for disciplina, nota in disciplinas},
            'notas': [nota for _, nota in disciplinas],
            'media': calcular_media([nota for _, nota in disciplinas])
        }
        for nome, disciplinas in alunos
    }
    exibir_alunos_por_media(alunos_dict)


    

def exibir_alunos_por_media(alunos_dict):
    alunos_filtrados = [(nome, dados['media'])
                        for nome, dados in alunos_dict.items()
                        if dados['media'] >= 7]

    if alunos_filtrados:
        print(f"\nAlunos com média acima de 7:")
        for nome, media in alunos_filtrados:
            print(f"- {nome}: {media:.2f}")
    else:
        print(f"\nNenhum aluno com média acima de 7.")
    ordenar_alunos_por_media(alunos_dict)

def ordenar_alunos_por_media(alunos_dict):
    alunos_ordenados = sorted(
        [(nome, dados['media']) for nome, dados in alunos_dict.items()],
        key=lambda x: x[1],
        reverse=True
    )

    print("\nAlunos ordenados por média (maior para menor):")
    for i, (nome, media) in enumerate(alunos_ordenados, 1):
        print(f"{i}. {nome}: {media:.2f}")

    return alunos_ordenados


if __name__ == "__main__":
   cadastrar_alunos()