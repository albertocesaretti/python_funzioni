#programmazione strutturata
#lettura da file.txt

listaTemperature = [] #lista temperature numeri interi
listaGiorni = []	#stringhe
f = open("temperature.txt","r")
i = 0
for linea in f:
    linea = linea.strip() #toglie rimando a capo dalla linea
    if i==0:
        print(linea)
    else:  
        lista_tmp = linea.split() #mette i dati della riga in umna lista temp
        print(lista_tmp)
        listaGiorni.append(lista_tmp[0])
        listaTemperature.append(int(lista_tmp[1]))
    i +=1
        
f.close()
print("**************")
print(listaGiorni)
print(listaTemperature)
media = sum(listaTemperature)/7
print("la media giornaliera = ", media)








"""    

f = open("TemperatureRimini.txt","a")
f.write("\n" + str(lista))
f.close()
"""
    
    
