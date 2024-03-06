# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;



# Função que inverte uma string:
def inverte_string(string_original):
    # Lista dos caracteres da string, em ordem invertida - inicialmente vazia
    caracteres_invertidos = []
    
    # Itera sobre a string original em ordem inversa e adiciona os caracteres na lista criada.
    for i in range(1, len(string_original)+1):
        # Em Python, é possível acessar o último item de uma lista ou string utilizando a posição -1, a penúltima com -2 e assim por diante.
        # Alternativamente, é possível iterar sobre range(len(string_original)-1, -1, -1), ou seja, iniciando na última posição e decrementando-a até chegar em 0
        caracteres_invertidos.append(string_original[-i])
        
    # Retorna a string invertida
    return "".join(caracteres_invertidos) # Junta os caracteres da lista em uma string


# Solicita ao usuário uma string para inverter
string_original = input("Digite uma string para inverter: ")

# Exibe a string original e a string invertida
print(f"A string original é: {string_original}\nA string invertida é: {inverte_string(string_original)}")
exit(0)