#prime factors of 13195 are 5,7,13,29
#largest prime factor of the number 600851475143

x = 600851475143
prime_factor_list = []
flag = False
while not flag:
    while x > 1:
        for y in range(1, 100000):
            if x % y == 0:
                x = x / y
                prime_factor_list.append(int(x))
                flag = True

print(prime_factor_list[-2])


