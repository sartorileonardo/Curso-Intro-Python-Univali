#!/usr/bin/python

#Arquivo Servidor.py

import socket                   #Importar módulo de socket

s = socket.socket()             #Cria o objeto socket
host = socket.gethostname()     #Pega o nome da máquina local
port = 12345                    #Reserva uma porta para este serviço
s.bind((host, port))            #Conecta a porta ao serviço

s.listen(5)                     #Espera pela conexão do cliente
while True:
    c, addr = s.accept()        #Estabelece uma conexão com o cliente
    print('Recebendo conexão de: ', addr)
    c.send('Obrigado por ser conectar')
    c.close()                   #Close the connection
