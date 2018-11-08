/*
* linearAlgebra: Linear Algebra operations implemented in vanilla JavaScript.
* Operations possible so far: [
*       add -- add two matrices,
*       subtract -- subtract two matrices,
*       scalar multiply -- multiply a matrix by a scalar,
*       multiply -- multiply two matrices together (if their product is defined),
*       determinant -- find the determinant of an NxN square matrix,
*       pretty print -- print matrices like matrices and not like ugly 2D arrayx :)
*  ]
* Required packages: None.
* Follows the Common.js module pattern so this module can be imported into any Node.js program.
* Methods:
*   1. linearAlgebra.add([matrixA], [matrixB]) -- adding matrices
*   2. linearAlgebra.subtract([matrixA], [matrixB]) -- subtracting two matrices
*   3. linearAlgebra.scalarMultiply([matrixA], scalar) -- multiplying a matrix by a scalar
*   4. linearAlgebra.multiply([matrixA], [matrixB]) -- multiplying two matrices (if their product is defined, else returns -1)
*   5. linearAlgebra.determinant([matrixA]) -- find the determinant of an NxN matrix (if the matrix is a square matrix, else returns -1)
*   6. linearAlgebra.prettyPrint([matrixA]) -- pretty print a matrix.
* */

// Sample matrices below (for testing purposes)
// 4x2
A = [[7, 3], [2, 5], [6, 8], [9, 0]];
// 2x3
B = [[7, 4, 9], [8, 1, 5]];
P = [[9, 2, 4], [3, 5, 6]];
Q = [[2, 4, 1], [2, 5, 7]];
T = [[4, 7, 1], [8, 3, 8]];
// 2x2
C = [[1, 7], [2, 4]];
R = [[1, 7], [2, 4]];
S = [[3, 3], [5, 2]];
// 3x2
U = [[4, 2], [5, 9], [6, 3]];
// 3x3
D = [[7, 4, 9], [8, 1, 5], [8, 3, 8]];
// 4x4
E = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]];
// 5x5
F = [[1, 2, 4, 3, 0], [2, 1, -1, 1, 3], [4, -1, -2, 5, 1], [7, 3, 6, 2, 1], [1, 0, -1, 1, 1]];
// 6x6
G = [[0, 21, 60, 40, 5, 82], [21, 0, 52, 70, 12, 98], [60, 52, 0, 18, 89, 95], [40, 70, 18, 0, 70, 81], [5, 12, 89, 70, 0, 88], [82, 98, 95, 81, 88, 0]];
// 7x7
H = [[-8, -13, 15, -16, 6, 9, -3], [4, 7, -6, 7, -2, -4, 1], [-50, -60, 74, -77, 29, 43, -13], [-82, -98, 118, -125, 47, 71, -21], [2, 1, -2, 2, 1, -1, 0], [-56, -88, 80, -86, 32, 50, -14], [48, 59, -70, 75, -28, -42, 15]];


var linearAlgebra = (function () {
    function add(A, B) {
        X = [];
        for(let i = 0; i < A.length; i++)
        {
            let newRow = [];
            for(let j = 0; j < A[0].length; j++)
            {
                newRow.push(A[i][j] +  B[i][j]);
            }
            X.push(newRow);
        }
        return X;
    }

    function subtract(A, B) {
        X = [];
        for(let i = 0; i < A.length; i++)
        {
            let newRow = [];
            for(let j = 0; j < A[0].length; j++)
            {
                newRow.push(A[i][j] -  B[i][j]);
            }
            X.push(newRow);
        }
        return X;
    }

    function scalarMultiply(A, s) {
        X = [];
        for(let i = 0; i < A.length; i++)
        {
            let newRow = [];
            for(let j = 0; j < A[0].length; j++)
            {
                newRow.push(A[i][j] * s);
            }
            X.push(newRow);
        }

        return X;
    }

    function dotProduct(A, B) {
        let product = 0;
        for(let i = 0; i < A.length; i++)
        {
            product += (A[i] * B[i])
        }

        return product;
    }

    function multiply(A, B) {
        if(A[0].length === B.length)
        {
            let columnsArr = [];
            for(let i = 0; i < B[0].length; i++)
            {
                let columnVector = [];
                for(let elem of B) {
                    columnVector.push(elem[i]);
                }
                columnsArr.push(columnVector);
            }

            let productArr = [];
            for(let j = 0; j < A.length; j++)
            {
                let productRows = [];
                for(let k = 0; k < columnsArr.length; k++)
                {
                    productRows.push(dotProduct(A[j], columnsArr[k]));
                }
                productArr.push(productRows);
            }

            return productArr;
        }
        else
        {
            return -1;
        }
    }

    function findNext(item, ind, iter) {
        let index = item[ind + iter];
        return !index ? (ind + iter) - item.length : ind + iter;
    }

    function lowerDeterminant(A) {
        let diagonals = A.length === 2 ? 1 : A.length;

        let forwardDiagonals = [];
        for(let i = 0; i < diagonals; i++)
        {
            let diagonal = 1;
            for(let j = 0; j < A.length; j++)
            {
                diagonal *= A[j][findNext(A, j, i)];
            }
            forwardDiagonals.push(diagonal);
        }

        let newArr = [];
        for(let i = 0; i < A.length; i++)
        {
            let row = [];
            for(let j = A[0].length - 1; j >= 0; j--)
            {
                row.push(A[i][j]);
            }
            newArr.push(row);
        }
        A = newArr;

        let backwardDiagonals = [];
        for(let i = 0; i < diagonals; i++)
        {
            let diagonal = 1;
            for(let j = 0; j < A.length; j++)
            {
                diagonal *= A[j][findNext(A, j, i)];
            }
            backwardDiagonals.push(diagonal);
        }

        return forwardDiagonals.reduce((a, b) => a + b, 0) - backwardDiagonals.reduce((a, b) => a + b, 0);
    }

    function higherDeterminant(X) {
        let l = X.length;

        let calcArr = [];
        for(let i = 0; i < l; i++)
        {
            let rows = [];
            for(let j = 0; j < l; j++)
            {
                let row = [];
                for(let k = 0; k < l; k++)
                {
                    if(j === 0)
                        break;
                    if(k === i)
                        continue;
                    row.push(X[j][k]);
                }

                if(row.length > 0)
                    rows.push(row);


            }
            let func = rows.length > 3 ? higherDeterminant : lowerDeterminant;
            calcArr.push(X[0][i] * func(rows));
        }

        let determinantVal = 0;
        for(let i = 0; i < calcArr.length; i++)
        {
            if(i % 2 !== 0)
            {
                determinantVal -= calcArr[i];
            }
            else
            {
                determinantVal += calcArr[i];
            }
        }

        return determinantVal;
    }

    function determinant(A) {
        if(A.length !== A[0].length)
            return -1;

        return higherDeterminant(A);
    }

    function prettyPrint(X) {
        for(let elem of X)
        {
            for(let k of elem)
            {
                process.stdout.write(k + '\t');
            }
            process.stdout.write('\n');
        }
    }

    return {
        add: add,
        subtract: subtract,
        scalarMultiply: scalarMultiply,
        multiply: multiply,
        findNext: findNext,
        determinant: determinant,
        prettyPrint: prettyPrint
    }
})();

// how to use:
// console.log(linearAlgebra.determinant(H));
// linearAlgebra.prettyPrint(multiply(B, U));
// linearAlgebra.prettyPrint(H);

module.exports = linearAlgebra;



