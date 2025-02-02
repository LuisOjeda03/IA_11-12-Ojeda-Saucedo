# Tarea 1 - Parte 1: Arbol Binario con los metodos: Vacio, Agregar, Buscar e Imprimir
# Clase hecha por: 
# Ojeda Lopez Luis Enrique
# Saucedo Rodriguez Roberto Carlos

from Nodo import *

class Arbol:
    raiz:Nodo

    def __init__(self):
        self.raiz = None
    
    def vacio(self):
        return self.raiz == None
    
    def agregar(self, valor:int):
        self.raiz = self._agregarNodo(self.raiz, valor)

    def _agregarNodo(self, actual:Nodo, valor:int):
        if(actual is None):
            return Nodo(valor)
        if(valor < actual.valor):
            actual.izq = self._agregarNodo(actual.izq, valor)
        if(valor > actual.valor):
            actual.der = self._agregarNodo(actual.der, valor)
        return actual
    
    def buscar(self, valor:int):
        return self._buscarRecorrido(self.raiz, valor)
    
    def _buscarRecorrido(self, actual:Nodo, valor:int):
        if(actual is None):
            return False
        if(actual.valor == valor):
            return True
        if(valor < actual.valor):
            return self._buscarRecorrido(actual.izq, valor)
        else:
            return self._buscarRecorrido(actual.der, valor)
        
    def imprimirPreOrden(self):
        self._imprimirRecorridoPO(self.raiz)

    def _imprimirRecorridoPO(self, actual:Nodo):
        if(actual is not None):
            print(actual.valor)
            self._imprimirRecorridoPO(actual.izq)
            self._imprimirRecorridoPO(actual.der)

if __name__ == "__main__":
    arbol = Arbol()

    arbol.agregar(50)
    arbol.agregar(30)
    arbol.agregar(70)
    arbol.agregar(20)
    arbol.agregar(40)
    arbol.agregar(60)
    arbol.agregar(80)
    arbol.agregar(10)
    arbol.agregar(25)
    arbol.agregar(35)

    print(arbol.vacio())

    print(arbol.buscar(60))
    print(arbol.buscar(100))

    arbol.imprimirPreOrden()


    