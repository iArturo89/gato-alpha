import random

tablero = [[1, "|", 2, "|", 3],
           ["-", "-", "-", "-", "-"],
           [4, "|", 5, "|", 6],
           ["-", "-", "-", "-", "-"],
           [7, "|", 8, "|", 9]]


def imprimirTablero():
    for fila in tablero:
        for elemento in fila:
            print(elemento, end="  ")
        print("\n")


def colocar_en_tablero(jugador, posicion):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == posicion:
                tablero[fila][columna] = jugador


def vereficar_casilla(jugador):
    return any(posicion in range(1, 10) for fila in tablero for posicion in fila)


def vereficar_empate():
    for fila in range(0, 5, 2):
        for columna in range(0, 5, 2):
            if tablero[fila][columna] in range(1, 10):
                return False
    return True


def vereficar_ganador(jugador):
    # Horizontal
    for fila in range(0, 5, 2):
        if tablero[fila][0] == jugador == tablero[fila][2] == tablero[fila][4]:
            return True

    # Vertical
    for columna in range(0, 5, 2):
        if tablero[0][columna] == jugador == tablero[2][columna] == tablero[4][columna]:
            return True

    # Diagonal
    if tablero[0][0] == jugador == tablero[2][2] == tablero[4][4]:
        return True
    if tablero[0][4] == jugador == tablero[2][2] == tablero[4][0]:
        return True

    return False


def posicionValida():
    posiciones = []
    for fila in range(0, 5, 2):
        for columna in range(0, 5, 2):
            if tablero[fila][columna] in range(1, 10):
                posiciones.append(tablero[fila][columna])
    return posiciones


def minimax(tablero, profundidad, esMaximizando, alpha, beta):
    jugador1 = "x"
    jugador2 = "O"

    if vereficar_ganador(jugador1):
        return -1
    elif vereficar_ganador(jugador2):
        return 1
    elif vereficar_empate():
        return 0

    if esMaximizando:
        mejorPuntaje = float("-inf")
        for fila in range(0, 5, 2):
            for columna in range(0, 5, 2):
                if tablero[fila][columna] in range(1, 10):
                    posicion = tablero[fila][columna]
                    tablero[fila][columna] = jugador2
                    puntaje = minimax(tablero, profundidad + 1, False, alpha, beta)
                    tablero[fila][columna] = posicion
                    mejorPuntaje = max(puntaje, mejorPuntaje)
                    alpha = max(alpha, mejorPuntaje)
                    if beta <= alpha:  # Poda alfa-beta
                        break  # Detener la exploración de ramas innecesarias
        return mejorPuntaje
    else:
        mejorPuntaje = float("inf")
        for fila in range(0, 5, 2):
            for columna in range(0, 5, 2):
                if tablero[fila][columna] in range(1, 10):
                    posicion = tablero[fila][columna]
                    tablero[fila][columna] = jugador1
                    puntaje = minimax(tablero, profundidad + 1, True, alpha, beta)
                    tablero[fila][columna] = posicion
                    mejorPuntaje = min(puntaje, mejorPuntaje)
                    beta = min(beta, mejorPuntaje)
                    if beta <= alpha:  # Poda alfa-beta
                        break  # Detener la exploración de ramas innecesarias
        return mejorPuntaje


def movimientoIA():
    mejorPuntaje = float("-inf")
    mejorMovimiento = None
    alpha = float("-inf")
    beta = float("inf")
    for fila in range(0, 5, 2):
        for columna in range(0, 5, 2):
            if tablero[fila][columna] in range(1, 10):
                posicion = tablero[fila][columna]
                tablero[fila][columna] = "O"
                puntaje = minimax(tablero, 0, False, alpha, beta)
                tablero[fila][columna] = posicion
                if puntaje > mejorPuntaje:
                    mejorPuntaje = puntaje
                    mejorMovimiento = posicion
    return mejorMovimiento


def jugarGato():
    jugador1 = "x"
    turno = 1

    while not vereficar_ganador(jugador1) and not vereficar_ganador("O") and not vereficar_empate():
        imprimirTablero()
        print("\n")

        if turno == 1:
            posicion = int(input("Jugador 1, ingresa el número: "))
            while posicion not in posicionValida():
                posicion = int(input("Posición inválida. Jugador 1, ingresa otro número: "))
            colocar_en_tablero(jugador1, posicion)
            turno = 2
        else:
            posicion = movimientoIA()
            colocar_en_tablero("O", posicion)
            turno = 1

    imprimirTablero()
    print("\n")

    if vereficar_ganador(jugador1):
        print("¡Ganó el jugador 1!")
    elif vereficar_ganador("O"):
        print("¡Ganó la IA!")
    else:
        print("Empate")


jugarGato()
