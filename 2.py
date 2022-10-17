def divisivle(numbers, divisor):
    return [num for num in numbers if num %divisor == 0]

num_list = [666, 20, 9, 1769, 1905, 65]

print('Делятся на 2: ')
print(divisivle(num_list, 2))
print('Делятся на 3: ')
print(divisivle(num_list, 3))
print('Делятся на 5: ')
print(divisivle(num_list, 5))