# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# Função para verificar se x pertênce à sequência de Fibonacci:
def verifica_fibonacci(x):
    # Inicializa a sequência de Fibonacci com os dois termos iniciais
    seq_fibonacci = [0, 1]

    # Incrementa a sequência até o último termo da sequência ser maior ou igual à x
    while seq_fibonacci[-1] < x:
        # Adiciona o novo termo com base na definição da sequência onde F[n] = F[n-1] + F[n+2]
        seq_fibonacci.append(seq_fibonacci[-1] + seq_fibonacci[-2])

    # Verifica se x está na sequência
    if x in seq_fibonacci:  # Se x está na sequência
        print(f"O número {x} pertence à sequência de Fibonacci: {seq_fibonacci}...")
    else:  # Se x não está na sequência
        print(
            f"O número {x} não pertence à sequência de Fibonacci. Esta é a sequência de Fibonacci até o menor termo maior que {x}: {seq_fibonacci}..."
        )
    return


# Solicita ao usuário um número para verificar se ele pertence à sequência de Fibonacci
x = input("Digite um número inteiro x para verificar se ele pertence à sequência de Fibonacci: ")
# Verifica se o número é um inteiro
if x.isdigit():
    # Chamada da função para verificar se x pertence à sequência de Fibonacci
    verifica_fibonacci(int(x))
else:
    print(f"{x} não é um inteiro válido.")
exit(1)
