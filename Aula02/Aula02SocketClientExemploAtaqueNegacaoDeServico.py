       

import socket           #importa o módulo de socket

while True:
    s = socket.socket()             #cria um objeto socket
    host = "10.7.25.208"     #pega o nome da maquina local
    port = 12345                    #Reserva uma porta para o seu serviço

    s.connect((host, port))
    print (s.recv(1024))
    s.close()
