def simplex_method(tableau):
    m, n = len(tableau), len(tableau[0])

    while True:
        # Looking for pivot
        col_i = next((i for i in range(n - 1) if tableau[-1][i] < 0), None)

        # Stop condition
        if col_i is None:
            break

        ratios = []
        for i in range(m - 1):
            if tableau[i][col_i] > 0:
                ratio = tableau[i][-1] / tableau[i][col_i]
                ratios.append(ratio)
            else:
                ratios.append(float('inf'))

        row_i = ratios.index(min(ratios))

        # Normalizing of the row
        pivot = tableau[row_i][col_i]
        tableau[row_i] = [el / pivot for el in tableau[row_i]]

        # Recalculation of values
        for i in range(m):
            if i == row_i:
                continue
            factor = tableau[i][col_i]
            tableau[i] = [tableau[i][j] - factor * tableau[row_i][j] for j in range(n)]

    return tableau


# example
tableau = [
    [2, -1, 0, -2, 1, 0, 16],
    [3, 2, 1, -3, 0, 0, 18],
    [-1, 3, 0, 4, 0, 1, 24],
    [-2, -3, 0, 1, 0, 0, 0]
]

result = simplex_method(tableau)
for row in result:
    print(row)

