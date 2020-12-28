def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    arr1 = [[1,2,3,4],[5,1,2,3],[6,5,1,2]]
    arr2 = [[1,2,3,4],[5,1,9,3],[6,5,1,2]]

    R = len(matrix)
    C = len(matrix[0])
    #for each element in the first row of the array
    for col in range(0,C):
        start = matrix[0][c]
        for k in range(0,min(R, C-col)):
            print(matrix[k][col+k])
            if matrix[k][col+k] != start:
                return False
    for row in range(0,R):
        start = matrix[R][0]
        for k in range(0,min(R-row, C)):
            print(matrix[row+k][k])
            if matrix[row+k][k] != start:
                return False
    return True