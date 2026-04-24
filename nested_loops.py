# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    list_of_lists = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            list_of_lists.append(matrix[x][y])
    return list_of_lists


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    list_row_sums = []

    for x in range(len(matrix)):
        list_row_sums.append(0)
        for y in range(len(matrix[x])):
            list_row_sums[x] += matrix[x][y]

    return list_row_sums
            

def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    list_col_sums = []

    for x in range(len(matrix)+1):
        suma_actual = 0
        for y in range(len(matrix)):
            suma_actual += matrix[y][x]
        list_col_sums.append(suma_actual)
        
    return list_col_sums
            

matrix =   [[1, 2, 3], [4, 5, 6]]
print(col_sums(matrix))