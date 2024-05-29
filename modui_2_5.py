def get_matrix(n, m, value):
    matrix = []

    for row in range(n):
        one_row_of_matrix = []

        for col in range(m):
            one_row_of_matrix.append(value)

        matrix.append(one_row_of_matrix)
    return matrix

one_matrix = get_matrix(2, 2, 'попу')

two_matrix = get_matrix(3, 5, 'нужно')

three_matrix = get_matrix(4, 2, 'мыть')


for row in one_matrix:
    print(row)
for row in two_matrix:
    print(row)
for row in three_matrix:
    print(row)