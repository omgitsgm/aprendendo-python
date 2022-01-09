# Exercício 5.15 - Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir (no livro) para obter o preço de cada produto. Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de erro "Código inválido".
# Gabriel Mendes, 05.01.2022
totalCompras = 0
while True:
    codigoProduto = int(input("Digite o código do produto ou '0' para exibir o total da compra: "))
    if codigoProduto < 0 or codigoProduto > 9 or codigoProduto == 4 or codigoProduto == 6 or codigoProduto == 7:
        print("Código inválido.")
    elif codigoProduto == 0:
        break
    else:
        if codigoProduto == 1:
            preco = 0.50
        elif codigoProduto == 2:
            preco = 1.0
        elif codigoProduto == 3:
            preco = 4.0
        elif codigoProduto == 5:
            preco = 7.0
        elif codigoProduto == 9:
            preco = 8.0
        qtdProduto = int(input(f"Digite a quantidade do produto {codigoProduto}: "))
        totalCompras += (qtdProduto * preco)
print(f"Total das compras: R${totalCompras:5.2f}")