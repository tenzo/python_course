if __name__ == '__main__':

    print('Przykład 1')
    try:
        names = ['Adam', 'Ola']
        print(names[2])  # zakomentuj tę linię i sprawdź, do którego bloku except trafimy
        number = 1 / 0

    except ZeroDivisionError:
        print("Dzielisz przez zero")
    except IndexError:
        print("Próbujesz pobrać element spoza tablicy")
    finally:
        print("To jest blok finally")

    print('Przykład 2')

    try:
        names = ['Adam', 'Ola']
        print(names[2])  # zakomentuj tę linię i sprawdź, do którego bloku except trafimy
        number = 1 / 0

    except Exception:  # klasa exception jest bazowa dla wszystkich (powiedzmy) wyjątków więc w ten sposób złapiemy wszystkie ich rodzaje w tym bloku
        print("Wystąpił jakiś wyjątek")
    finally:
        print("To jest blok finally")
