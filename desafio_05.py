
# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.

numero = 1
indice = 0

while numero <= 60:
    if indice % 2 == 0:
        print(f"Índice: {indice:02.0f}|Item:{numero:02.0f}")
    numero += 1
    indice += 1






