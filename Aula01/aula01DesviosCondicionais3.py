print("Test IF/ELSE")

grade1 = input("Entre com sua nota:")
grade1 = int(grade1)

if grade1 >= 7:
    print("Você passou!")
    if(grade1 >= 9):
        print("Sua nota é A")
    elif grade1 >= 8:
        print("Sua nota é B")
    elif grade1 >= 7:
        print("Sua nota é C")
else:
    print("Não passou!")
