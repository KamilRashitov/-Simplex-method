#include <bits/stdc++.h>
using namespace std;

void solve(std::vector<double> con, std::vector<std::vector<double>> a, std::vector<double> B, int approx, bool mn)
{
    try
    {
        int number_of_constrains = con.size();
        int numbers_of_equations = a.size();
        std::vector<double> C(number_of_constrains + numbers_of_equations);
        for (int i = 0; i < number_of_constrains + numbers_of_equations; i++)
        {
            if (i < number_of_constrains)
            {
                C[i] = con[i];
            }
            else
            {
                C[i] = 0;
            }
        }
        std::vector<std::vector<double>> A(numbers_of_equations);
        for (int i = 0; i < numbers_of_equations; i++)
        {
            int coef = 1;
            if (B[i] < 0)
            {
                coef = -1;
                B[i] *= -1;
            }
            for (int j = 0; j < numbers_of_equations + number_of_constrains; j++)
            {
                if (j < number_of_constrains)
                {
                    A[i].push_back(a[i][j]);
                }
                else
                {
                    if (j - number_of_constrains != i)
                    {
                        A[i].push_back(0);
                    }
                    else
                    {
                        A[i].push_back(1);
                    }
                }
            }
        }

        std::vector<int> basis(numbers_of_equations, -1);
        for (int i = 0; i < numbers_of_equations; i++)
        {
            for (int j = 0; j < numbers_of_equations + number_of_constrains; j++)
            {
                if (A[i][j] == 1)
                {
                    bool op = true;
                    for (int k = 0; k < numbers_of_equations; k++)
                    {
                        if (k != i && A[k][j] != 0)
                        {
                            op = false;
                            break;
                        }
                    }
                    if (op)
                    {
                        basis[i] = j;
                        break;
                    }
                }
            }
        }
        for (int i = 0; i < numbers_of_equations; i++)
        {
            if (basis[i] == -1)
            {
                throw invalid_argument("not applicable");
            }
        }
        int n = A.size(), m = A[0].size();
        bool best = false;
        int negate = 1;
        if (mn)
        {
            negate = -1;
        }
        while (!best)
        {
            vector<double> CjZj(m);
            best = true;
            double pivot_col_coef = 0;
            int pivot_col = 0;

            for (int i = 0; i < m; i++)
            {
                double zj = 0;
                for (int j = 0; j < n; j++)
                {
                    zj += C[basis[j]] * A[j][i];
                }
                CjZj[i] = C[i] - zj;
                CjZj[i] *= negate;
                if (CjZj[i] > 0)
                {
                    best = false;
                    if (pivot_col_coef < CjZj[i])
                    {
                        pivot_col_coef = CjZj[i];
                        pivot_col = i;
                    }
                }
            }
            if (!best)
            {
                double pivot_row_coef = -1;
                int pivot_row = -1;
                for (int i = 0; i < n; i++)
                {
                    if (B[i] / A[i][pivot_col] >= 0 && (B[i] / A[i][pivot_col] < pivot_row_coef || pivot_row == -1))
                    {
                        pivot_row = i;
                        pivot_row_coef = B[i] / A[i][pivot_col];
                    }
                }
                if (pivot_row == -1)
                {
                    throw invalid_argument("not applicable");
                }
                basis[pivot_row] = pivot_col;
                for (int i = 0; i < m; i++)
                {
                    if (i != pivot_col)
                    {
                        A[pivot_row][i] /= A[pivot_row][pivot_col];
                    }
                }
                B[pivot_row] /= A[pivot_row][pivot_col];
                A[pivot_row][pivot_col] = 1;
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < m; j++)
                    {
                        if (i != pivot_row && j != pivot_col)
                        {
                            A[i][j] -= A[i][pivot_col] * A[pivot_row][j];
                        }
                    }
                    if (i != pivot_row)
                    {
                        B[i] -= A[i][pivot_col] * B[pivot_row];
                        A[i][pivot_col] = 0;
                    }
                }
            }
        }

        double res = 0;
        for (int i = 0; i < n; i++)
        {
            res += C[basis[i]] * B[i];
        }
        cout << fixed << setprecision(approx) << res;
    }
    catch (...)
    {
        cout << "Not applicable" << endl;
    }
}

int main()
{
    cout << "Number of constraingts" << endl;
    int n;
    cin >> n;
    vector<double> con(n);
    for (int i = 0; i < n; i++)
    {
        cin >> con[i];
    }

    cout << "Number of equations" << endl;
    int m;
    cin >> m;
    vector<vector<double>> a(m, vector<double>(n));
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }

    cout << "right hand side" << endl;
    vector<double> b(m);
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
    }

    int approx;
    cin >> approx;

    bool mn = false;
    string s;
    cin >> s;
    if (s == "min")
    {
        mn = true;
    }
    else
    {
        mn = false;
    }

    solve(con, a, b, approx, mn);
}