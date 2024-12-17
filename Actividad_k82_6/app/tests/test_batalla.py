import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.batalla import (
    es_mar, obtener_matriz_inicial, MAR, DISPARO_FALLADO, DISPARO_ACERTADO,
    colocar_e_imprimir_barcos, SUBMARINO, DESTRUCTOR, DESTRUCTOR_VERTICAL
)   


def disparar_para_pruebas(x, y, matriz) -> bool:
    if es_mar(x, y, matriz):
        matriz[y][x] = DISPARO_FALLADO
        return False
    elif matriz[y][x] == DISPARO_FALLADO or matriz[y][x] == DISPARO_ACERTADO:
        return False
    else:
        matriz[y][x] = DISPARO_ACERTADO
        return True

def test_es_mar():
    matriz = obtener_matriz_inicial()
    assert es_mar(0, 0, matriz) == True
    matriz[0][0] = DISPARO_FALLADO
    assert es_mar(0, 0, matriz) == False

def test_disparar_acierto():
    matriz = obtener_matriz_inicial()
    matriz[2][2] = SUBMARINO 
    result = disparar_para_pruebas(2, 2, matriz)
    assert result == True
    assert matriz[2][2] == DISPARO_ACERTADO

def test_disparar_fallo():
    matriz = obtener_matriz_inicial()
    result = disparar_para_pruebas(3, 3, matriz)
    assert result == False
    assert matriz[3][3] == DISPARO_FALLADO

def test_colocar_barcos():
    matriz = obtener_matriz_inicial()
    cantidad_barcos = 5
    matriz = colocar_e_imprimir_barcos(matriz, cantidad_barcos, "J1")
    barcos_colocados = sum(1 for fila in matriz for celda in fila if celda in [SUBMARINO, DESTRUCTOR, DESTRUCTOR_VERTICAL])
    assert barcos_colocados == 6  