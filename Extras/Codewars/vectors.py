import numpy


class Vector:
    def __init__(self, elements):
        self.elements = elements

    def equal_length(self, vector):
        if len(self.elements) != len(vector.elements):
            raise Exception('Vectors have different length')


    def add(self, vector):
        self.equal_length(vector)
        a = numpy.array(self.elements)
        b = numpy.array(vector.elements)
        return a + b

    def subtraction(self, vector):
        self.equal_length(vector)
        a = numpy.array(self.elements)
        b = numpy.array(vector.elements)
        return a - b

    def dot(self, vector):
        self.equal_length(vector)
        a = numpy.array(self.elements)
        b = numpy.array(vector.elements)
        c = a * b
        return sum(c)

    def norm(self):
        c = []
        for x in self.elements:
            c.append(x**2)
            print(c)
        return (sum(c))**2


a = Vector([1, 2])
b = Vector([3, 4])
c = Vector([1, 2, 3])

print(a.add(b))
