print("Teste usando variáveis e operadores numericos")

number1 = input("Entre com o primeiro número:\n")
number2 = input("Entre o segundo número:\n")

#Parse
number1 = int(number1)
number2= int(number2)

soma = number1 + number2
print("A adição dos números é:", soma)

subtracao = number1 - number2
print("A subtração dos números é:", subtracao)

multiplicacao = number1 * number2
print("A multiplicacao dos números é:", multiplicacao)

divisao = number1 / number2
print("A divisão dos números é:", divisao)

exponenciacao = number1 ** number2
print("A exponenciação é:", exponenciacao)

modulo = number1 % number2
print("O módulo é:", modulo)
