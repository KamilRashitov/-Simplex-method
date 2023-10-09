print("Enter the coefficients of the main problem on one line with space delimiter")
coeff_main = list(map(int, input().split()))
print("Enter number of constraints")
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input("Enter coefficients of " + str(i + 1) + "th constraint with space delimiter")
                           .split(' '))))
print("Enter the right-hand coefficients of the constraints on one line with space delimiter")
coeff_constr = list(map(int, input().split()))
print("Enter 1 if your problem is maximize and -1 if your problem is minimize")
k = int(input())
for i in range(len(coeff_main)):
    coeff_main = coeff_main * k
for i in range(len(coeff_main)):
    coeff_main = coeff_main * -1
print("Enter the approximation accuracy")
approximation_accuracy = int(input())
matrix.insert(0, coeff_main)
for i in range(1, len(matrix)):
    matrix[i].append(coeff_constr[i - 1])
    








