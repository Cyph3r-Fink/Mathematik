import numpy as np
summe = 0
u = 1
vektor = np.zeros((0))
print("Die Summe einer Folge von ungeraden (ganzen) Zahlen (größer null) ergibt eine Quadratzahl")
print("Dies kann graphisch mit Matrizen bewiesen werden.")
print("")
Zahl = int(input("Geben Sie eine ungerade (ganze) Zahl (größer null) ein:"))
## Hier noch eine Abfrage, dass die Zahl größer Null und ungerade ist!
for i in range(1,Zahl+2,2):
    summe = i + summe
    print("Wir sind bei", i,".")
    print("Die Summe aller ungeraden Zahlen bis", i ,"beträgt", summe,".")
    vektor= np.zeros((u,u))
    for j in range(0,u-1):
        for k in range(0,u-1):
            vektor[j,k]=1
    u = u+1
    print(vektor)
    print("---------------------------------------------------------------------------")