
#fattoriale
def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)
    
def sommaRicorsiva(n):
    if n==0:
        return 0
    else:
        return n+sommaRicorsiva(n-1)
    

def invertiStringa(s):
    if len(s)==0:
        return ""
    else:
        return invertiStringa(s[1:]) + s[0]
#main
    
def quadrato(x):
    return x*x


def calcola(funzione, n):
    return funzione(n)


funzioneAnonima = lambda x: x*x

print(calcola(lambda x: x*x, 4))    
    
    
"""    
print(fattoriale(5))
print(sommaRicorsiva(4))

print(invertiStringa("alberto"))
"""






"""
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n*fattoriale(n-1)
    
def somma(n):
    if n == 0:
        return 0
    else:
        return n + somma(n-1)
    
def quadrato(x):
    return x*x

def inverti_stringa(s):
    if len(s) == 0:  # Caso base: stringa vuota
        return ""
    else:  # Passo ricorsivo: il primo carattere va alla fine della stringa invertita del resto
        #print(inverti_stringa(s[1:]) + s[0])
        return inverti_stringa(s[1:]) + s[0]

stringa = "alberto"
stringa1 = stringa[1:] + stringa[0]
print(stringa1)
stringa2 = stringa1[1:] + stringa1[0]
print(stringa2)

def fibonacci(n):
    if n <= 1:  # Caso base
        return n
    else:  # Passo ricorsivo
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#print(fattoriale(3))
#print(somma(4))

def calcola(v_funzione, n):
    return v_funzione(n)

#print(calcola(lambda x: x*x, 3 ))
"""
