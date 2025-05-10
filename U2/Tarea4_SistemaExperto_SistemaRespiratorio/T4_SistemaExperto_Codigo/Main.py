from pyswip import Prolog

def iniciar_diagnostico():
    prolog = Prolog()
    prolog.consult("Reglas.pl")
    print("\nIniciando el sistema experto...\n")
    for _ in prolog.query("evaluar."):
        pass

# Bucle principal
while True:
    iniciar_diagnostico()
    respuesta = input("\n¿Desea realizar otro diagnóstico? (s/n): ").strip().lower()
    if respuesta != 's':
        print("Gracias por usar el sistema experto.")
        break
