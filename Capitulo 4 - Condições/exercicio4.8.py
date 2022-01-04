# Exercício 4.8 - Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
# Gabriel Mendes, 04.01.2022
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))
operacao = int(input("Qual operação você deseja realizar?\n1- Soma (+)\n2- Subtração (-)\n3- Multiplicação (*)\n4- Divisão (/)\nDigite a opção desejada: "))
if operacao == 1:
    resultado = primeiroNumero + segundoNumero
elif operacao == 2:
    resultado = primeiroNumero - segundoNumero
elif operacao == 3:
    resultado = primeiroNumero * segundoNumero
elif operacao == 4:
    resultado = primeiroNumero / segundoNumero
else:
    print("Opção de operação inválida. Digite um valor entre 1 e 4.")
    resultado = "'inválido'"
print(f"O resultado da operação é: {resultado}.")