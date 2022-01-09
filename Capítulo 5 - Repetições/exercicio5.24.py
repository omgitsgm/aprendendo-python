# Exercício 5.24 - Modifique o programa 5.23 de forma a ler um número n. Imprima os n primeiros números primos.
# Gabriel Mendes, 06.01.2022
while True:
    numero = int(input("Digite um número qualquer: "))
    verificaNumero = 0
    verificaPrimo = 0
    while verificaNumero <= numero:
        primo = True
        if verificaNumero == 0 or verificaNumero == 1:
            primo = False
        else:
            verificaPrimo = 2
            while verificaPrimo <= verificaNumero:
                if verificaNumero % verificaPrimo == 0 and verificaNumero != verificaPrimo:
                    primo = False
                verificaPrimo += 1
        if primo == True:
            print(f"{verificaNumero} é primo.")
        verificaNumero += 1
    opcao = 2
    while opcao != 0 and opcao != 1:
        opcao = int(input("Digite 0 para sair ou 1 para continuar: "))
        if opcao != 0 and opcao != 1:
            print("Opção invalida.")
    if opcao == 0:
        print("Programa encerrado.")
        break
