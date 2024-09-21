texto=input("Ingrese el parrafo:")
def tex():
    li=texto.split()
    return len(li)
np=tex()
print("El texto tiene",np)