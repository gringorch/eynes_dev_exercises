'''
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
'''
import numpy as np


def generar_matriz_consecutivos(valor_numeromasalto):

    n = valor_numeromasalto

    matriz = np.random.randint(n, size=(5, 5))

    for i in range(2):
        for j in range(2):
            
            a = matriz[i][j]
            # Valores en Horizontal
            bv = matriz[i][j+1]
            cv = matriz[i][j+2]
            dv = matriz[i][j+3]
            # Valores en Vertical
            bh = matriz[i+1][j]
            ch = matriz[i+2][j]
            dh = matriz[i+3][j]

            if a+1 == bv and  a+2 == cv and a+3 == dv:
                print(f'Valores Consecutivos desde ({i},{j}) hasta ({i},{j+3})')

            if a+1 == bh and  a+2 == ch and a+3 == dh:
                print(f'Valores Consecutivos desde ({i},{j}) hasta ({i+3},{j})')

    for i in range(3,5):
        for j in range(3,5):
            
            a = matriz[i][j]
            # Valores en Horizontal
            bv = matriz[i][j-1]
            cv = matriz[i][j-2]
            dv = matriz[i][j-3]
            # Valores en Vertical
            bh = matriz[i-1][j]
            ch = matriz[i-2][j]
            dh = matriz[i-3][j]

            if a-1 == bv and  a-2 == cv and a-3 == dv:
                print(f'Valores Consecutivos desde ({i},{j}) hasta ({i},{j-3})')

            if a-1 == bh and  a-2 == ch and a-3 == dh:
                print(f'Valores Consecutivos desde ({i},{j}) hasta ({i-3},{j})')

    return matriz

generar_matriz_consecutivos(6)