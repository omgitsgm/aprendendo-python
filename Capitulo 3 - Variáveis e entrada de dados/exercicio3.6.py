# Exercício 3.6 - Esvreva uma expressão que será utilizada pra decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
# Gabrie Mendes, 02.01.2022
materia1 = 7.0
materia2 = 9.0
materia3 = 8.5
alunoAprovado = materia1 > 7.0 and materia2 > 7.0 and materia3 > 7.0
print("Aluno aprovado:", alunoAprovado) 