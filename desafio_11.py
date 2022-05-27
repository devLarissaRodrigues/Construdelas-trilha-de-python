# Dado um arquivo de entrada, escreva um programa que leia o conteudo do arquivo para uma string,
# e escreva um outro arquivo de saída que imprima o texto ao contrário.
# Exemplo de entrada: Oi mulheres maravilhosas do curso de Python do ConstruDelas!
# Exemplo de saída: !saleDurtsnoC od nohtyP ed\nosruc od sasohlivaram serehlum iO


with open("arquivo_desafio_11.txt", "r") as arquivo:
    arquivo_desafio_11 = arquivo.read()


print(arquivo_desafio_11[::-1])