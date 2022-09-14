def creare_lista():
    n=int(input('dati numarul de elemente: '))
    lista_creata=[]
    for j in range(n):
        element=eval(input('elementul '+str(j)+' este: '))
        while type(element)!=int:
            element=eval(input('Introduceti doar elemente de tip int! Elementul '+str(j)+' este: '))
            if type(element)==int:
                break
        lista_creata.append(element)
    return lista_creata
lista1=creare_lista()
print(lista1)