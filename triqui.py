tablero: list[list[str]] = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
]

def imprimir_tablero(tab):
    nombres_col: str = "XYZ"
    
    print("    A   B   C")
    for i, fila in enumerate(tab):
        ncol = nombres_col[i].lower()
        print(ncol, end=" | ")  # recorre fila por fila
        for casilla in fila:  # recorre por casilla o columna 
            print(casilla, end=" | ")
        print(ncol)
        if i < 2:
            print("  -----------")
    print("    A   B   C")

def realizar_jugada(ficha: str, tab: list[list[str]], pos: tuple[int, int]) -> bool:
    movimiento_ok: bool = False

    if tab[pos[0]][pos[1]] == "*":
        tab[pos[0]][pos[1]] = ficha
        movimiento_ok = True

    return movimiento_ok

def lectura_usuario() -> tuple[int, int]:
    nombres_columnas = "ABC"
    nombres_filas = "xyz"
    valores = input("Ingrese la fila y columna (ej: x c): ").split()
    fila = nombres_filas.find(valores[0].lower())
    columna = nombres_columnas.find(valores[1].upper())

    return fila, columna

def colocar_ficha(ficha: str, tab: list[list[str]], posicion: tuple[int, int]) -> bool:
    movimiento_valido = False
    
    if tab[posicion[0]][posicion[1]] == "*":
        tab[posicion[0]][posicion[1]] = ficha
        movimiento_valido = True
    
    return movimiento_valido

def validar_empate(tab) -> bool: 
    hay_empate = True

    for fila in tab:
        for col in fila:
            if col == "*":
                hay_empate = False

    return hay_empate

def buscar_ganador(tab) -> str:
    for fila in tab:
        if fila[0] == fila[1] == fila[2] and fila[0] != "*":
            return fila[0]
        
    for num_col in range(3):
        if tab[0][num_col] == tab[1][num_col] == tab[2][num_col] and tab[0][num_col] != "*":
            return tab[0][num_col]
        
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] != "*":
        return tab[0][0]
    if tab[2][0] == tab[1][1] == tab[0][2] and tab[2][0] != "*":
        return tab[2][0]
    
    return None

def jugar() -> None:
    turno: str = "x"
    ganador: str | None = None

    while ganador is None:
        imprimir_tablero(tablero)
        print(f"Es el turno de {turno}")
        f, c = lectura_usuario()
        jugada_valida: bool = realizar_jugada(turno, tablero, (f, c))
    
        if jugada_valida:
            ganador = buscar_ganador(tablero)
            if ganador is None:
                if validar_empate(tablero):
                    ganador = "E"
                else:
                    turno = "o" if turno == "x" else "x"
        else:
            print("Movimiento no válido, intenta de nuevo.")

    if ganador == "E":
        print("Juego empatado, buen juego")
    else:
        print(f"El ganador del juego es {ganador}, buen juego")

# Iniciar el juego
jugar()








