# Exercício 5.20 - O que acontece se digitarmos 0,001 no programa 5.19? Caso ele não funcione, altere-o de forma a corrigir o problema.
# Gabriel Mendes, 05.01.2022
valor = float(input("Digite o valor a pagar: R$"))
cedulas = 0
atual = 100
apagar = valor
if valor >= 0.01:
    while True:
        if atual <= apagar:
            apagar -= atual
            cedulas += 1
        else:
            if atual >= 1:
                print(f"{cedulas} cédula(s) de R${atual}.")
            else:
                print(f"{cedulas} moeda(s) de R${atual}.")
            if apagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            cedulas = 0
else:
    print("Valor a ser pago é inválido.")