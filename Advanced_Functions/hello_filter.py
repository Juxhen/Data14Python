students = ["DAVID", "Lee", "RICHARD"]

result = filter(str.isupper, students)
#filter keeps anything that (str.isupper) returns true in the list students
print(list(result))


def t_or_f(x):
    return x % 6 == 0

print(t_or_f(7))

numbers = list(range(1,100))

print(list(filter(t_or_f, numbers)))

# def check_length(word, lentgh1, length2):
#     return len(word) == lentgh1 or len(word) == length2