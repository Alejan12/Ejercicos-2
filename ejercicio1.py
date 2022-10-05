ejes=((2,0),(2,1),(2,2),(2,3),(2,4),(1,2),(0,2),(2,2),(3,2),(4,2))
forma=len(ejes)
filas=5
columnas=5
figura=[[]]
for l in range(filas -1):
    figura+=[[]]

def estructura(i,j):
    cruz=False
    for valor in range(forma):
        if ejes[valor]==(i,j):
            figura[i].append("+")
            cruz=True
            break
    if cruz==False:
        figura[i].append(" ")
    return figura

for i in range(filas):
    for j in range(columnas):
        estructura(i,j)

def sacar_ejes():
    for z in range(len(figura)-1):
        print(str(figura[z])+"")
    print(figura[len(figura)-1])

sacar_ejes()