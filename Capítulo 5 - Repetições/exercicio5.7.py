# Exercício 5.7 - Modifique o programa 5.6 de tal forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
# Gabriel Mendes, 04.01.2022
valor = int(input("Digite o valor da tabuada desejada: "))
inicio = int(input("Digite o valor inicial da tabuada: "))
fim = int(input("Digite o valor final da tabuada: "))
while inicio <= fim:
    resultado = valor * inicio
    print(f"{valor} x {inicio} = {resultado}")
    inicio = inicio + 1