from colorama import Fore, Back, Style, init
def print_tableau(tableau, column, row):
    m, n = len(tableau), len(tableau[0])
    for i in range(m):
        if i == column:
            for j in range(n):
                print(f"{Fore.CYAN}{tableau[i][j]:10.2f}{Style.RESET_ALL}", end=" ")
        else:
            for j in range(n):
                if j == row:
                    print(f"{Fore.MAGENTA}{tableau[i][j]:10.2f}{Style.RESET_ALL}", end=" ")
                else:
                    print(f"{tableau[i][j]:10.2f}", end=" ")
        print()

def simplex_method(tableau):
    m, n = len(tableau), len(tableau[0])
    step = 0

    while True:
        print(f"Step {step}:\n")
        print_tableau(tableau, -1, -1)

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

        pivot_value = tableau[row_i][col_i]
        print(f"Pivot Column (Column {col_i + 1}):")
        print_tableau(tableau, col_i, -1)
        print(f"Pivot Row (Row {row_i + 1}):")
        print_tableau(tableau, -1, row_i)

        # Normalizing of the row
        tableau[row_i] = [el / pivot_value for el in tableau[row_i]]
        print(f"Normalize Row {row_i + 1}:")
        print_tableau(tableau, -1, row_i)

        # Recalculation of values
        for i in range(m):
            if i == row_i:
                continue
            factor = tableau[i][col_i]
            tableau[i] = [tableau[i][j] - factor * tableau[row_i][j] for j in range(n)]
        print(f"Recalculate Rows:")
        print_tableau(tableau, -1, -1)

        step += 1

    print(f"Step {step}:\n")
    print_tableau(tableau, -1, -1)
    return tableau

tableau = [
    [2, -1, 0, -2, 1, 0, 16],
    [3, 2, 1, -3, 0, 0, 18],
    [-1, 3, 0, 4, 0, 1, 24],
    [-2, -3, 0, 1, 0, 0, 0]
]

table_ans = simplex_method(tableau)
print(f"Result: {table_ans[-1][-1]}")
