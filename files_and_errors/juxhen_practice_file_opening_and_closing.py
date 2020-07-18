class JuxhenFile:

    def __init__(self):
        with open("Juxhen's Dream Cars.txt", "a") as juxhenscars:
            juxhenscars.write("Ferrari 488\n"
                             "Mercedes-Benz G6X6\n"
                             "Mercedes-Benz S65\n")


JuxhenFile()

# def append_to_file():
#
#
#     def write_to_file(filename):
#         try:
#             with open("order.txt", "w") as opened_file:
#                 opened_file.write("cheeseburger\n chicken")
#         except FileNotFoundError:
#             print("File cannot be found")
#             raise
#
#
#     appened_to_file("order.txt", "Pasta\n")
#     appened_to_file("order.txt", "Hotdog\n")
#     appened_to_file("order.txt", "Kebab\n")