the_list = [1, 2]
even_numbers_list = []

flag = False
while not flag:
    next_num = the_list[-1] + the_list[-2]
    if next_num <= 4000000:
        the_list.append(next_num)
        if next_num % 2 == 0:
            even_numbers_list.append(next_num)
    else:
        flag = True
print(sum(even_numbers_list) + 2)
