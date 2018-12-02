# Linear Algebra operations implemented in vanilla Python (uses only the math module).
# Operations possible so far: [
#       add -- add two matrices or vectors,
#       subtract -- subtract two matrices or vectors,
#       scalar multiply -- multiply a matrix/vector by a scalar,
#       multiply -- multiply two matrices together (if their product is defined),
#       transpose -- transpose (spatially invert by rows and cols) a matrix of any dimensions,
#       determinant -- find the determinant of an NxN square matrix (general function),
#       inverse -- find the inverse of an NxN square matrix (the inverse of a matrix when multiplied with the original matrix produced the identity matrix of the corresponding order),
#       magnitude -- find the magnitude/length of a column vector
#       dotProduct -- find the dot product of two column vectors,
#       crossProduct - find the cross product of two 3 dimensional column vectors. Only valid for 3 dimensional vectors and returns a vector orthogonal to the first two.
#       angle - find the angle between two vectors (uses the definition of the dot product)
#       pretty print -- print matrices like matrices and not like ugly 2D arrayx :)
#  ]
# Required packages: None.
# Methods:
#       1. add([matrixA/vectorA], [matrixB/vectorB]) -- adding matrices/vectors
#       2. subtract([matrixA/vectorA], [matrixB/vectorB]) -- subtracting two matrices/vectors
#       3. scalarMultiply([matrixA/vectorA], scalar) -- multiplying a matrix/vector by a scalar
#       4. magnitude([vectorA]) -- magnitude/length of a vector
#       5. dotProduct([matrixA/vectorA], [matrixB/vectorB]) -- dot product of two column vectors (used in matrix multiplication)
#       6. crossProduct([vectorA], [vectorB]) -- cross product of two column vectors
#       7. angle([vectorA], [vectorB]) -- angle between two vectors (returns a list of angle in radians and degrees)
#       8. multiply([matrixA], [matrixB]) -- multiplying two matrices (if their product is defined, else returns -1)
#       9. transpose([matrixA]) -- transpose (spatially invert by rows and cols) a matrix of any dimensions
#       10. determinant([matrixA]) -- find the determinant of an NxN matrix (general function for NxN, works only if the matrix is a square matrix or else returns -1)
#       11. higherDeterminant([matrixA]) -- find the determinant of matrices using the Laplace expansion/minor matrices method (works only for 3x3 matrices and above, partially recursive and computationally heavier than the diagonal method)
#       12. lowerDeterminant([matrixA]) -- find the determinant of matrices using diagonal method (can only be used for 2x2 and 3x3, computationally faster for 3x3 as compared to the minor method)
#       13. inverse([matrixA]) -- find the inverse of a matrix (if the matrix is a square matrix and its inverse is defined, else returns -1)
#       14. prettyPrint([matrixX]) -- pretty print a matrix.
#       15. findNext(item, index, iteration) -- random function, used to create a cycling indexing function where out of bounds indices are made valid indices (used in diagonal method for determinant calculation)

# Sample matrices below (for testing purposes)
#
V = [[8], [2], [6]]
W = [[5], [7], [10]]
# 4x2
A = [[7, 3], [2, 5], [6, 8], [9, 0]]
# 2x3
B = [[7, 4, 9], [8, 1, 5]]
P = [[9, 2, 4], [3, 5, 6]]
Q = [[2, 4, 1], [2, 5, 7]]
T = [[4, 7, 1], [8, 3, 8]]
# 2x2
C = [[1, 7], [2, 4]]
R = [[1, 7], [2, 4]]
S = [[3, 3], [5, 2]]
# 3x2
U = [[4, 2], [5, 9], [6, 3]]
# 3x3
D = [[7, 4, 9], [8, 1, 5], [8, 3, 8]]
O = [[-1, -2, 2], [2, 1, 1], [3, 4, 5]]
# 4x4
E = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
# 5x5
F = [[1, 2, 4, 3, 0], [2, 1, -1, 1, 3], [4, -1, -2, 5, 1], [7, 3, 6, 2, 1], [1, 0, -1, 1, 1]]
# 6x6
G = [[0, 21, 60, 40, 5, 82], [21, 0, 52, 70, 12, 98], [60, 52, 0, 18, 89, 95], [40, 70, 18, 0, 70, 81], [5, 12, 89, 70, 0, 88], [82, 98, 95, 81, 88, 0]]
# 7x7
H = [[-8, -13, 15, -16, 6, 9, -3], [4, 7, -6, 7, -2, -4, 1], [-50, -60, 74, -77, 29, 43, -13], [-82, -98, 118, -125, 47, 71, -21], [2, 1, -2, 2, 1, -1, 0], [-56, -88, 80, -86, 32, 50, -14], [48, 59, -70, 75, -28, -42, 15]]

# Vector and Matrix addition
def add(A, B):
    X = []  # A + B
    for i in range(len(A)):
        new_row = []
        for k in range(len(A[i])):
            new_row.append(A[i][k] + B[i][k])
        X.append(new_row)
    return X

# Vector and Matrix subtraction
def subtract(A, B):
    X = [] # A - B
    for i in range(len(A)):
        new_row = []
        for k in range(len(A[i])):
            new_row.append(A[i][k] - B[i][k])
        X.append(new_row)
    return X

# Magnitude/Length of a vector
def magnitude(a):
    mag = 0
    flag = 0
    if type(a[0]) == list:
        flag = 1
    for elem in a:
        if flag == 1:
            mag += elem[0]**2
        else:
            mag += elem**2

    return mag**(0.5)

# Scalar multiplication of a Matrix and Vector
def scalarMultiply(A, s):
    X = [] # A * s
    for row in A:
        new_row = []
        for elem in row:
            new_row.append(elem * s)
        X.append(new_row)
    return X

# Dot product of column vectors
def dotProduct(a, b):
    dotP = 0
    flag = 0
    if type(a[0]) == list:
        flag = 1
    for i in range(len(a)):
        if flag == 1:
            e1, e2 = a[i][0], b[i][0]
        else:
            e1, e2 = a[i], b[i]
        dotP += (e1*e2)
    return dotP

# Cross product of two 3 dimensional column vectors
def crossProduct(a, b):
    l = len(a)
    if l != 3:
        return -1

    flag = 0
    if type(a[0]) == list:
        flag = 1

    product = []
    for i in range(l):
        x = findNext(b, i, 1)
        y = findNext(b, i, 2)
        if flag == 1:
            calc = [a[x][0] * b[y][0] - a[y][0] * b[x][0]]
        else:
            calc = [a[x] * b[y] - a[y] * b[x]]
        product.append(calc)

    return product

# Angle between two vectors
def angle(a, b):
    dot = dotProduct(a, b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    import math

    rad_angle = math.acos(dot/(mag_a * mag_b))
    degree_angle = math.degrees(rad_angle)

    return [rad_angle, degree_angle]

# Matrix multiplication
def multiply(A, B):
    if len(A[0]) == len(B):
        columnsArr = []
        for i in range(len(B[0])):
            columnVector = []
            for elem in B:
                columnVector.append(elem[i])
            columnsArr.append(columnVector)
        productArr = []
        for i in range(len(A)):
            productRows = []
            for k in range(len(columnsArr)):
                productRows.append(dotProduct(A[i], columnsArr[k]))
            productArr.append(productRows)
        return productArr
    else:
        return -1

def switchRows(A, R1, R2):
    temp = A[R1]
    A[R1] = A[R2]
    A[R2] = temp

    return A

def rowOperations(A, option, **kwargs):
    # 1 - switch rows, 2 - add rows and replace row, 3 - subtract rows and replace row, 4 - multiply rows with a scalar
    try:
        if option == 1:
            R1 = int(kwargs['R1']) - 1
            R2 = int(kwargs['R2']) - 1
            temp = A[R1]
            A[R1] = A[R2]
            A[R2] = temp

            return A
        elif option == 2:
            R1 = int(kwargs['R1']) - 1
            R2 = int(kwargs['R2']) - 1
            destR = int(kwargs['Rd']) - 1

            newRow = []
            for i in range(len(A[R1])):
                newRow.append(A[R1][i] + A[R2][i])
            A[destR] = newRow

            return A
        elif option == 3:
            R1 = int(kwargs['R1']) - 1
            R2 = int(kwargs['R2']) - 1
            destR = int(kwargs['Rd']) - 1

            newRow = []
            for i in range(len(A[R1])):
                newRow.append(A[R1][i] - A[R2][i])
            A[destR] = newRow

            return A
        elif option == 4:
            R = int(kwargs['R']) - 1
            s = kwargs['s']
            newRow = []
            for elem in A[R]:
                newRow.append(elem * s)
            A[R] = newRow

            return A
    except ValueError:
        return -1

# Cycling indexing function
def findNext(item, ind, iter):
    try:
        elem = item[ind + iter]
        return ind + iter
    except IndexError:
        return (ind + iter) - len(item)

# Only valid for 2x2 and 3x3
def lowerDeterminant(A):
    if len(A) == 2:
        diagonals = 1
    else:
        diagonals = len(A)

    forwardDiagonals = []
    for i in range(diagonals):
        diagonal = 1
        for k in range(len(A)):
            diagonal *= A[k][findNext(A, k, i)]
        forwardDiagonals.append(diagonal)

    invertedA = []
    for elem in A:
        invertedA.append(elem[::-1])

    backwardDiagonals = []
    for j in range(diagonals):
        diagonal = 1
        for l in range(len(invertedA)):
            diagonal *= invertedA[l][findNext(A, l, j)]
        backwardDiagonals.append(diagonal)

    return sum(forwardDiagonals) - sum(backwardDiagonals)

# Valid for 3x3 and above
def higherDeterminant(A):
    l = len(A)

    calcArr = []
    for i in range(l):
        rows = []
        for j in range(l):
            row = []
            for k in range(l):
                if j == 0:
                    break
                if k == i:
                    continue
                row.append(A[j][k])
            if row:
                rows.append(row)

        if len(rows) > 3:
            func = higherDeterminant
        else:
            func = lowerDeterminant
        calcArr.append(A[0][i] * func(rows))

    determinant = 0
    for i in range(len(calcArr)):
        if i % 2 != 0:
            determinant -= calcArr[i]
        else:
            determinant += calcArr[i]

    return determinant

# General determinant function
def determinant(A):
    if len(A) != len(A[0]):
        return -1

    if len(A) == 2:
        return lowerDeterminant(A)
    else:
        return higherDeterminant(A)

# Valid for matrices of any dimensions
def transpose(A):
    transposed = []
    for i in range(len(A[0])):
        row = []
        for k in range(len(A)):
            row.append(A[k][i])
        transposed.append(row)

    return transposed

# Valid for any NxN square matrices
def inverse(A):
    if len(A) != len(A[0]):
        return -1

    det = determinant(A)
    if det == 0:
        return -1
    else:
        l = len(A)
        if l == 2:
            adjugate = transpose(A)

            adjugate = adjugate[::-1]
            for i in range(l):
                for k in range(l):
                    if k == i:
                        adjugate[i][k] = -adjugate[i][k]

            for temp in range(l):
                adjugate[temp] = adjugate[temp][::-1]

            return scalarMultiply(adjugate, 1/det)
        else:
            matrix_of_minors = []
            for u in range(l):
                calcArr = []
                for i in range(l):
                    rows = []
                    for j in range(l):
                        row = []
                        for k in range(l):
                            if j == u:
                                break
                            if k == i:
                                continue
                            row.append(A[j][k])
                        if row:
                            rows.append(row)

                    if len(rows) > 3:
                        func = higherDeterminant
                    else:
                        func = lowerDeterminant
                    calcArr.append(func(rows))
                matrix_of_minors.append(calcArr)

            for i in range(l):
                if i % 2 == 0:
                    start = +1
                else:
                    start = -1
                for j in range(l):
                    matrix_of_minors[i][j] = start * matrix_of_minors[i][j]
                    start *= -1

            return scalarMultiply(transpose(matrix_of_minors), 1/det)

def solveSimultaneousEquations():
    flag = 0
    unknowns = 1
    try:
        unknowns = int(input('Enter number of unknowns: '))
    except ValueError:
        flag = 1
        print("Invalid input, enter a number")

    if flag == 0:
        if unknowns == 1:
            print("Invalid number of unknowns, valid: 2 and more")
        else:
            coeffMatrix = []
            constantsVector = []
            iteration_interrupted = 0
            for i in range(unknowns):
                coeffs = input('Enter the coefficients and constant separated by commas for eq.{}: '.format(i + 1))
                coeffs = coeffs.split(',')
                invalidFlag = 0
                for k in range(len(coeffs)):
                    try:
                        coeffs[k] = int(coeffs[k].strip())
                    except ValueError:
                        invalidFlag = 1
                        break
                if invalidFlag == 1:
                    print("Invalid input, enter numbers")
                    iteration_interrupted = 1
                    break
                coeffMatrix.append(coeffs[:len(coeffs) - 1])
                constantsVector.append([coeffs[len(coeffs) - 1]])

            if iteration_interrupted == 0:
                solutions = multiply(inverse(coeffMatrix), constantsVector)

                print("The solutions are: ")
                for ind in range(len(solutions)):
                    print('unknown {}: {}'.format(ind + 1, solutions[ind][0]))


# Print matrices like matrices
def prettyPrint(A):
    if type(A) == list:
        for elem in A:
            for k in elem:
                print(k, end='\t')
            print()
    else:
        print("Not a list")


# how to use:
# print(determinant(D))
# prettyPrint(multiply(A, B))
# print(determinant(H))
# prettyPrint(G)
# prettyPrint(multiply(G, inverse(G)))
# solveSimultaneousEquations()

'''
prettyPrint(D)
print('*' * 50)
prettyPrint(rowOperations(D, 4, R=2, s=2))
'''

K = [2, 3]
Z = [5, 10]
print(angle(K, Z))






