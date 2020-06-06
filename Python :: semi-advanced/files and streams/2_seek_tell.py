if __name__ == '__main__':
    # operacje read i write przesuwają wskaźnik pliku
    # za pomocą seek można ten wskaźnik przesuwać ręcznie
    # za pomocą tell można odczytać bieżącą pozycję wskaźnika
    try:
        file = open('python_zen.txt')
        print(file.tell())
        print(file.read(8))
        print(file.tell())
        file.seek(45)
        print(file.tell())
        print(file.read(8))
        print(file.tell())
    finally:
        file.close()
