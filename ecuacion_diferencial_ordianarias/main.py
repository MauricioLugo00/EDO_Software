# Importación de los métodos numéricos para resolver ecuaciones diferenciales
import metodos.Euler
import metodos.Euler_modificado
import metodos.Taylor
import metodos.Runge_kutta

def datos():
    """
    Función para capturar los datos de entrada de la ecuación diferencial.
    
    Formato de entrada de la ecuación:
    - La ecuación debe estar en función de f(x,y)
    - Usar operadores matemáticos de Python:
      * Multiplicación: *
      * División: /
      * Potencia: **
      * Funciones matemáticas: sin(), cos(), exp(), log(), sqrt()
    
    Ejemplos de entradas válidas:
    1. 'x-y'            # Ecuación lineal simple
    2. 'x**2 + y'       # Términos de x y y
    3. 'sin(x) + cos(y)'# Funciones trigonométricas
    4. 'exp(x) - y'     # Función exponencial
    
    IMPORTANTE:
    - Usar variables x e y exactamente con esos nombres
    - No usar espacios en blanco dentro de la ecuación
    """
    print("La ecuacion debe estar en funcion de f(x,y)")
    print("\nFormato de entrada:")
    print("- Use operadores: +, -, *, /, **")
    print("- Funciones: sin(), cos(), exp(), log(), sqrt()")
    print("- Ejemplos: 'x-y', 'x**2 + y', 'sin(x) + cos(y)'")
    
    ecuacion = input("  Ecuacion a evaluar: ")
    x0 = float(input("  Intervalo de evaluacion  x0: "))
    x1 = float(input("  Intervalo de evaluacion  x1: "))
    y0 = float(input("  Valor evaluado en     y(x0): "))
    n = int(input("  No. de Subintervalos: "))
    return ecuacion, x0, x1, y0, n


def metodo(opcion):
    """
    Función para seleccionar y ejecutar el método numérico elegido.
    
    Parámetros:
    - opcion: Número entero que representa el método a utilizar
    """
    if opcion == 1:
        ecuacion, x0, x1, y, n = datos()
        metodos.Euler.mEuler(ecuacion, x0, x1, y, n)

    elif opcion == 2:
        ecuacion, x0, x1, y, n = datos()
        metodos.Taylor.mTaylor(ecuacion, x0, x1, y, n)

    elif opcion == 3:
        ecuacion, x0, x1, y, n = datos()
        metodos.Euler_modificado.mEulerm(ecuacion, x0, x1, y, n)

    elif opcion == 4:
        ecuacion, x0, x1, y, n = datos()
        metodos.Runge_kutta.mRungeK4orden(ecuacion, x0, x1, y, n)
        
    else:
        print("Opcion incorrecta, vuelva a seleccionar otra opcion")


if __name__ == '__main__':
    """
    Bloque principal del programa.
    Permite al usuario seleccionar un método numérico para resolver
    ecuaciones diferenciales ordinarias.
    """
    ejecutar = True

    while(ejecutar):
        opcion = int(input('''
        - - - Integracion Numerica - - -\n
        Elegir un metodo:\n
            [1] Metodo de Euler 1er Orden
            [2] Metodo de Taylor 2do Orden
            [3] Metodo de Euler Modificado
            [4] Metodo de Runge - Kutta 4to Orden
            [5] Salir\n
        Opcion: '''))
        if opcion == 5:
            ejecutar = False
        else:
            metodo(opcion)
            ejecutar = False