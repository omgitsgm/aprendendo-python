# Exercício 5.21 - Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.
# Gabriel Mendes, 06.01.2022
while True:
    valor = int(input("Digite o valor a pagar ou digite '0' para sair: "))
    if valor == 0:
        print("Programa encerrado.")
        break
    cedulas = 0
    atual = 50
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            print(f"{cedulas} cédula(s) de R${atual}.")
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cedulas = 0