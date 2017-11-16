#!usr/bin/python

#Importanto o arquivo que tem as funções de cálculo, no caso abaixo a função soma
from Aula02ModulosOperacoes1 import soma

from Aula02ModulosOperacoes1 import sub

from Aula02ModulosOperacoes1 import mult

from Aula02ModulosOperacoes1 import div

n1 = 5
n2 = 7

somatoria = soma(n1, n2)
print("Resultado: ", somatoria)

subtracao = sub(n1, n2)
print("Resultado: ", subtracao)

multiplicacao = mult(n1, n2)
print("Resultado: ", multiplicacao)

divisao = div(n1, n2)
print("Resultado: ", divisao)









