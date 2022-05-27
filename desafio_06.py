# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.

# Comece o programa perguntando o nome da aluna.


# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser
# impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.


alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]
nome = input("Digite o seu nome: ").title()

if nome in alunas:
    nota = (notas[alunas.index(nome)])
    if nota < 60:
        print("{}Olá, {}! Sua nota foi {}.{}".format('\033[1;31m', nome, nota,'\033[m'))
    elif nota >= 90:
         print("{}Olá, {}! Parabéns! Sua nota foi {}.{}".format('\033[1;32m', nome, nota,'\033[m'))
    else:
        print("Olá, {}! Sua nota foi {}".format(nome, nota))

else:
    print("{}ERRO! Nome não cadastrado na turma!{}".format('\033[1;31m', '\033[m'))