# # file = open("order.txt")
#
# # try:
# #     file = open("order.txt")
# # except:
# #     print("Error! PANIC!")
#
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("file not found!")
#     print(errmsg)
#     raise
# finally: # optional, outputs whatever happens even if its passed or failed
#     print("Finished handling everything")

# r - Read mode (Default)
# w - Write mode (if no file, creates one; if file, truncate)
# x - creates a new file (if there is a file it fails)
# a - append mode (writes things to the end of the file, if there is no file it creates one)
# t - text mode
# b - binary mode (open it in binary)
# + - reading and writing

def open_and_print_file(filename):
    try:
        with open("order.txt") as opened_file:
            file_line_list = opened_file.readlines()


        # for line in file_line_list:
        #     print(line.rstrip('\n'))

        # opened_file.close()

    except FileNotFoundError:
        print("File cannot be found, please check filename provided")
        raise

# to read a file
# with open("order.txt", "w") as opened_file:
#     opened_file.write("cheeseburger")

def write_to_file(filename):
    try:
        with open("order.txt", "w") as opened_file:
            opened_file.write("cheeseburger\n chicken")
    except FileNotFoundError:
        print("File cannot be found")
        raise


def appened_to_file(filename, order):
    try:
        with open(filename, "a") as opened_file:
            opened_file.write(order)
    except TypeError:
        print("File cannot be found")
        raise


appened_to_file("order.txt", "Pasta\n")
appened_to_file("order.txt", "Hotdog\n")
appened_to_file("order.txt", "Kebab\n")

# open_and_print_file("order.txt")
# write_to_file("order.txt")
# open_and_print_file("order.txt")




# file = open("order.txt")
# # order_lines = file.re
# print(1, file.readlines())
# print(2, file.readline())
# # print(1, file.readline())
# # print(2, file.readline())
# # print(3, file.readline())
# # print(4, file.readline())
# # print(5, file.readline())

# another way to open files

# with open("order.txt") as opened_file:
#     print(opened_file.readlines())
# open_and_print_file("order.txt")