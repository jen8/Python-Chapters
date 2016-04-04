def add_matrices(m1, m2):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[2, 2], [2, 2]]
    >>> add_matrices(a, b)
    [[3, 4], [5, 6]]
    >>> c = [[8, 2], [3, 4], [5, 7]]
    >>> d = [[3, 2], [9, 2], [10, 12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    >>> d
    [[3, 2], [9, 2], [10, 12]]
    """    
    output = []
    
    for index in range(len(m1)):
        row_1 = m1[index]
        row_2 = m2[index]
        new_row = []
        for index2 in range(len(row_1)):
            sum = row_1[index2] + row_2[index2]
            new_row.append(sum)
        output.append(new_row)
    return output


def row_times_column(m1, row, m2, column):
        """
          >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
          19
          >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
          22
          >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
          43
          >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
          50
        """

        sum = 0
        for index in range(len(m1)):
            product = m1[row][index] * m2[index][column]
            sum += product
        return sum
    
        
def matrix_mult(m1, m2):
    """
    >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    output = []
    for rowIndex, row in enumerate(m1):  #go through rows in m1
        new_row = []
        for columnIndex in range(len(m2[0])):  #go through indices for each column of m2
            sum = 0
            for index3 in range(len(row)):
                product = m1[rowIndex][index3] * m2[index3][columnIndex]
                sum += product
            new_row.append(sum)
        output.append(new_row)
    return output
    
    
    #output = []
    #first for loop corresponds to the rows of my output matrix and loops through the rows of m1 (enumerate)
    #create an empty new row
    # second for loop, loops through columns of m2
    # create sum variable, initialize it with zero
    # third for loop, multiplies the index of the row in m1 times the index of the column in m2
    # add sum to product and assign this to the sum variable
    # append sum to new row
    # append new row to output
    # return output
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()