# Exercício 5.3 - Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
# Gabriel Mendes 04.01.2022
contagem = 10
while contagem >= 0:
    if contagem == 0:
        print(f"{contagem} ", end="")
    else:
        print(f"{contagem}, ", end="")
    contagem = contagem - 1
print("e Fogo!")