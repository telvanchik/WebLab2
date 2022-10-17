def newton(number, eps=0.001):
    a = float(number)
    prev_x = number

    while True:
        new_x = 0.5 * (prev_x + a / prev_x)
        if abs(new_x - prev_x) < eps:
            break

        prev_x = new_x

    return new_x


print(newton(225))
print(newton(783))