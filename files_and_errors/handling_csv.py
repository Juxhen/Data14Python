import csv
#scores = []
# with open("some_data.csv") as csvfile:
#     csvreader = csv.reader(csvfile)
#     print(list(csvreader)) # a list of lists
#     #headers = next(csvreader)
#     #headers = list(map(str.lstrip, next(csvreader))) # using map
#     # for row in csvreader:
#     #     # scores.append(row[-1]) # displays with the header 'score'
#     #     # print(row[-1]) # returns only the scores
#     #     scores.append(int(row[-1]))
# #print(headers)
# #print(scores)
#
# data_to_write = [["David", 5], ["Paula", 6], ["Nish", 7]]
#
# with open("some_data.csv", "w") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     # for row in data_to_write:
#     #     csv_writer.writerow(row) # option 1
#     csv_writer.writerows(data_to_write) # option 2 (preferable one for meee)

#Write a function that will read in the iris dataset
#write a function that will return the mean for each 'column'

display_list = []

def read_data(dataset):
    try:
        with open("iris.csv", "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            # csv_reader = list(csv.reader(csvfile))
            # csv_reader = csv_reader[1:]
            #csv_reader = list(csv.reader(csvfile))
            #next(csv_reader)
            headers = list(map(str.lstrip, next(csv_reader)))
            print(headers)
            return list(csv_reader)
    except FileNotFoundError:
        print("file not found")


def find_mean(dataset, reader):
    with open("iris.csv", "r") as csvfile:
        csv_reader = list(csv.reader(csvfile))
        csv_reader = csv_reader[1:]
        for i in range(4):
            sum = 0
            for row in csv_reader:
                print(i, row)
                sum += float(row[i])
            mean = sum / len(list(csv_reader))
            display_list.append(mean)
        return display_list

the_means = find_mean("iris.csv", read_data("iris.csv"))
# print(the_means)
the_means_with_headers = ['sepal_length', find_mean[0]],['sepal_width', find_mean[1]],['petal_length', find_mean[2]],['petal_width', find_mean[3]]

with open("means.csv", "w") as opened_csv:
    opened_csv.writelines(the_means_with_headers)
