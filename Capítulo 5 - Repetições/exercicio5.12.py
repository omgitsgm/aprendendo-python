# Exercício 5.12 - Altere o programa 5.11 de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de casa mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
# Gabriel Mendes, 04.01.2022
depositoInicial = float(input("Digite o depósito inicial: R$"))
taxaJuros = (float(input("Digite a taxa de juros da poupança (%): "))) / 100
depositoMensal = float(input("Digite um valor para ser depositado mensalmente: R$"))
mes = 1
saldoAtual = depositoInicial
while mes <= 24:
    saldoAtual = saldoAtual + depositoMensal + (saldoAtual * taxaJuros)
    print(f"{mes:02d}º mês: R${saldoAtual:5.2f}.")
    mes = mes + 1
totalGanhoJuros = saldoAtual - depositoInicial
print(f"Total ganho em juros: R${totalGanhoJuros:5.2f}.")