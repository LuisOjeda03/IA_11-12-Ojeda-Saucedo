Tarea 1: Realizar un Árbol Binario de Búsqueda con los métodos Insertar, ImprimirArbol, Vacio y Buscar.
Alumnos: 
- Ojeda López Luis Enrique
- Saucedo Rodriguez Roberto Carlos

Descripción - Nodo:
Este proyecto consta de dos clases principales: Nodo y Árbol.
En la clase de Nodo se tienen 3 atributos (Valor, Izquierdo y Derecho), donde Valor es tipo entero,
e izquierdo y derecho son de tipo Nodo, por lo que tendran referencias a otros Nodos.

Descripción - Árbol:
En la clase de Árbol se tiene el atributo de raiz de tipo Nodo, el cual se inicializa en Null.
Cuenta con distintos métodos los cuales permiten manejar un Árbol de Búsqueda Binario:

- Vacio: Retorna falso si contiene algún elemento, de lo contrario regresa verdadero.
- Agregar: Toma un valor entero, y llama a un método privado llamado _agregarNodo con los parametros del valor y el Nodo raiz y comprueba a que Nodo asociarlo.
- Buscar: Toma un valor entero, y llama a un método privado llamado _buscarRecorrido con los parametros del valor y el Nodo raiz y recorre todo el Árbol hasta
encontrar el Nodo, si lo encuentra retorna True, caso contrario retorna False.
- ImprimirPreOrden: LLama a un método privado llamado _imprimirRecorridoPO el cual toma como parametro la raiz. Verifica si está vacio, en el caso de que no lo esté, imprimirá con
recursión todos los recorridos izquierdos, y luego todos los recorridos derechos.

- __main__: Método para comprobar la correcta función del Árbol, dónde se hace una instancia del Árbol y se agregan datos, se verifica que no esté vacio, se buscan datos y por último
se imprime el Árbol con un preOrden.


