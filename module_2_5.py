
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])   # добавляем список
        for j in range(m):
            matrix[i].append(value) # пишем в список значение
    return [matrix[i], matrix[j]]
print(get_matrix(2, 2, 10))


