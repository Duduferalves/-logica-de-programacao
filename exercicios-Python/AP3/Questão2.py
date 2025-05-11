aprovados = 0
reprovados = 0
total_alunos = 0
print("Digite [-1] para sair")
while True:
    nota = float(input("Digite a nota do aluno: "))
    if nota == -1:
        break
    total_alunos = total_alunos + 1
    if nota >= 5:
        aprovados = aprovados + 1
    else:
        reprovados = reprovados + 1
if total_alunos > 0:
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade de alunos reprovados: {reprovados}")
    print(f"Total de alunos que fizeram a prova: {total_alunos}")
else:
    print("Nenhuma nota válida foi digitada.")
