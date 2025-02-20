def read(file):
    with open(file, "r") as f:
        """Read matrices from a line"""

        # Read the first two lines
        rows = f.readline().strip()
        columns = f.readline().strip()

        rows = int(rows.split('=')[1])
        columns = int(columns.split('=')[1])
        
        # Instantiate a list, and save the rest of the line in the file into a list
        lines = []
        for line in f:
            line = line.strip()
            line = line.strip("()").split(",")

            lines.append(tuple(map(int, line)))

    

        return lines, rows, columns
        
    #     i = 0
    #     matrices = []
    #     for line in f:
    #         i += 1
    #         if i > 2:
    #             matrices.append(line)
    # return matrices    




def add(*matrices):
    """Addition of sparse matrices, matrices passed as args"""
    result = {}

    for matrix in matrices:
        for i, j, value in matrix:
            result[(i, j)] = result.get((i,j), 0) + value

    # Format the results
    result = [(i, j, v) for (i, j), v in result.items() if v != 0]

    return result

def subtract(*matrices):
    """Subtraction of matrices, matrices passed as args"""
    result = {}
    # Set first matrice into the result
    result = { (i, j): v for i, j, v in matrices[0] }
    # Subtract the rest by going through the rest 
    for matrix in matrices[1:]:
        for i, j, value in matrix:
            result[i, j] = result.get((i,j), 0) - value


    # Format the results
    result = [(i, j, v) for (i, j), v in result.items() if v != 0]
    return result


def multiplication(A, B, colsA, rowsB):
    """
    Multiplies two sparse matrices A and B
    """
    try:
        if not A or not B:
            return []

        # Convert A and B into dictionaries for faster lookup
        A_dict = {}
        B_dict = {}

        # Fill A_dict
        for i, j, value in A:
            if i not in A_dict:
                A_dict[i] = {}
            A_dict[i][j] = value

        # Fill B_dict
        for i, j, value in B:
            if i not in B_dict:
                B_dict[i] = {}
            B_dict[i][j] = value

        # Result dictionary
        result = {}

        # Perform multiplication
        for rA in A_dict:  # Iterate over rows of A
            for cA in A_dict[rA]:  # Iterate over columns of A
                if cA in B_dict:  # A's column must be a row in B
                    for cB in B_dict[cA]:  # Iterate over columns of B
                        key = (rA, cB)
                        if key not in result:
                            result[key] = 0  # Initialize if not present
                        result[key] += A_dict[rA][cA] * B_dict[cA][cB]

        # Format the results
        result = [(i, j, v) for (i, j), v in result.items() if v != 0]
        return result

    except Exception as e:
        print(e)

def getElement(file, currRow, currCol):
    """Reads the lines in a file and gets the non zero element in the row and column"""
    with open(file, "r") as f:
        lines = []
        for line in f:
            lines.append().strip()    
        
        for line in lines:
            if currRow and currCol:
                return line
            else:
                return 0

def setElement(file, currRow, currCol, value):
    with open(file, "r") as f:
        lines = []
        for line in f:
            lines.append().strip()


        for line in lines:
            if currRow and currCol in line:
                line.append(({currRow}, {currCol}, {value}))
            else:
                line[2] = value
        
        with open(file, "w") as f:
            for line in lines:
                f.write(line + "\n")


# print(read("dsa/sparse_matrix/sample_inputs/ easy_sample_01_2.txt"))
# print(multiplication([(0, 23, 632), (0, 32, 5456)], [(0, 23, 632), (0, 32, 5456)]))

matrix1 = read("dsa/sparse_matrix/sample_inputs/easy_sample_01_2.txt")
matrix2 = read("dsa/sparse_matrix/sample_inputs/easy_sample_01_3.txt")

# add(matrix1[0], matrix2[0])

print(matrix1[1], matrix1[2], matrix2[1], matrix2[2])
# print(read("dsa/sparse_matrix/sample_inputs/ easy_sample_01_2.txt"))