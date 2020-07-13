# # Don't
# # Repeat
# # Yourself
#
# def print_something():
#     print("Something!")
#
# print_something()
#
# def print_something_multiple(something, number_of_times):
#     string_to_print = something * number_of_times
#     print(string_to_print)
#
# print_something_multiple("woohoo",3)
#
def repeat_string(string_to_repeat,number_of_repeats):
    string_to_return = string_to_repeat * number_of_repeats
    return string_to_return


 print(repeat_string("woohoo",3))
#
#
# def addition(x1, x2):
#     output = x1+x2
#     return output

# returns all numbers multiplied together.
#
# def find_product(*multiargs):
#     if len(multiargs) <1:
#         return None
#     else:
#         product = 1
#         for num in multiargs:
#             product *= num
#     return product
#
#
# print(find_product(1, 2, 3, 4, 5))

