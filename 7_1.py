class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(["\t".join([str(w) for w in row]) for row in self.matrix])

    def __add__(self, other):
        j = 0
        out_list = []
        while j < len(self.matrix):
            n = self.matrix[j]
            k = other.matrix[j]
            i = 0
            in_list = []
            while i < len(self.matrix[j]):
                p = k[i] + n[i]
                in_list.append(p)
                i += 1
            out_list.append(in_list)
            j += 1
        return out_list


m_1 = Matrix([[1, 3333, 2], [8, 2, 5], [1, 2, 66]])
m_2 = Matrix([[6, 7, 8], [13, 24, 22], [9, 8, 7]])
print(m_1)
print(m_2)
print(m_1 + m_2)
