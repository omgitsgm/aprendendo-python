# Exercício 5.6 - Altere o programa 5.5 para exibir os resultado no mesmo formato de uma tabulada: 2x1 = 2, 2x2 = 4...
# Gabriel Mendes, 04.01.2022
valor = int(input("Digite o valor da tabuada desejada: "))
tabuada = 1
while tabuada <= 10:
    resultado = valor * tabuada
    print(f"{valor} x {tabuada} = {resultado}")
    tabuada = tabuada + 1