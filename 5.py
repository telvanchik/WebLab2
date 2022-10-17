def is_simple(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

print(is_simple(13))
print(is_simple(200))
print(is_simple(953))
print(is_simple(89))
print(is_simple(4))