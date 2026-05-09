import math
# ===== FUNCIONES =====
# ----- detalles -----
def cierre():
    print("------------------------------------")
    return
# ----- solicitudes -----
def pedirnumero():
    num1: float = float(input("dime el primer numero: "))
    num2: float = float(input("dime el segundo numero: "))
    return num1,num2
def pedirangulo():
    angulo: int = int(input("dime el angulo a calcular: "))
    return angulo
def medida():
    print("que medida quieres trabajar?")
    medi: str = input(": ")
    return medi
# --- operadores Álgebra ---
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b 
def potencia(a,b):
    return a**b
def radicacion(a,b):
    return a ** (1/b)
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
    return math.pi * r ** 2
def acuadrado(l):
    return l ** 2
def arectangulo(b,a):
    return b * a
def atrapecio(a,b,h):
    return (a + b) * h /2
def atriangulo(a,b):
    return a * b /2
# --- soluciones geometria ---
def circulo1():
    print("cual es el radio del circulo?")
    radio: float = float(input(": "))
    print(f"el área seria {acirculo(radio):.2f} {medida()}")
    return
def cuadrado1():
    print("cual es el lado del cuadrado?")
    lado: float = float(input(": "))
    print(f"el área seria {acuadrado(lado)} {medida()}")
    return
def rectangulo1():
    print("cual es la base y la altura del rectangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    print(f"el área seria {arectangulo(base,altura)} {medida()}")
    return
def trapecio1():
    print("Cual es la base mayor,menor y altura del trapecio?")
    baseM: float = float(input("Base mayor: "))
    basem: float = float(input("Base menor: "))
    altura: float = float(input("Altura:"))
    print(f"el área seria {atrapecio(baseM, basem, altura)} {medida()}")
    return
def triangulo1():
    print("cual es la base y la altura del triangulo?")
    base: float = float(input("base: "))
    altura: float = float(input("altura: "))
    print(f"el área seria {atriangulo(base,altura)} {medida()}")
    return

# ====== LOBBY ======
print("==========BIENVENIDO==========")
while True:
    print("¿Qué tipo de operación desea hacer?")
    print("1)Álgebra 2)trigonometria 3)Geometria(no disponible) 4)logaritmos(no disponible)")
    print("presione 0 para salir")
    tipo: int = int(input(": "))
    match tipo:
# --- Álgebra ---
        case 1:
            print("1)suma, 2)resta, 3)multiplicación, 4)división, 5)potencia, 6)raiz")
            print("que desea hacer?")
            opera: int = int(input(": "))
            match opera:
                case 1:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {suma(num1,num2)}")
                    cierre()
                case 2:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {resta(num1,num2)}")
                    cierre()
                case 3:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {multi(num1,num2)}")
                    cierre()
                case 4:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {divi(num1,num2)}")
                    cierre()
                case 5:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {potencia(num1,num2)}")
                    cierre()
                case 6:
                    num1, num2 = pedirnumero()
                    print(f"el resultado es {radicacion(num1,num2)}")
                    cierre()
                case _:
                    print("operación no valida")
                    cierre()
# --- Trigonometria ---
        case 2:
            print("1)Seno 2)Coseno 3)Tangente")
            opera: int = int(input(": "))
            match opera:
                case 1:
                    angulo = pedirangulo()
                    print(f"el seno de ese angulo seria {sin(angulo):.2f}")
                    cierre()
                case 2:
                    angulo = pedirangulo()
                    print(f"el coseno de ese angulo seria {cos(angulo):.2f}")
                    cierre()
                case 3: 
                    angulo = pedirangulo()
                    print(f"la tangente seria {tan(angulo):.2f}")
                    cierre()
                case _:
                    print("operación no valida")
                    cierre()
# --- Geometria ---
        case 3:
            print("la figura a calcular es 3D o 2D?")
            print("(Escribir '2d' o '3d')")
            forma: str = input(": ")
            forma = forma.upper()
            match forma:
                case "2D":
                        print("1)Área 2)Perimetro")
                        opera: int =int(input(": "))
                        match opera:
                            case 1:
                                print("escribe la figura que deseas calcular el área:")
                                print("1)circulo 2)cuadrado 3)rectangulo 4)trapecio 5)triangulo")
                                figura: int = int(input())
                                match figura:
                                    case 1:
                                        circulo1()
                                        cierre()
                                    case 2:
                                        cuadrado1()
                                        cierre()
                                    case 3:
                                        rectangulo1()
                                        cierre()
                                    case 4:
                                        trapecio1()
                                        cierre()
                                    case 5:
                                        triangulo1()
                                        cierre()
                                    case _:
                                        print("operación no valida")
                                        cierre()
                            case 2:
                                print("escribe la figura que deseas calcular el área:")
                                print("1)circulo 2)cuadrado 3)rectangulo 4)trapecio 5)triangulo")
                                figura: int = int(input())
                case _:
                    print("dimensión no valida")
                    cierre()
        case 0:
            print("==========HASTA PRONTO==========")
            break
        case _:
            print("Numero no existente, intentelo de nuevo")
            cierre()
#falta: 
# 1) hacer la geometria 3)volumen
# 2) hacer conversion de decimales a fraccion y viceversa 
# 3) suma, resta, multiplicacion y division de fracciones
# 4) usar el "for" e "in" para la calculadora
