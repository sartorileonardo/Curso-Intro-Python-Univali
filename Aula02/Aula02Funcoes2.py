#!usr/bin/python

def alteralista(minhalista):
    "Modifica uma lista passara como parâmetros"
    minhalista.append([1,2,3,4]);
    print("Valores dentro da função: ", minhalista)
    return

#Agora você pode chamar a função alteralista
minhalista = [10,20,30];
alteralista(minhalista)
print("Valores fora da função:", minhalista)
