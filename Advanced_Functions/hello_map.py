data14 = ["Katie", "Juxhen", "Joe"]

# data14_capitalised = list(str(data14).upper())"# returns as string not as list
# # data14_upper = map(str.upper, data14)
# # for name in data14_upper:
# #     print(name)
# #
# # map is a function to an iterable
# #
# print(data14_capitalised)
# print(type(data14_capitalised))
numbers = [1, 2, 3, 4, 5]
adds = [10, 100, 1000]


def square_and_add_three(num, add):
    return num * num + add

# num_map = map(square_and_add_three, numbers)
#
# print(list(num_map))


num_map = map(square_and_add_three, numbers, adds)

print(list(num_map))
