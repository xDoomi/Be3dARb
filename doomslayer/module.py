from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, spisok):
        self.spisok = [line.copy() for line in spisok]

    def __str__(self):
        res = ['\t'.join([str(j) for j in i]) for i in self.spisok]
        return '\n'.join(res)

    def __add__(self, other):
        if (len(self.spisok) == len(other.spisok) and
                len(self.spisok[0]) == len(other.spisok[0])):
            res = []
            for i in range(len(self.spisok)):
                res.append(list(map(lambda x, y: x + y, self.spisok[i],
                                other.spisok[i])))
            return Matrix(res)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            res = []
            for i in range(len(self.spisok)):
                res.append(list(map(lambda x: x * other, self.spisok[i])))
        elif (isinstance(other, Matrix) and
                len(self.spisok[0]) == len(other.spisok)):
            res = [[0] * len(other.spisok[0]) for i in range(len(self.spisok))]
            for i in range(len(self.spisok)):
                for j in range(len(other.spisok[0])):
                    for k in range(len(self.spisok[0])):
                        res[i][j] += self.spisok[i][k] * other.spisok[k][j]
        else:
            raise MatrixError(self, other)
        return Matrix(res)

    __rmul__ = __mul__

    def size(self):
        return (len(self.spisok), len(self.spisok[0]))

    def transpose(self):
        res = [[0] * len(self.spisok) for i in range(len(self.spisok[0]))]
        for i in range(len(self.spisok)):
            for j in range(len(self.spisok[0])):
                res[j][i] = self.spisok[i][j]
        self.spisok = res
        return Matrix(res)

    @staticmethod
    def transposed(other):
        res = [[0] * len(other.spisok) for i in range(len(other.spisok[0]))]
        for i in range(len(other.spisok)):
            for j in range(len(other.spisok[0])):
                res[j][i] = other.spisok[i][j]
        return Matrix(res)
exec(stdin.read())
