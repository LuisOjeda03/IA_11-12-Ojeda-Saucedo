Este proyecto resuelve el juego del 8 Puzzle utilizando el algoritmo A* con la heurística de Manhattan. Se busca encontrar la solución más eficiente para ordenar las piezas del puzzle utilizando un estado inicial hasta un estado final, haciendo jugadas, las cuales consisten en mover la ficha vacía.

Funcionamiento:
- Nodo: Cada estado del puzzle es representado por un objeto de la clase Nodo. 
Esta clase contiene información sobre el estado actual del puzzle, la posición de la posición vacía, y las métricas para el algoritmo.

- Algoritmo A*: Explora el espacio de posibles movimientos buscando la mejor ruta. Utiliza la heurística de Manhattan para calcular qué tan lejos está cada pieza de su posición final, y la función f = g + h para tomar decisiones sobre qué nodo explorar a continuación.

- Movimientos: El vacío (representado por el número 0) puede moverse hasta en cuatro direcciones posibles: arriba, abajo, izquierda o derecha, y el estado del puzzle se actualiza según el movimiento.

- Reconstrucción del camino: Cuando el algoritmo encuentra la solución, reconstruye el camino desde el estado final hasta el estado inicial y muestra el proceso que se siguió para la resolución del puzzle.

Estructura:
- Clase Nodo: Representa cada estado del puzzle, contiene métodos para el cálculo de la heurística de Manhattan, encontrar la posición del vacío y generar los posibles movimientos y generar el nuevo estado.

- Algoritmo A*: Es el algoritmo a cargo de verificar los posibles estados nuevos y encontrar la solución para luego mostrar el camino.

- Función precalculate_positions: Calcula las posiciones de los números en el estado final para calcular la heurística de Manhattan.
