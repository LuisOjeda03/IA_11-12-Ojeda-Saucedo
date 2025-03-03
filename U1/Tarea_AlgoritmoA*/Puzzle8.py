# Proyecto: 8 Puzzle con algoritmo A* y Manhattan
# Desarrollador por: Ojeda Lopez Luis Enrique, Saucedo Rodriguez Roberto Carlos
# Materia: Inteligencia Artificial 11:00 - 12:00 am

import heapq
import copy
import time

# Variable global para las posiciones de los numeros del estado final
posiciones = {}

# Representamos todo el tablero como un Nodo
class Nodo:

    # Inicializacion de constructor
    def __init__(self, estado, posicionVacio, g, h, padre):
        self.estado = estado
        self.posicionVacio = posicionVacio
        self.g = g
        self.h = h
        self.f = g + h
        self.padre = padre
    
    # Metodo less than usado para comparar el valor f(n)
    def __lt__(self, otro):
        return self.f < otro.f
    
    # Calculamos el valor h(n) (Manhattan) de cada posicion y la sumamos
    def calcular_manhattan(self):
        contador = 0
        for i in range(3):
            for j in range(3):
                valor = self.estado[i][j]
                if valor != 0:
                    y, x = posiciones[self.estado[i][j]]
                    contador += (abs(x - j) + abs(y - i))
        return contador
    
    # Encontramos la posicion del vacio para poder saber que movimientos se pueden realizar
    def encontrar_vacio(self):
        for i in range(3): #Y
            for j in range(3): #X
                if self.estado[i][j] == 0:
                    self.posicionVacio = tuple((i, j))
                    return (i, j)

    # Se guarda en un arreglo todos los movimientos posibles a partir de la posicion del vacio y 
    # se almacena el desplazamiento
    def movimientos_posibles(self, y, x):
        movimientos = []
        if y > 0: movimientos.append((-1, 0))  # Arriba
        if y < 2: movimientos.append((1, 0))   # Abajo
        if x > 0: movimientos.append((0, -1))  # Izquierda
        if x < 2: movimientos.append((0, 1))   # Derecha
        return movimientos
    
    
    # Se reciben los desplazamientos para cada movimiento y se intercambia el vacio con la ficha obtenida
    # haciendo uso de una variable auxiliar
    def calcular_juego(self, desplazamientoY, desplazamientoX):
        actualYvacio , actualXvacio = self.posicionVacio 

        nuevoY = actualYvacio + desplazamientoY
        nuevoX = actualXvacio + desplazamientoX

        valorGuardado = self.estado[nuevoY][nuevoX]
        estadoNuevo = copy.deepcopy(self.estado) # Se crea una copia diferente

        # Intercambio de valores entre numero y 0
        estadoNuevo[nuevoY][nuevoX] = 0
        estadoNuevo[actualYvacio][actualXvacio] = valorGuardado

        # Podemos retornar el nodo creado
        return Nodo(estadoNuevo, (nuevoY, nuevoX), self.g + 1, 0, self)

    # Funcion principal del algoritmo A* 
    def AEstrella(self, estadoInicial, estadoFinal):

        # Se define una lista abierta (cola de prioridad) 
        # y una lista cerrada(set que almacena los estados visitados para evitar ciclos)
        listaAbierta = []
        listacerrada = set()
        
        # Obtiene las coordenadas del espacio vacio del estado inicial
        y, x = self.encontrar_vacio()
        
        # Se agrega el primer nodo a la cola de prioridad
        heapq.heappush(listaAbierta, Nodo(estadoInicial, (y,x), 0, self.calcular_manhattan(), None))

        while listaAbierta:

            # Saca el elemento con menor F(n) de la cola de prioridad gracias a _lt_
            nodoActual = heapq.heappop(listaAbierta)
            
            # Pasar el estado actual a una tupla de tuplas permite la comparacion con set()
            estadoActualTupla = tuple(map(tuple, nodoActual.estado))  
            # Si el estado actual ya se visito la iteracion actual se termina
            if estadoActualTupla in listacerrada:
                continue  # Ya visitamos este estado antes
            listacerrada.add(estadoActualTupla)
            
            # Se encuentra la solucion 
            if nodoActual.estado == estadoFinal:
                # Terminamos el tiempo total del programa
                end_time = time.time()
                elapsed_time = end_time - start_time
                print()
                print("Solución encontrada")
                print("=========")
                for paso in self.reconstruir_camino(nodoActual):    # Se recorre el camino
                    for fila in paso:   # Se recorre fila por fila en cada paso del camino
                        print(fila)
                    print("=========")
                print(f"Numero de movimientos realizados: {nodoActual.g}")
                print(f"Tiempo: {elapsed_time}")
                return
            
            # Se encuentra el vacio para calcular los movimientos posibles actuales
            x, y = nodoActual.encontrar_vacio()
            movimientos = nodoActual.movimientos_posibles(y,x)

            for dx,dy in movimientos:
                # Agregar los posibles movimientos en listaVecinos
                nodoVecino = nodoActual.calcular_juego(dy,dx)
                nodoVecino.g = nodoActual.g + 1
                nodoVecino.h = nodoVecino.calcular_manhattan()
                nodoVecino.f = nodoVecino.g + nodoVecino.h
                nodoVecino.padre = nodoActual
                
                heapq.heappush(listaAbierta, nodoVecino)

        print("Solucion no encontrada")

    # Reconstruccion del camino desde el nodo final hasta el nodo inicial
    def reconstruir_camino(self,nodo):
        camino = [] 
        while nodo:
            camino.append(nodo.estado)
            nodo = nodo.padre
        return reversed(camino)

# Función para calcular las posiciones de cada elemento final, util para el calculo de Manhattan
def precalculate_positions(matrizFinal):
    global posiciones
    posiciones = {}
    for i in range(3):
        for j in range(3):
            posiciones[matrizFinal[i][j]] = (i, j)

# Main
if __name__ == "__main__":
    inicio = []
    final = []
    
    # Se lee el estado inicial
    for i in range(3):
        fila = [int(input(f"Ingrese el valor para el estado inicial ({i+1}, {j+1}): ")) for j in range(3)]
        inicio.append(fila)
    
    # Se lee el estado final
    for i in range(3):
        fila = [int(input(f"Ingrese el valor para el estado final ({i+1}, {j+1}): ")) for j in range(3)]
        final.append(fila)
    
    # Empieza a contar el tiempo del algorimo
    start_time = time.time()
    # Se calculan las posiciones del estado final
    precalculate_positions(final)
    #Se define el nodo inicial con el estado inicial y se inicia el algoritmo A*
    nodo = Nodo(inicio, None, 0, 0, None)
    nodo.AEstrella(inicio, final)