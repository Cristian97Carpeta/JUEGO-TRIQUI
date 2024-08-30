tablero: list[list[str]] = [
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]

def imprimir_tablero(tab):
    print("  0   1   2")
    for i,fila in enumerate (tab):
        print(i, end=" ")#recorre fila por fila
        for casilla in fila: #recorre por casilla o columna 
            print(casilla, end= " | ")
        print("\n-----------")

imprimir_tablero(tablero)