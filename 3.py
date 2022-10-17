def reverse(num):
    num_str = [d for d in str(num)]
    num_str.reverse()
    if num < 0:
        num_str.insert(0, num_str.pop())

    return int(''.join(num_str))

print(reverse((123)))
print(reverse(-359))