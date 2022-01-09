# Exercício 5.11 - Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
# Gabriel Mendes, 04.01.2022
depositoInicial = float(input("Digite o depósito inicial: "))
taxaJuros = (float(input("Taxa de juros da poupança (%): "))) / 100
mes = 1
saldoAtual = depositoInicial
while mes <= 24:
    saldoAtual = saldoAtual + (saldoAtual * taxaJuros)
    print(f"{mes:02d}º mês: R${saldoAtual:5.2f}.")
    mes = mes + 1
totalGanhoJuros = saldoAtual - depositoInicial
print(f"Total ganho com juros no período: R${totalGanhoJuros:5.2f}.")