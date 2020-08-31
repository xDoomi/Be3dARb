from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Exception(BaseException):
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

    def solve(self, otv):
        res = [0] * len(otv)
        ind = 0
        while(ind < len(self.spisok)):
            if ind == len(self.spisok) - 1:
                num = self.spisok[ind][ind]
                if num == 0:
                    raise Exception(self, otv)
                self.spisok[ind][ind] = self.spisok[ind][ind] / num
                otv[ind] = otv[ind] / num
                ind += 1
                continue
            max = self.spisok[ind][ind]
            index = ind
            for i in range(len(self.spisok)):
                if self.spisok[i][ind] > max:
                    max = self.spisok[i][ind]
                    index = i
            if index != ind:
                for i in range(len(self.spisok[index])):
                    m = self.spisok[index][i]
                    self.spisok[index][i] = self.spisok[ind][i]
                    self.spisok[ind][i] = m
                n = otv[index]
                otv[index] = otv[ind]
                otv[ind] = n
            for i in range(ind, len(self.spisok)):
                num = self.spisok[i][ind]
                if num == 0:
                    continue
                for j in range(ind, len(self.spisok[i])):
                    self.spisok[i][j] = self.spisok[i][j] / num
                otv[i] = otv[i] / num
            for i in range(ind + 1, len(self.spisok)):
                if self.spisok[i][ind] == 0:
                    continue
                for j in range(ind, len(self.spisok[i])):
                    self.spisok[i][j] -= self.spisok[ind][j]
                otv[i] -= otv[ind]
            ind += 1
        index = len(otv) - 2
        res[len(otv) - 1] = otv[len(otv) - 1]
        for i in range(len(otv) - 2, -1, -1):
            for j in range(len(otv) - 1, index, -1):
                res[i] -= self.spisok[i][j] * res[j]
            res[i] += otv[i]
            index -= 1
        return res

    @staticmethod
    def transposed(other):
        res = [[0] * len(other.spisok) for i in range(len(other.spisok[0]))]
        for i in range(len(other.spisok)):
            for j in range(len(other.spisok[0])):
                res[j][i] = other.spisok[i][j]
        return Matrix(res)

exec(stdin.read())
