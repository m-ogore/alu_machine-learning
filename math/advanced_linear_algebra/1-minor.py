
determinant = __import__('0-determinant').determinant

def minor(matrix):
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a list of lists')
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a list of lists')
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError('matrix must be a non-empty square matrix')
    if len(matrix) == 0:
        return []
    '''
        Let's start with the definition of (i,j)th minor matrix of a matrix:

        (i,j)th minor of a matrix of size n is a smaller matrix of size n-1 with the i'th row and j'th column deleted.

        Now lets look at this python one liner:

        [row for row in (m[:i] + m[i+1:])]
        m[:i] gives the first i rows of m (remember that we are representing a matrix as a list of rows, and adding two lists gives back a bigger list in python), now let's look at another one liner:

        row[:j] + row[j+1:]
        This gives us all the elements of a row except the j'th element (lst[a:b] gives a list with elements from lst between a and b, with b excluded)

        Combine the above two and you get an expression which returns a new matrix with i'th row and j'th column excluded:

        def getMatrixMinor(m,i,j):
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
        Which is the minor matrix.

        minor = []
    '''
   


    
    minors = []
    for i in range(len(matrix)):
        minor_row = []
        for j in range(len(matrix[0])):
             """
                Compute the (i,j)th minor matrix of the input matrix by excluding the i'th row and j'th column.
            """
             minor_sub_matrix =  [row[:j] + row[j+1:] for row_idx, row in enumerate(matrix) if row_idx != i]
             
             """
                Compute the matrix of minors of the input matrix.
            """
             minor_row.append(determinant(minor_sub_matrix))
        minors.append(minor_row)
    return minors
