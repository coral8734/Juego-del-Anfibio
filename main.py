import random
import math


class Anfibio():
    # Atributos de clase
    numeroAnfibios = 0
    puntosPorNadar = 1
    puntosPorSaltar = 2
    numeroUbicaciones = 0

    def __init__(self, nombre, puntuacion, ubicacion, numeroNado, numeroSalto):
        # Atributos de objeto
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.ubicacion = ubicacion
        self.historicoUbicaciones = list(
            [Coordenada(0.0, 0.0)])  # Inicializamos la lista de ubicaciones para cada anfibio
        self.numeroVidas = 3
        self.numeroNado = numeroNado
        self.numeroSalto = numeroSalto
        Anfibio.numeroAnfibios += 1


class Rana(Anfibio):
    longitudSalto = 3
    longitudNado = 2

    # Métodos nadar y saltar rana
    def nadar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudNado)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorNadar  # Actualización de su puntuación
        self.numeroNado += 1

    def saltar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudSalto)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorSaltar  # Actualización de su puntuación
        self.numeroSalto += 1


class Sapo(Anfibio):
    longitudSalto = 4
    longitudNado = 3

    # Métodos nadar y saltar sapos
    def nadar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudNado)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorNadar  # Actualización de su puntuación
        self.numeroNado += 1

    def saltar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudSalto)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorSaltar  # Actualización de su puntuación
        self.numeroSalto += 1


class Triton(Anfibio):
    longitudSalto = 1
    longitudNado = 5

    # Métodos nadar y saltar tritones
    def nadar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudNado)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorNadar  # Actualización de su puntuación
        self.numeroNado += 1

    def saltar(self):
        direccion = randomDireccion()
        self.ubicacion = calculaUbicacion(self.ubicacion, direccion, self.longitudSalto)
        self.historicoUbicaciones.append(self.ubicacion)
        self.puntuacion += Anfibio.puntosPorSaltar  # Actualización de su puntuación
        self.numeroSalto += 1


# Clase para almacenar las coordenadas x e y de un punto espacial
class Coordenada():

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Para determinar dirección aleatoria donde irá el anfibio
def randomDireccion():
    return random.randint(0, 359)


# para saber donde se encuentrará el anfibio tras un salto o un nado. Le pasamos la direccion y la longitud de avance, que
# es distinta para el nado o salto
def calculaUbicacion(ubicacionActual, direccion, longitudAvance):
    nuevaX = longitudAvance * math.cos(direccion)
    nuevaY = longitudAvance * math.sin(direccion)

    nuevaUbicacion = Coordenada(ubicacionActual.x + nuevaX, ubicacionActual.y + nuevaY)

    return nuevaUbicacion




# Codificación del estanque
def tipoTerreno(x, y):
    # Se devuelve 0 para agua, 1 para hoja y 2 para tierra

    if ((x >= 0) and (x <= 5) and (y >= 0) and (y <= 5)):
        return 0  # Celda M CASILLA CENTRAL PUNTO DE SALIDA INICIAL
    elif ((x > 5) and (x <= 10) and (y >= 0) and (y <= 5)):
        return 1  # Celda N
    elif ((x > 10) and (x <= 15) and (y >= 0) and (y <= 5)):
        return 0  # Celda O
    elif ((x > 15) and (x <= 20) and (y >= 0) and (y <= 5)):
        return 1  # Celda P
    elif ((x < 0) and (x >= -5) and (y >= 0) and (y <= 5)):
        return 0  # Celda L
    elif ((x < -5) and (x >= -10) and (y >= 0) and (y <= 5)):
        return 0  # Celda K
    elif ((x < -10) and (x >= -15) and (y >= 0) and (y <= 5)):
        return 0  # Celda J
    elif ((x < -15) and (x >= -20) and (y >= 0) and (y <= 5)):
        return 1  # Celda I


    elif ((x >= 0) and (x <= 5) and (y > 5) and (y <= 10)):
        return 1  # Celda E
    elif ((x > 5) and (x <= 10) and (y > 5) and (y <= 10)):
        return 0  # Celda F
    elif ((x > 10) and (x <= 15) and (y > 5) and (y <= 10)):
        return 1  # Celda G
    elif ((x > 15) and (x <= 20) and (y > 5) and (y <= 10)):
        return 1  # Celda H
    elif ((x < 0) and (x >= -5) and (y > 5) and (y <= 10)):
        return 0  # Celda D
    elif ((x < -5) and (x >= -10) and (y > 5) and (y <= 10)):
        return 0  # Celda C
    elif ((x < -10) and (x >= -15) and (y > 5) and (y <= 10)):
        return 0  # Celda B
    elif ((x < -15) and (x >= -20) and (y > 5) and (y <= 10)):
        return 1  # Celda A


    elif ((x >= 0) and (x <= 5) and (y < 0) and (y >= -5)):
        return 0  # Celda U
    elif ((x > 5) and (x <= 10) and (y < 0) and (y >= -5)):
        return 0  # Celda V
    elif ((x > 10) and (x <= 15) and (y < 0) and (y >= -5)):
        return 1  # Celda W
    elif ((x > 15) and (x <= 20) and (y < 0) and (y >= -5)):
        return 1  # Celda X
    elif ((x < 0) and (x >= -5) and (y < 0) and (y >= -5)):
        return 0  # Celda T
    elif ((x < -5) and (x >= -10) and (y < 0) and (y >= -5)):
        return 1  # Celda S
    elif ((x < -10) and (x >= -15) and (y < 0) and (y >= -5)):
        return 0  # Celda R
    elif ((x < -15) and (x >= -20) and (y < 0) and (y >= -5)):
        return 1  # Celda Q


    elif ((x >= 0) and (x <= 5) and (y < -5) and (y >= -10)):
        return 0  # Celda C1
    elif ((x > 5) and (x <= 10) and (y < -5) and (y >= -10)):
        return 0  # Celda D1
    elif ((x > 10) and (x <= 15) and (y < -5) and (y >= -10)):
        return 1  # Celda E1
    elif ((x > 15) and (x <= 20) and (y < -5) and (y >= -10)):
        return 1  # Celda F1
    elif ((x < 0) and (x >= -5) and (y < -5) and (y >= -10)):
        return 0  # Celda B1
    elif ((x < -5) and (x >= -10) and (y < -5) and (y >= -10)):
        return 1  # Celda A1
    elif ((x < -10) and (x >= -15) and (y < -5) and (y >= -10)):
        return 0  # Celda Z
    elif ((x < -15) and (x >= -20) and (y < -5) and (y >= -10)):
        return 1  # Celda Y

    else:
        return 2

    # Imprime datos de la evolución de todos los anfibios en el juego


def imprimirDatosAnfibios(listaAnfibios):
    print("  Nombre    Puntuación    Número de saltos   Número de nados   Lugar de deceso (x,y) ")
    print("---------------------------------------------------------------------------------")

    for i in listaAnfibios:
        print("{a1:^10}   {a2:^10}    {a3:^10}       {a4:^10}        {a5:^6.2f}    {a6:^6.2f}".format(a1=i.nombre,
                                                                                                      a2=i.puntuacion,
                                                                                                      a3=i.numeroSalto,
                                                                                                      a4=i.numeroNado,
                                                                                                      a5=i.ubicacion.x,
                                                                                                      a6=i.ubicacion.y))




def imprimirIntroduccionJuegoAnfibio(listaAnfibios):
    numeroTotalAnfibios = 0
    for i in listaAnfibios:
        numeroTotalAnfibios = i.numeroAnfibios

    print("")
    print("___________________________________________________________________________________")
    print("|                                                                                  |")
    print("|                          Juego de los anfibios                                   |")
    print("|                                                                                  |")
    print("________________________________________________________________ __________________")
    print("")
    print("| Numero de anfibios: %s" % numeroTotalAnfibios)


# Instanciar los anfibios

listaAnfibios = list()  # Creamos una lista donde vamos a almacenar todos los anfibios con sus datos

# Se instancian 5 ranas.
# Se ejecuta su acción en el juego para cada una de las ranas, hasta que no le quedan vidas.
for i in range(5):

    rana = Rana("Rana%d" % i, 0, Coordenada(0, 0), 0, 0)

    listaAnfibios.append(rana)  # Añadimos cada rana a la lista de anfibios

    while (rana.numeroVidas >= 1):

        if (tipoTerreno(rana.ubicacion.x,
                        rana.ubicacion.y) == 0):  # La proxima ubicación de la rana es agua y por ello nadará
            rana.nadar()
        elif (tipoTerreno(rana.ubicacion.x, rana.ubicacion.y) == 1):
            rana.saltar()
        else:
            rana.saltar()
            rana.numeroVidas -= 1

for i in range(5):

    sapo = Sapo("Sapo%d" % i, 0, Coordenada(0, 0), 0, 0)

    ubicacionInicial = Coordenada(0, 0)
    listaAnfibios.append(sapo)

    while (sapo.numeroVidas >= 1):

        if (tipoTerreno(sapo.ubicacion.x, sapo.ubicacion.y) == 0):
            sapo.nadar()
        elif (tipoTerreno(sapo.ubicacion.x, sapo.ubicacion.y) == 1):
            sapo.saltar()
        else:
            sapo.saltar()
            sapo.numeroVidas -= 1

for i in range(5):

    triton = Triton("Triton%d" % i, 0, Coordenada(0, 0), 0, 0)

    listaAnfibios.append(triton)

    while (triton.numeroVidas > 0):

        if (tipoTerreno(triton.ubicacion.x, triton.ubicacion.y) == 0):
            triton.nadar()
        elif (tipoTerreno(triton.ubicacion.x, triton.ubicacion.y) == 1):
            triton.saltar()
        else:

            triton.saltar()
            triton.numeroVidas -= 1


# Imprime el histórico de saltos del anfibio ganador
def imprimirHistoricoAnfibioGanador(listaAnfibios):

    listaBuena = sorted(listaAnfibios, key=lambda x: x.puntuacion, reverse=True)

    print("------------------------------------------------\n")
    print("Anfibio ganador:", listaBuena[0].nombre)
    print("Puntuacion:", listaBuena[0].puntuacion)
    print("------------------------------------------------\n")

    for i in listaBuena[0].historicoUbicaciones:
        print("Ubicacion X:",format(i.x, '0.2f'),"Ubicacion Y:", format(i.y, '0.2f'))





imprimirIntroduccionJuegoAnfibio(listaAnfibios)
imprimirDatosAnfibios(listaAnfibios)
imprimirHistoricoAnfibioGanador(listaAnfibios)

