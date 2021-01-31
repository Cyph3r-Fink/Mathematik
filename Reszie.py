import numpy as np
u = 6
vektor = np.zeros((u,u))
print(vektor)
for j in range(0, u - 1):
    print(j)
    for k in range(0, u - 1):
        vektor[j, k] = 1
        print(vektor)
