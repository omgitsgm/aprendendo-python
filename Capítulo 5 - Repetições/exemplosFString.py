# Básico de f-string
a = "mundo"
print(f"Alô {a}.")

# Formatando f-strings especificando o número de caracteres após o nome da variável e dos dois pontos.
preco = 5.20
print(f"Preço: {preco:5.2f}")
print(f"Preço: {preco:10.2f}")
print(f"Preço: {preco:.2f}")

# Utilizando <, > e ^ para alinhar os valores a esquerda, a direita ou ao centro:
print(f"Preço: R${preco:>10.2f}")
print(f"Preço: R${preco:<10.2f}!")
print(f"Preço: R${preco:^10.2f}")

# Especificando caractere para preencher os espaços em branco:
print(f"Preço: R${preco:.^10.2f}!")
print(f"Preço: R${preco:x^10.2f}!")
print(f"Preço: R${preco:_^10.2f}!")

# Chamando funções dentro da f-string:
x = 5.1
print(f"Inteiro: {int(x)}")

# Realizando operações matemáticas dentro da f-string:
print(f"Preço: R${preco * 10:5.2f}!")

# Criando strings de múltiplas linhas com f-string:
print(f"""
... O preço do novo produto é: R${preco:5.2f}.
... E pode ser encontrado nas melhores lojas do ramo.
... """)

# Utilizando o \n em strings
a = "\nprimeira linha\nsegunda linha\nterceira linha"
print(a)