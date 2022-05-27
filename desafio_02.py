# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

cidade = input("Digite sua cidade: ").capitalize()
estado = input("Digite seu estado: ").capitalize()

print(f"Você mora na cidade: {cidade}")
print("Seu estado é: {}".format(estado))
