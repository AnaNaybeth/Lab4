
def voc_cons(palabra):
    palabra=palabra.lower()
    voc=0
    con=0
    for let in palabra:
        if let.isalpha():
            if let in "aeiou":
                voc+=1
            else:
                con+=1
    return voc,con
palabra=input()
voc,con=voc_cons(palabra)
print("vocales:",voc,"consonantes:",con)

