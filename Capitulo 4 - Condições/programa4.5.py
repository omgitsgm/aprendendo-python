# Programa 4.5 - Conta de telefone com três faixas de preço
# Gabriel Mendes, 04.01.2022
minutos = int(input("Digite quantos minutos você utilizou esse mês: "))
if minutos < 200:
    preco = minutos * 0.20
else:
    if minutos < 400:
        preco = minutos * 0.18
    else:
        preco = minutos * 0.15
print(f"Você vai pagar, este mês, o valor de R${preco:4.2f}.")