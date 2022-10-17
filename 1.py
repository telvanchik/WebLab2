def is_palindrome(num):
    num_list = [int(d) for d in str(num)]
    return num_list == list(reversed(num_list))

print(is_palindrome(25152))
print(is_palindrome(23152))
print(is_palindrome(1234567890))
print(is_palindrome(666))
