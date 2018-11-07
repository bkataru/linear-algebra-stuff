'''
A = [[9, 2, 4], [3, 5, 6]]
B = [[2, 4, 1], [2, 5, 7]]

C = [[1, 7], [2, 4]]
D = [[3, 3], [5, 2]]


C = [[4, 7, 1], [8, 3, 8]]
D = [[4, 2], [5, 9], [6, 3]]
'''

A = [[7, 3], [2, 5], [6, 8], [9, 0]]
B = [[7, 4, 9], [8, 1, 5]]
C = [[1, 7], [2, 4]]
D = [[7, 4, 9], [8, 1, 5], [8, 3, 8]]

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

def findNext(item, ind, iter):
    try:
        elem = item[ind + iter]
        return ind + iter
    except IndexError:
        return (ind + iter) - len(item)


def determinant(A):
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
        for k in range(len(A)):
            diagonal *= A[k][findNext(A, k, j)]
        backwardDiagonals.append(diagonal)

    return sum(forwardDiagonals) - sum(backwardDiagonals)


def prettyPrint(X):
    for elem in X:
        for k in elem:
            print(k, end='\t')
        print()

print(determinant(D))

# prettyPrint(multiply(A, B))







