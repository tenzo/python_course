from io import StringIO, BytesIO

if __name__ == '__main__':
    # zapis do bufora
    out = StringIO()
    out.write('Ala ma kota\n')
    out.write('Kot ma mleko')

    # odczyt zawartości całego bufora
    print(out.getvalue())

    out.close()  # pamięć bufora jest wyczyszczona - w przeciwieństwie do plików jego zawartość nie jest nigdzie zachowana

    # odczyt z bufora
    input = StringIO('Wartość początkowa bufora')

    # odczyt
    print(input.read(4))
    input.seek(8)
    print(input.read(4))