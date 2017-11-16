print("Teste de formatação de strings")

myInteger = 12345
myFloat = 3.14159
myString = "Curso de Python da UNIVALI"

print("Integer:", myInteger)
print("Integer decimal %d é um número integer %d"%(myInteger,myInteger))
print("Integer Hexadecimal %x"%myInteger)

print("Float", myFloat)
print("Default %f"%myFloat)
print("Exponencial %e"%myFloat)

print("Justificar Direita(%10d)"%myFloat)
print("Justificar Esquerda(%-10d)"%myFloat)

print("Forçar 9 dígitos %.9d"%myInteger)
print("3 dígitos depois do decimal (float)%.3f"%myFloat)
print("Dez e cinco caracteres permitidos na string:")
print("(%.10s) (%.5s)"%(myString, myString))
