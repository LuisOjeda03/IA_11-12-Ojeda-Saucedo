class Nodo:
    def __init__(self, valor:int):
        self.valor:int = valor
        self.izq:Nodo = None
        self.der:Nodo = None