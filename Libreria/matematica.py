#funzioni e procedure

def procedura1():
    a = float(input("inserisci un numero\n"))
    b = float(input("inserisci un numero\n"))
    somma = a + b
    print("somma  = ", somma)
    
def funzione1():
    a = float(input("inserisci un numero\n"))
    b = float(input("inserisci un numero\n"))
    return  a + b    
    
def procedura2(a, b):
    somma = a + b
    print("somma  = ", somma)
    
def funzione2(a,b):
    return  a + b

def potenza(a, b = 2): #b parametro opzionale
    return a**b