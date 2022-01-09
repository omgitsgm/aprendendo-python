# Exercício 5.10 - Modifique o programa do livro para que aceite respostas com letras maiúsculas e minúsculas em todas as questões.
# Gabriel Mendes, 04.01.2022
pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Digite a resposta da questão {questao}: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos = pontos + 1
    elif questao == 2 and (resposta == "a" or resposta == "A"):
        pontos = pontos + 1
    elif questao == 3 and (resposta == "d" or resposta == "D"):
        pontos = pontos + 1
    questao = questao + 1
print(f"O aluno fez {pontos} ponto(s).") 