nom=input("Ingrea tu nombre completo:")
def nombre():
    nomb=nom.split()
    ini=[nomb[0].upper() for nomb in nomb]
    return "".join(ini)
print(nombre())