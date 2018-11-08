# Linear Algebra operations implemented in vanilla Python.
# Operations possible so far: [
#       add -- add two matrices,
#       subtract -- subtract two matrices,
#       scalar multiply -- multiply a matrix by a scalar,
#       multiply -- multiply two matrices together (if their product is defined),
#       determinant -- find the determinant of an NxN square matrix (general function),
#       dotProduct -- find the dot product of two column vectors
#       pretty print -- print matrices like matrices and not like ugly 2D arrayx :)
#  ]
# Required packages: None.
# Methods:
#       1. add([matrixA], [matrixB]) -- adding matrices
#       2. subtract([matrixA], [matrixB]) -- subtracting two matrices
#       3. scalarMultiply([matrixA], scalar) -- multiplying a matrix by a scalar
#       4. multiply([matrixA], [matrixB]) -- multiplying two matrices (if their product is defined, else returns -1)
#       5. dotProduct([matrixA], [matrixB]) -- dot product of two column vectors (used in matrix multiplication)
#       5. determinant([matrixA]) -- find the determinant of an NxN matrix (general function for NxN, works only if the matrix is a square matrix or else returns -1)
#       6. higherDeterminant([matrixA]) -- find the determinant of matrices using submatrix/minor method (used for 4x4 matrices and above but can be used for lower order matrices as well, partially recursive and computationally heavier than the diagonal method for lower order matrices)
#       7. lowerDeterminant([matrixA]) -- find the determinant of matrices using diagonal method (can only be used for 2x2 and 3x3, computationally faster for 2x3 and 3x3 as compared to the minor method)
#       8. prettyPrint([matrixA]) -- pretty print a matrix.
#       9. findNext([matrixA], index, iteration) -- random function, used to create a cycling indexing function where out of bounds indices are made valid indices (used in diagonal method for determinant calculation)
#

# Sample matrices below (for testing purposes)
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
# 4x4
E = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
# 5x5
F = [[1, 2, 4, 3, 0], [2, 1, -1, 1, 3], [4, -1, -2, 5, 1], [7, 3, 6, 2, 1], [1, 0, -1, 1, 1]]
# 6x6
G = [[0, 21, 60, 40, 5, 82], [21, 0, 52, 70, 12, 98], [60, 52, 0, 18, 89, 95], [40, 70, 18, 0, 70, 81], [5, 12, 89, 70, 0, 88], [82, 98, 95, 81, 88, 0]]
# 7x7
H = [[-8, -13, 15, -16, 6, 9, -3], [4, 7, -6, 7, -2, -4, 1], [-50, -60, 74, -77, 29, 43, -13], [-82, -98, 118, -125, 47, 71, -21], [2, 1, -2, 2, 1, -1, 0], [-56, -88, 80, -86, 32, 50, -14], [48, 59, -70, 75, -28, -42, 15]]

# Matrix addition
def add(A, B):
    X = []  # A + B
    for i in range(len(A)):
        new_row = []
        for k in range(len(A[i])):
            new_row.append(A[i][k] + B[i][k])
        X.append(new_row)
    return X

# Matrix subtraction
def subtract(A, B):
    X = [] # A - B
    for i in range(len(A)):
        new_row = []
        for k in range(len(A[i])):
            new_row.append(A[i][k] - B[i][k])
        X.append(new_row)
    return X

# Scalar multiplication of a Matrix
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
    for i in range(len(a)):
        dotP += (a[i]*b[i])
    return dotP

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

    for ind in range(len(A)):
        A[ind] = A[ind][::-1]

    backwardDiagonals = []
    for j in range(diagonals):
        diagonal = 1
        for l in range(len(A)):
            diagonal *= A[l][findNext(A, l, j)]
        backwardDiagonals.append(diagonal)

    return sum(forwardDiagonals) - sum(backwardDiagonals)

# Valid for all NxN matrices
def higherDeterminant(X):
    l = len(X)

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
                row.append(X[j][k])
            if row:
                rows.append(row)

        if len(rows) > 3:
            func = higherDeterminant
        else:
            func = lowerDeterminant
        calcArr.append(X[0][i] * func(rows))

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

    return higherDeterminant(A)

# Print matrices like matrices
def prettyPrint(X):
    for elem in X:
        for k in elem:
            print(k, end='\t')
        print()


# how to use:
# print(determinant(D))
# prettyPrint(multiply(A, B))
# print(determinant(H))
# prettyPrint(G)







