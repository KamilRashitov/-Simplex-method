import numpy as np

def solve(con, a, B, approx, mn):
    try:
        number_of_constraints = len(con)
        number_of_equations = len(a)
        C = np.zeros(number_of_constraints + number_of_equations)

        for i in range(number_of_constraints + number_of_equations):
            if i < number_of_constraints:
                C[i] = con[i]
            else:
                C[i] = 0

        A = np.zeros((number_of_equations, number_of_constraints + number_of_equations))

        for i in range(number_of_equations):
            coef = 1
            if B[i] < 0:
                coef = -1
                B[i] *= -1

            for j in range(number_of_constraints + number_of_equations):
                if j < number_of_constraints:
                    A[i][j] = a[i][j]
                else:
                    if j - number_of_constraints != i:
                        A[i][j] = 0
                    else:
                        A[i][j] = 1

        basis = [-1] * number_of_equations

        for i in range(number_of_equations):
            for j in range(number_of_constraints + number_of_equations):
                if A[i][j] == 1:
                    op = True
                    for k in range(number_of_equations):
                        if k != i and A[k][j] != 0:
                            op = False
                            break
                    if op:
                        basis[i] = j
                        break

        for i in range(number_of_equations):
            if basis[i] == -1:
                raise ValueError("not applicable")

        n = A.shape[0]
        m = A.shape[1]
        best = False
        negate = 1

        if mn:
            negate = -1

        while not best:
            CjZj = np.zeros(m)
            best = True
            pivot_col_coef = 0
            pivot_col = 0

            for i in range(m):
                zj = 0

                for j in range(n):
                    zj += C[basis[j]] * A[j][i]

                CjZj[i] = C[i] - zj
                CjZj[i] *= negate

                if CjZj[i] > 0:
                    best = False

                    if pivot_col_coef < CjZj[i]:
                        pivot_col_coef = CjZj[i]
                        pivot_col = i

            if not best:
                pivot_row_coef = -1
                pivot_row = -1

                for i in range(n):
                    if B[i] / A[i][pivot_col] >= 0 and (B[i] / A[i][pivot_col] < pivot_row_coef or pivot_row == -1):
                        pivot_row = i
                        pivot_row_coef = B[i] / A[i][pivot_col]

                if pivot_row == -1:
                    raise ValueError("not applicable")

                basis[pivot_row] = pivot_col

                for i in range(m):
                    if i != pivot_col:
                        A[pivot_row][i] /= A[pivot_row][pivot_col]

                B[pivot_row] /= A[pivot_row][pivot_col]
                A[pivot_row][pivot_col] = 1

                for i in range(n):
                    for j in range(m):
                        if i != pivot_row and j != pivot_col:
                            A[i][j] -= A[i][pivot_col] * A[pivot_row][j]

                    if i != pivot_row:
                        B[i] -= A[i][pivot_col] * B[pivot_row]
                        A[i][pivot_col] = 0

        res = 0

        for i in range(n):
            res += C[basis[i]] * B[i]

        print(f"{res:.{approx}f}")

    except Exception as e:
        print("Not applicable")

if __name__ == "__main__":
    print("Number of constraints")
    n = int(input())
    con = [float(input()) for _ in range(n)]

    print("Number of equations")
    m = int(input())
    a = [[float(x) for x in input().split()] for _ in range(m)]

    print("right hand side")
    B = [float(input()) for _ in range(m)]

    approx = int(input())

    mn = input() == "min"

    solve(con, a, B, approx, mn)
