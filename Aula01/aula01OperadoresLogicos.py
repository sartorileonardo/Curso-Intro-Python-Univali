print("Teste de igualdade em Operadores Relacionais")

number1 = input("Entre o primeiro número:")
number1 = int(number1)

number2 = input("Entre o segundo número:")
number2 = int(number2)

if number1 == number2:
    print("%d é igual a %d"%(number1, number2))

if(number1 != number2):
    print("%d não é igual a %d"%(number1, number2))

if(number1 < number2):
    print("%d é menor que %d"%(number1,number2))

if(number1 > number2):
    print("%d é maior que %d"%(number1,number2))
    
if(number1 <= number2):
    print("%d é menor ou igual que %d"%(number1,number2))

if(number1 >= number2):
    print("%d é maior ou igual que %d"%(number1,number2))

