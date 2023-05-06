class Conjunto:
    
    def __init__(self):
        self.__lista=[]
        
    def cargaLista(self):
        elemento=int(input("ingrese un elemento a cargar \n"))
        while elemento != 0:
            self.__lista.append(elemento)
            elemento=int(input("ingrese un elemento a cargar 0 para terminar \n"))
    
    def mostrar(self):
        return self.__lista
        
    def agregar(self,elemento):
        if elemento not in self.__lista:
            self.__lista.append(elemento)
    
    def ordena(self):
        return self.__lista.sort()
        
    def __add__(self,otro):
        lista3=[]
        for x in self.__lista:
            lista3.agregar(x)        
            for y in otro.__lista:
                if y not in self.__lista:
                    lista3.agregar(y)
        return lista3
    
    def __sub__(self,otro):
        lista4=[]
        for x in self.__lista:
            if x not in otro.__lista:
                lista4.agregar(x)
        return lista4
        
    def __eq__(self,otro):
        band=True
        if len(self.__lista) != len(otro.__lista):
            band=False
        else:
            for x in self.__lista:
                if x not in otro.__lista:
                    band=False
            for y in otro.__lista:
                if y not in self.__lista:
                    band=False
        return band

        
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