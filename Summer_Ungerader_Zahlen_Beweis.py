import numpy as np
summe = 0
u = 1
vektor = np.zeros((0))
print("Die Summe einer Folge von ungeraden ganzen Zahlen größer null ergibt eine Quadratzahl")

for i in range(1,17,2):
    print(u)
    summe = i + summe
    print(summe)
    vektor.resize(u,u)
    #vektor= np.zeros((u,u))
    for j in range(0,u-1):
        for k in range(0,u-1):
            vektor[j,k]=1
    u = u+1
    print(vektor)

