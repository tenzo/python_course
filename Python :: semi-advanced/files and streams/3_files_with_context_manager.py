if __name__ == '__main__':

    # preferowanym sposobem otwierania pliku w pythonie jest użycie managera kontekstu:
    with open('python_zen.txt') as file:
        print(file.read())
        print("W tym miejscu plik jest jeszcze otwarty")

    print("Dalsza część programu")

    # zapis:
    with open('some_text.txt', 'w') as file:
        file.write('Ala ma kota\n')
        file.write('Kot ma czołg\n')
