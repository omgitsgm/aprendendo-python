# Exercício 5.23 - Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
# Gabriel Mendes, 06.01.2022
while True:
    primo = True
    numero = int(input("Digite um número: "))
    if numero == 0 or numero == 1:
        primo = False
    else:
        verificaPrimo = 2
        while verificaPrimo <= numero:
            if primo == False:
                break
            restoDivisao = numero % verificaPrimo
            if verificaPrimo == 2 or verificaPrimo % 2 != 0:
                if restoDivisao == 0 and verificaPrimo != numero:
                    primo = False
            verificaPrimo += 1
    if primo == False:
        print(f"O número {numero} não é primo.")
    else:
        print(f"O número {numero} é primo.")
    
    opcao = 2
    while opcao != 0 and opcao != 1:
        opcao = int(input("Digite 0 para sair ou 1 para continuar: "))
        if opcao != 0 and opcao != 1:
            print("Opção inválida.")
    if opcao == 0:
        print("Programa encerrado.")
        break