from clase8 import Conjunto     
       
if __name__=='__main__':
    list1=Conjunto()
    list2=Conjunto()
    print("----LISTA 1-----")
    list1.cargaLista()
    print("----LISTA 2-----")
    list2.cargaLista()
    list1.ordena()
    list2.ordena()
    print(f"los elementos de la lista 1 son: {list1.mostrar()} ")
    print(f"los elementos de la lista 2 son: {list2.mostrar()} ")
    menu=int(input("1. Union de Conjuntos \n 2. Diferencia de Conjuntos \n 3.Igualdad de Conjuntos \n 0. Salir \n"))
    while menu != 0:
        
        if menu == 1:
            lista3=Conjunto()
            lista3= list1 +list2
            lista3.ordena()
            print(f"{lista3.mostrar()} ")
        if menu == 2:
            lista4=Conjunto()
            lista4= list1 - list2
            lista4.ordena()
            print(f"{lista4.mostrar()} ")
        if menu == 3:
            if list1 == list2:
                print(" lista 1 y lista 2 son iguales")
            else:
                print("Las listas 1 y 2 no son iguales")
        menu=int(input("1. Union de Conjuntos \n 2. Diferencia de Conjuntos \n 3.Igualdad de Conjuntos \n 0. Salir \n"))