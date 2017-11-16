#!usr/bin/python

lista1 = [1,2,3,4,5,6,7,8,9]

print("Lista 1 original:", lista1)

lista1.append(10)
lista1.append(11)

print("Lista 1 com o 10 e 11 adicionados:", lista1)

del lista1[10]

print("Lista 1 com o 11 removido:", lista1)

for x in lista1:
    print("elemento:", x)
