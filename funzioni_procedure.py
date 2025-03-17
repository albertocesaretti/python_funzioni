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

#main
procedura1()
somma = funzione1()
print("la somma risulta ", somma)

a = float(input("inserisci un numero\n"))
b = float(input("inserisci un numero\n"))

procedura2(a,b)
somma = funzione2(a,b)
print("la somma risulta ", somma)

a = float(input("inserisci un numero per calocolare la potenza alla seconda\n"))
p = potenza(a)
print(p)

b = float(input("inserisci un numero per calocolare la potenza alla terza \n"))
p = potenza(b,3)
print(p)
