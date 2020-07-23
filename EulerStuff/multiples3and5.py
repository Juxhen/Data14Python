list_of_multiples = []
for x in range(0,1000):
    if x % 5 == 0:
        list_of_multiples.append(x)
    elif x % 3 == 0:
        list_of_multiples.append(x)

print(sum(list_of_multiples))