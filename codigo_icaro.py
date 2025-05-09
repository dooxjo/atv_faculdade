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

    return alunos

def criar_dicionario_alunos(alunos):
    alunos_dict = {
        nome: {
            'disciplinas': {disciplina: nota for disciplina, nota in disciplinas},
            'notas': [nota for _, nota in disciplinas],
            'media': calcular_media([nota for _, nota in disciplinas])
        }
        for nome, disciplinas in alunos
    }

    return alunos_dict

def exibir_alunos_por_media(alunos_dict, media_minima):
    alunos_filtrados = [(nome, dados['media'])
                        for nome, dados in alunos_dict.items()
                        if dados['media'] >= media_minima]

    if alunos_filtrados:
        print(f"\nAlunos com média acima de {media_minima}:")
        for nome, media in alunos_filtrados:
            print(f"- {nome}: {media:.2f}")
    else:
        print(f"\nNenhum aluno com média acima de {media_minima}.")

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

def main():
    alunos = [
        ("João", [("Matemática", 8.5), ("Português", 7.0), ("Física", 9.0)]),
        ("Maria", [("Matemática", 9.5), ("Português", 8.5), ("Química", 10.0)]),
        ("Pedro", [("Matemática", 6.5), ("Português", 6.0), ("História", 7.0)]),
        ("Ana", [("Matemática", 8.0), ("Português", 9.0), ("Biologia", 8.5)]),
        ("Lucas", [("Matemática", 5.5), ("Português", 6.5), ("Geografia", 7.5)])
    ]

    alunos_dict = criar_dicionario_alunos(alunos)

    print("\nTodos os alunos e suas médias:")
    for nome, dados in alunos_dict.items():
        print(f"{nome}: {dados['media']:.2f}")

    media_minima = 7.5
    exibir_alunos_por_media(alunos_dict, media_minima)
    ordenar_alunos_por_media(alunos_dict)

if __name__ == "__main__":
    main()
