if __name__ == '__main__':

    # Naiwne i niezbyt bezpieczne otwarcie i odczytanie pliku
    file = open('python_zen.txt')
    print(file.read())
    file.close()
    print(file.closed)

    # Nieco lepsza obsługa pliku - plik zawsze będzie zamknięty
    try:
        file = open('python_zen.txt')
        content = file.read()
        print(content)
    finally:
        file.close()

    # zapis:
    try:
        file = open('some_text.txt', 'a')
        file.write(content)
    finally:
        file.close()
