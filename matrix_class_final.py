class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])

    def multiply(self, x):
        # x = instance of 2nd matrix - list of lists
        if self.cols != x.rows:
            print('unable to multiply')
        elif isinstance(x, Matrix):
            # creating empty result matrix
            C = [[0 for i in range(x.cols)] for j in range(self.rows)]
            # algorithm for calculating matrix * matrix
            for i in range(self.rows):
                for j in range(x.cols):
                    for k in range(x.rows):
                        C[i][j] += self.matrix[i][k] * x.matrix[k][j]
            return C
        else:
            return 'something is wrong'

    def add(self, x):
        if isinstance(x, Matrix):
            # creating empty result matrix
            C = [[0 for i in range(x.cols)] for j in range(self.rows)]
            # algorithm for calculating matrix + matrix
            for i in range(self.rows):
                for j in range(x.cols):
                    C[i][j] += self.matrix[i][j] + x.matrix[i][j]
            return C
        else:
            return 'something is wrong'
