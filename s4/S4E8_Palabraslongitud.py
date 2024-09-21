lista=input("ingresa una lista de palabras separadas por espacios:").split()
def orpal():
    return sorted(lista,key=len)
print(orpal())
