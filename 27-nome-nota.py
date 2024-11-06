alunos = []
notas = []

for i in range(5):
    aluno = input("Digite o Nome do Aluno: ")
    nota = int(input("Digite a Nota do Aluno: "))
    alunos.append(aluno)
    notas.append(aluno)

for i in range(5):
    print(f"O Aluno {alunos[i]} - Tirou Nota: {notas[i]}")
