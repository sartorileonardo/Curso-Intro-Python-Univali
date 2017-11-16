#!/usr/bin/python

import mysql.connector
from mysql.connect import errorcode

try:
    cnx = mysql.connector.connect(user="root",
                                  password="CursoPython",
                                  host="cursopython.c7logjfx955c.us-west-2.rds.amazonaws.com",
                                  database="employees")
    except mysql.connect.Error as err:
        if err.errno = errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com o seu nome de usuário e password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Banco de dados não existe")
        else:
            print(err)
    else:
        cnx.close()
