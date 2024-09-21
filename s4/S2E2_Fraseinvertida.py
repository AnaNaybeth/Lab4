fras=input("Ingrese una frase:")
def palinv(fras):
   pal=fras.split()
   inv=[pal[::-1] for pal in pal]
   nv=" ".join(inv)
   return nv
print(palinv(fras))
