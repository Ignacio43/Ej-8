

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
    
        for x in self.__lista:
            lista3.agregar(x)        
            for y in otro.__lista:
                if y not in self.__lista:
                    lista3.agregar(y)
        return lista3
    
    def __sub__(self,otro):
        for x in self.__lista:
            if x not in otro.__lista:
                lista4.agregar(x)
        return lista4
        
    def __eq__(self,otro):
        if len(self.__lista) != len(otro.__lista):
            return False
        else:
            for x in self.__lista:
                if x not in otro.__lista:
                    return False
            for y in otro.__lista:
                if y not in self.__lista:
                    return False
        return True
        
        