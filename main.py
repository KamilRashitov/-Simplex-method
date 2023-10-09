import math

from colorama import Fore, Style


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


print("Enter the coefficients of the main problem on one line with space delimiter")
coeff_main = list(map(int, input().split()))
print("Enter number of constraints")
n = int(input())
tableau = []
for i in range(n):
    tableau.append(list(map(int, input("Enter coefficients of " + str(i + 1) + "th constraint with space delimiter")
                           .split(' '))))
print("Enter the right-hand coefficients of the constraints on one line with space delimiter")
coeff_constr = list(map(int, input().split()))
coeff_constr.append(0)
print("Enter 1 if your problem is maximize and -1 if your problem is minimize")
k = int(input())
for i in range(len(coeff_main)):
    coeff_main[i] = coeff_main[i] * k
for i in range(len(coeff_main)):
    coeff_main[i] = coeff_main[i] * -1
print("Enter the approximation accuracy")
approximation_accuracy = int(input())
tableau.append(coeff_main.copy())
for i in range(0, len(tableau)):
    tableau[i].append(coeff_constr[i])

tableau = simplex_method(tableau)
print(f"Result: {math.floor(tableau[-1][-1] * 10**approximation_accuracy) / 10**approximation_accuracy}")

