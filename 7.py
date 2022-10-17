def decorator(func, *args):
    cache = {}
    def caching(*args):
        print('\n')
        print('Текущие аргументы =', args)
        print('КЭШ =', cache)
        if cache.get(args):
            return cache[args]
        else:
            cache[args] = func(*args)
            return cache[args]
    return caching

@decorator
def summator(*args):
    return sum(args)

print('result =', summator(1, 2))
print('result =', summator(7, 6))
print('result =', summator(1, 2, 3))
print('result =', summator(9, 0, 4))
