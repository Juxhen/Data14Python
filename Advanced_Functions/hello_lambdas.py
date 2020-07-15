#Lambda

#Anonymous Functions


# def add(n1,n2):
#     return n1 + n2
#
#
# print(add(2,2))
#
# add_lambda = lambda n1, n2: n1 + n2
# print(add_lambda(5,99))

# using lambda with map

# numbers = [181, 2384, 2, 283, 3]
#
# results = map(lambda x: x * x + 3, numbers)
# print(list(results))

savings = [234.00, 555.00, 674.00, 78.00]
# results2 = map(lambda x: x + (x*0.1), savings)
# # print(list(results2))
#
# even_savings = map(lambda x: x%2 == 0, savings)

# using lambda with filter
even_savings = list(filter(lambda x: x % 2 == 0, savings))
print(even_savings)
