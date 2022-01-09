# Exercício 5.22 - Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida. Repita até que a opção sair seja escolhida.
# Gabriel Mendes, 06.01.2022
while True:
    print("TABUADA DE OPERAÇÕES")
    print("1- Adição\n2- Subtração\n3- Divisão\n4- Multiplicação\n5- Sair")
    opcao = int(input("Opção desejada: "))
    if opcao == 5:
        print("Programa encerrado.")
        break
    if opcao < 1 or opcao > 5:
        print("Opção inválida.")
    else:
        tabuada = 1
        while tabuada <= 10:
            numero = 1
            while numero <= 10:
                if opcao == 1:
                    resultado = tabuada + numero
                    print(f"{tabuada} + {numero} = {resultado}")
                elif opcao == 2:
                    resultado = tabuada - numero
                    print(f"{tabuada} - {numero} = {resultado}")
                elif opcao == 3:
                    resultado = tabuada / numero
                    print(f"{tabuada} / {numero} = {resultado}")
                elif opcao == 4:
                    resultado = tabuada * numero
                    print(f"{tabuada} x {numero} = {resultado}")
                numero += 1
            tabuada += 1