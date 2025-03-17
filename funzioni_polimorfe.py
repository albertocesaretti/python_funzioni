# *args
def somma(*args):
    risultato = 0
    for numero in args:
        risultato += numero
    return risultato

print(somma(1, 2, 3))  # Output: 6
print(somma(1, 2, 3, 4, 5))  # Output: 15

def stampa_info(**kwargs):
    for chiave, valore in kwargs.items():
        print(f"{chiave}: {valore}")

stampa_info(nome="Alice", eta=30, citta="Roma")
    # Output:
    # nome: Alice
    # eta: 30
    # citta: Roma
    
def funzione_mista(*args, **kwargs):
    print("Argomenti posizionali:", args)
    print("Argomenti con nome:", kwargs)

funzione_mista(1, 2, 3, nome="Bob", professione="Programmatore")
    # Output:
    # Argomenti posizionali: (1, 2, 3)
    # Argomenti con nome: {'nome': 'Bob', 'professione': 'Programmatore'}    
    
    