import matematica as m

#main
m.procedura1()
somma = m.funzione1()
print("la somma risulta ", somma)

a = float(input("inserisci un numero\n"))
b = float(input("inserisci un numero\n"))

m.procedura2(a,b)
somma = m.funzione2(a,b)
print("la somma risulta ", somma)

a = float(input("inserisci un numero per calocolare la potenza alla seconda\n"))
p = m.potenza(a)
print(p)

b = float(input("inserisci un numero per calocolare la potenza alla terza \n"))
p = m.potenza(b,3)
print(p)


