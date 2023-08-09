from math import isclose


def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])


    if columnas_matriz1 != filas_matriz2:
        print("Error,No se pueden multiplicar las matrices.")
        return None

    matriz_resultado = [[0 for y in range(columnas_matriz2)] for x in range(filas_matriz1)]

    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                matriz_resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz_resultado

def multiplicar_matriz_vector(matriz,vector):
    filas_matriz = len(matriz)
    columnas_matriz = len(matriz[0])
    filas_vector = len(vector)

    if columnas_matriz!= filas_vector:
        print("No se puede multiplicar la matriz debido al vector.")
        return None
    vector_resultado = [0 for x in range(filas_matriz)]


    for i in range(filas_matriz):
        for k in range(columnas_matriz):
            vector_resultado[i] += matriz[i][k] * vector[k]

    return vector_resultado

def barycentricCoords(A,B,C,P):

    areaPCB = abs((P[0]*C[1]+C[0]*B[1]+B[0]*P[1])-(P[1]*C[0]+C[1]*B[0]+B[1]*P[0]))
    areaACP = abs((A[0]*C[1]+C[0]*P[1]+P[0]*A[1])-(A[1]*C[0]+C[1]*P[0]+P[1]*A[0]))
    areaABP = abs((A[0]*B[1]+B[0]*P[1]+P[0]*A[1])-(A[1]*B[0]+B[1]*P[0]+P[1]*A[0]))
    areaABC = abs((A[0]*B[1]+B[0]*C[1]+C[0]*A[1])-(A[1]*B[0]+B[1]*C[0]+C[1]*A[0]))

    if areaABC == 0:
        return None
    u= areaPCB/areaABC
    v= areaACP/areaABC
    w= areaABP/areaABC

    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and isclose(u+v+w,1.0):
        return (u,v,w)
    else:
        return None
