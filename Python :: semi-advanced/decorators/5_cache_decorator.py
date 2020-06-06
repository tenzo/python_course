from collections import defaultdict
from functools import wraps

cache_dict = defaultdict(dict)


# Struktura słownika cache'ującego:
# {
#     'multiply': {
#         (2, 3): 6,
#         (1, 2): 2
#     }
#     'divide': {
#         (6,2): 3
#     }
# }

def cache(func):
    '''Działa tylko z operacjami przemiennymi'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache_dict[func.__name__]:
            print('Zwracam wynik używając cache')
            return cache_dict[func.__name__][args]
        else:
            result = func(*args, **kwargs)
            cache_dict[func.__name__][args] = result
            return result

    return wrapper


@cache
def multiply(a, b):
    return a * b


@cache
def divide(a, b):
    return a / b


if __name__ == '__main__':
    print(multiply(1, 2))
    print(multiply(2, 3))
    print(multiply(2, 3))
    print(multiply(6, 5))
    print(divide(6, 5))
    print(divide(6, 5))

    print(f'Słownik cache\'ujący: {cache_dict}')

