import math


# ===== FUNCIONES =====
# ----- detalles -----
def cierre():
    print("------------------------------------\n")


def error(mensaje: str):
    print(f"[ERROR]: {mensaje}")


def resultado(operacion, mensaje: str = "El resultado es", añadido: str = ""):
    print(f"{mensaje}: {operacion:.3f}{añadido}")


# ----- solicitudes -----
def pedirnumero():
    num1: float = float(input("Ingresar primer numero: "))
    num2: float = float(input("Ingresar segundo numero: "))
    return num1, num2


def pedirangulo():
    angulo: int = int(input("Ingresar ángulo a calcular (grados): "))
    return angulo


def medida():
    medi: str = input("¿Que medida quieres trabajar (m, km, cm, etc)?: ")
    return medi


# --- operadores Álgebra ---
def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    return a / b


def potencia(a, b):
    return a**b


def radicacion(a, b):
    return a ** (1 / b)


# --- operadores Trigonometria ---
def tan(angulo):
    rad = math.radians(angulo)
    tan = math.tan(rad)
    return tan


def sin(angulo):
    rad = math.radians(angulo)
    sin = math.sin(rad)
    return sin


def cos(angulo):
    rad = math.radians(angulo)
    cos = math.cos(rad)
    return cos


# --- operadores geometria ---
def acirculo(r):
    return math.pi * r**2


def acuadrado(l):
    return l**2


def arectangulo(b, a):
    return b * a


def atrapecio(a, b, h):
    return (a + b) * h / 2


def atriangulo(a, b):
    return a * b / 2


# --- soluciones geometria ---
def circulo1():
    print("¿Cual es el radio del circulo?")
    radio: float = float(input(": "))
    return acirculo(radio)


def cuadrado1():
    print("¿Cual es el lado del cuadrado?")
    lado: float = float(input(": "))
    return acuadrado(lado)


def rectangulo1():
    print("cual es la base y la altura del rectangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    return arectangulo(base, altura)


def trapecio1():
    print("Cual es la base mayor,menor y altura del trapecio?")
    baseM: float = float(input("Base mayor: "))
    basem: float = float(input("Base menor: "))
    altura: float = float(input("Altura:"))
    return atrapecio(baseM, basem, altura)


def triangulo1():
    print("cual es la base y la altura del triangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    return atriangulo(base, altura)


# ====== LOBBY ======
print("==========BIENVENIDO==========")
while True:
    print("¿En que área desea trabajar?")
    print(
        "1) Álgebra \n2) Trigonometria \n3) Geometria(no disponible) \n4) Logaritmos(no disponible)"
    )
    print("-- Presione 0 para salir")
    tipo: int = int(input(": "))
    match tipo:
        # --- Álgebra ---
        case 1:
            print("\n¿Qué operación desea hacer?")
            print(
                "1) Suma \n2) Resta \n3) Multiplicación \n4) División \n5) Potencia \n6) Raíz"
            )
            opera: int = int(input(": "))
            match opera:
                case 1:
                    num1, num2 = pedirnumero()
                    resultado(suma(num1, num2))
                    cierre()
                case 2:
                    num1, num2 = pedirnumero()
                    resultado(resta(num1, num2))
                    cierre()
                case 3:
                    num1, num2 = pedirnumero()
                    resultado(multi(num1, num2))
                    cierre()
                case 4:
                    num1, num2 = pedirnumero()
                    resultado(divi(num1, num2))
                    cierre()
                case 5:
                    num1, num2 = pedirnumero()
                    resultado(potencia(num1, num2))
                    cierre()
                case 6:
                    num1, num2 = pedirnumero()
                    resultado(radicacion(num1, num2))
                    cierre()
                case _:
                    error("Operación no valida")
                    cierre()
        # --- Trigonometria ---
        case 2:
            print("\n¿Qué operación desea hacer?")
            print("1) Seno \n2) Coseno \n3) Tangente")
            opera: int = int(input(": "))
            match opera:
                case 1:
                    angulo = pedirangulo()
                    resultado(sin(angulo), "El seno del angulo es", "°")
                    cierre()
                case 2:
                    angulo = pedirangulo()
                    resultado(cos(angulo), "El coseno del angulo es", "°")
                    cierre()
                case 3:
                    angulo = pedirangulo()
                    resultado(tan(angulo), "La tangente del angulo es", "°")
                    cierre()
                case _:
                    error("Operación no valida")
                    cierre()
        # --- Geometria ---
        case 3:
            print("\nLa figura a calcular es 3D o 2D?")
            print("(Escribir '2d' o '3d')")
            forma: str = input(": ")
            print("¿Qué operación desea hacer?")
            match forma.upper():
                case "2D":
                    print("1) Área \n2) Perimetro")
                    opera: int = int(input(": "))
                    match opera:
                        # areas
                        case 1:
                            print("Escribe la figura que deseas calcular el área:")
                            print(
                                "1) Circulo \n2) Cuadrado \n3) Rectangulo \n4) Trapecio \n5) Triangulo"
                            )
                            figura: int = int(input(": "))
                            match figura:
                                case 1:
                                    resultado(circulo1(), "El área es", medida())
                                    cierre()
                                case 2:
                                    resultado(cuadrado1(), "El área es", medida())
                                    cierre()
                                case 3:
                                    resultado(rectangulo1(), "El área es", medida())
                                    cierre()
                                case 4:
                                    resultado(trapecio1(), "El área es", medida())
                                    cierre()
                                case 5:
                                    resultado(triangulo1(), "El área es", medida())
                                    cierre()
                                case _:
                                    error("Operación no valida")
                                    cierre()
                        # perimetros
                        case 2:
                            print("Escribe la figura que deseas calcular el perimetro:")
                            print(
                                "1) Circulo \n2) Cuadrado \n3) Rectangulo \n4) Trapecio \n5) Triangulo"
                            )
                            figura: int = int(input(": "))
                case _:
                    error("Dimensión inválida")
                    cierre()
        case 0:
            print("==========HASTA PRONTO==========")
            break
        case _:
            error("Área inexistente")
            cierre()


# falta:
# 1) Colocar tries
# 2) hacer la geometria (volumen)
# 3) hacer conversion de decimales a fraccion y viceversa
# 4) suma, resta, multiplicacion y division de fracciones
# 5) usar el "for" e "in" para la calculador
# 6) Colocar textos de colores
