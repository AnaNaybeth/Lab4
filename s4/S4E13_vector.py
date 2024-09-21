def esca(v1, v2):
    if len(v1)!=len(v2):
        print("Los vectores deben tener la misma longitud")
        break

    return sum(x*y for x,y in zip(v1,v2))

v1=list(map(float, input("Ingrese (x, y, z): ").split()))


print(esca(v1,v2))
