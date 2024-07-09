print('Pyhton na Escola de Programação Alura')

name = 'Karina'
age = 45
print(f'Meu nome é {name} e tenho {age} anos.')

print('A\n' 'L\n' 'U\n' 'R\n' 'A\n')
print('A','L','U','R','A',sep='\n')

pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')

pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

def classificar_musica(genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'Pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'

resultado = classificar_musica('Rock', 'Pop')
print(resultado)

"""1 - Solicite ao usuário que insira um número e, em seguida, 
use uma estrutura if else para determinar se o número é par ou ímpar."""

number = int(input("Enter any number and let´s find out if it is odd or even: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

"""2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar 
a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos."""

age = int(input("Please enter your age: "))
if age <= 12:
    print("You are a child")
elif 13 < age < 18:
    print("You are a teenager")
elif age >=18:
    print("You are an adult")
else:
    print("Invalid")

"""3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário
 e a senha fornecidos correspondem aos valores esperados determinados por você."""

user_id = "melissa"
password_id = "mel1234"

"""3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o 
nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você."""

user = input("Please provide your user name: ")
password = input("Enter your password: ")

if user == user_id and password == password_id:
    print("Successfully logged in!")
else:
    print("These credentials are invalid. Please try again.")

"""4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem."""

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")

# Criando uma lista de compras
lista_de_compras = ["Maçã", "Banana", "Leite", "Pão", "Queijo"]

# Adicionando um item à lista
lista_de_compras.append("Ovos")

# Removendo um item da lista
lista_de_compras.remove("Banana")

# Exibindo a lista
print("Lista de Compras:")
for item in lista_de_compras:
    print("- " + item)

# Definindo uma tupla de coordenadas geográficas
coordenadas_gps = (40.7128, -74.0060)

# Exibindo as coordenadas
print("Coordenadas GPS:")
print("Latitude:", coordenadas_gps[0])
print("Longitude:", coordenadas_gps[1])

