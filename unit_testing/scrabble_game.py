# # import random as r
# #
# #
# class ScrabbleCalc:
#
#     def __init__(self):
#         self.one_point_words = ["a", "e", "i", "o", "u", "l", "n", "r", "s", "t"]
#         self.two_point_words = ["d", "g"]
#         self.three_point_words = ["b", "c", "m", "p"]
#         self.four_point_words = ["f", "h", "v", "w", "y"]
#         self.five_point_words = ["k"]
#         self.eight_point_words = ["j", "x"]
#         self.ten_point_words = ["q", "z"]
#         self.alphabet = (
#             "a", "b", "c", "d", "e", "f",
#             "g", "h", "i", "j", "k", "l",
#             "m", "n", "o", "p", "q", "r",
#             "s", "t", "u", "v", "w", "x",
#             "y", "z"
#         )
#         self.first_hand = []
#         self.score = 0
#         self.user_input = ""
#
#     def add_to_score(self, user_input):
#         self.user_input = user_input
#         for letter in user_input:
#             if letter in self.one_point_words:
#                 self.score += 1
#             elif letter in self.two_point_words:
#                 self.score += 2
#             elif letter in self.three_point_words:
#                 self.score += 3
#             elif letter in self.four_point_words:
#                 self.score += 4
#             elif letter in self.five_point_words:
#                 self.score += 5
#             elif letter in self.eight_point_words:
#                 self.score += 8
#             elif letter in self.ten_point_words:
#                 self.score += 10
#         print(self.score)
#
#     def starting_letters(self):
#         for x in range(7):
#             self.first_hand.append(self.alphabet[r.randint(0, 25)])
#         print(self.first_hand)
#
#     def get_user_input(self):
#         user_input = input("Please enter your word\n")
#         self.user_input = user_input
#         return self.user_input
#
#     def check_user_input(self, userinput):
#         userinput = self.user_input
#         isitvalid = False
#         if userinput.isalpha():
#             while not isitvalid:
#                 if len(userinput) > 7:
#                     print("please enter between 1 and 7 letters")
#                     self.check_user_input(self.add_to_score(self.get_user_input()))
#                     self.score = 0
#                 elif len(userinput) == 0:
#                     print("please enter at least 1 character")
#                     self.check_user_input(self.add_to_score(self.get_user_input()))
#                 else:
#                     return userinput
#                 isitvalid = True
#         else:
#             print("please enter only characters")
#             self.score = 0
#             self.check_user_input(self.add_to_score(self.get_user_input()))
#
#
#     def start_game(self):
#         juxhen.starting_letters()
#         juxhen.check_user_input(juxhen.add_to_score(juxhen.get_user_input()))
# #
# #
# # juxhen = ScrabbleCalc()
# #
# # juxhen.start_game()
#
#
# for i in range(0, 60):
#     print(f"hello + {i}")
#
#

list = [1,2,3,7,5,6,7,8,9,10]
list2 = ['a','b','d','g','h','z','p']
minimum = min(list)
maximum = max(list)
# sum , len, sorted()

sorted_list = sorted(list2)

print(sorted_list)