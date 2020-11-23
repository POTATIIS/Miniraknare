def plus(x, y):
    return x + y

def minus(x, y):
    return x - y    

def gånger(x, y):
    return x * y    

def delat(x, y):
    return x / y
            
print("Välj alternativ. ")
print("1.plus")    
print("2.minus")
print("3.gånger")
print("4.delat")
print("5.avsluta")

while True:
    alternativ = input("Välj alternativ: ")

    if alternativ in ('1', '2', '3', '4'):
        nummer1 = float(input("Välj den första siffran: "))
        nummer2 = float(input("Välj den andra siffran: "))

    if alternativ == '5':
        print("Hej Då")
        break

    elif alternativ == '1':
        print(nummer1, "+", nummer2, "=", plus(nummer1, nummer2))        

    elif alternativ == '2':
        print(nummer1, "-", nummer2, "=", minus(nummer1, nummer2))        

    elif alternativ == '3':
        print(nummer1, "*", nummer2, "=", gånger(nummer1, nummer2))

    elif alternativ == '4':
        print(nummer1, "/", nummer2, "=", delat(nummer1, nummer2))
        break

    else:
        print("Försök igen")
  