def outer_function(name: str):
    print('Funkcja outer: ' + name)

    def inner_function(name: str, repeats: int):
        print('Funkcja inner')
        return name * repeats

    print('Wynik inner: ' + inner_function(name, 3))
    return inner_function


if __name__ == '__main__':
    outer_function('Paweł')
