def read(file):
    with open(file, "r") as f:
        """Read matrices from a line"""

        # Read the first two lines
        rows = f.readline().strip()
        columns = f.readline().strip()
        
        # Instantiate a list, and save the rest of the line in the file into a list
        lines = []
        for line in f:
            lines.append().strip()

        return lines, rows, columns
        
    #     i = 0
    #     matrices = []
    #     for line in f:
    #         i += 1
    #         if i > 2:
    #             matrices.append(line)
    # return matrices    




def add(*matrix):
    """Addition of sparse matrices, matrices passed as args"""
    result = {}

    for i, j, value in matrix:
        result[i, j] = result.get((i,j), 0) + value

    # Format the results
    result = [(i, j, v) for (i, j), v in result.items() if v != 0]

    return result

def subtract(*matrix):
    """Subtraction of matrices, matrices passed as args"""
    result = {}
    # Set first matrice into the result
    first = matrix[0]
    result = {first[:2]:first[2]}
    # Subtract the rest by going through the rest 
    for i, j, value in matrix[1:]:
        result[i, j] = result.get((i,j), 0) - value


    # Format the results
    result = [(i, j, v) for (i, j), v in result.items() if v != 0]
    return result


def multiplication(*matrix):
    pass

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


print(read("dsa/sparse_matrix/sample_inputs/ easy_sample_01_2.txt"))
# print(add((0, 23, 632), (0, 32, 5456)))