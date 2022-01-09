# Exercício 5.13 - Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
# Gabriel Mendes, 04.01.2022
valorInicialDivida = float(input("Digite o valor inicial da dívida: R$"))
juroMensalDivida = (float(input("Digite o juro mensal da dívida (%): "))) / 100
valorMensalPago = float(input("Digite o valor mensal que será pago: R$"))
divida = valorInicialDivida
totalPago = 0
totalJuroPago = 0
mes = 0
while divida > 0:
    if (divida * juroMensalDivida) + divida < valorMensalPago:
        valorMensalPago = (divida * juroMensalDivida) + divida
    totalJuroPago = totalJuroPago + (divida * juroMensalDivida) 
    divida = ((divida * juroMensalDivida) + divida) - valorMensalPago
    totalPago = totalPago + valorMensalPago
    mes = mes + 1
print(f"Total de meses para pagar a dívida: {mes:02d}.")
print(f"Total pago: R${totalPago:5.2f}.")
print(f"Total de juros pago: R${totalJuroPago:5.2f}.")