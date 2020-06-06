if __name__ == '__main__':
    # readline odczyta znaki w pliku aż do spotkania znaku nowej linii - nie jest to jednak arcywygodne
    with open('python_zen.txt') as file:
        while(True):
            line = file.readline()
            if line:
                print(line)
            else:
                break

    # możemy wczytać wszystkie linie naraz i otrzymać listę linii - nie jest to jednak odpowiednia metoda
    # przy dużych plikach
    with open('python_zen.txt') as file:
        lines = file.readlines()
        for line in lines:
            print(line)

    # w ten sposób iterujemy po "leniwym" iteratorze - linie wczytywane są po kolei, a nie na raz dzięki temu
    # nie skończy nam się pamięć
    with open('python_zen.txt') as file:
        for line in file:
            print(line)