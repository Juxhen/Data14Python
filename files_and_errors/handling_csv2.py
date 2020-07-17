import csv


class Iris:

    def __init__(self, filename):
        raw_data = self.load_data(filename)
        self.header = raw_data[0]
        self.data = raw_data[1:]

    def load_data(self, filename):
        with open(filename) as open_file:
            csv_reader = csv.reader(open_file)
            return list(csv_reader)

    def find_mean(self, list_of_values):
        return mean


iris = Iris("iris.csv")

print(iris.header)
print(iris.data)

iris.find_mean(iris.sepal_lengths) # for example
# expect it to return a dictionairy {"sepal_length":5.28, "sepal_width":2.89....}