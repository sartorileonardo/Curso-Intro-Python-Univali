print("Teste WHILE")

#O numero factorial é como 5 = 5*4*3*2*1

factorial_number = input("Entre com um número:")
factorial_number = int(factorial_number)

if factorial_number > 0:
    step = factorial_number
    total = factorial_number
    while step > 1:
        step -= 1
        total *= step
        print("O fatorial de %d é %d"%(factorial_number, total))

elif factorial_number == 0:
    print("O fatorial de 0 é 1")
else:
    print("O fatorial de um número negativo é inválido")

