from functools import wraps
from typing import Callable


def greeting_decorator(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)

    return wrapper


@greeting_decorator
def print_name(name):
    '''Wypisuje imię'''
    print(name)


@greeting_decorator
def print_name_and_lastname(name, lastname):
    '''wypisuje imię i nazwisko'''
    print(name + ' ' + lastname)


if __name__ == '__main__':
    print_name('Ola')
    print_name_and_lastname('Paweł', 'Kmiecik')

    help(print_name)
    help(print_name_and_lastname)
