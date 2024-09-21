n=int(input("numero de filas:"))
m=int(input("numero de columnas:"))
def tabl(n,m):
    tab=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(i+j)%2==0:
                tab[i][j]=1
    return tab
for fila in tabl(n,m):
    print(fila)
