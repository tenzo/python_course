class AddressException(Exception):
    pass


class ZipCodeException(AddressException):
    pass


def validate_zip_code(zip_code: str) -> None:
    if len(zip_code) != 6:
        raise ZipCodeException("Kod jest za krótki")
    elif '-' not in zip_code:
        raise ZipCodeException("Kod nie ma kreski")


if __name__ == '__main__':

    try:
        validate_zip_code('85-777')  # w tym miejscu wpisz niepoprawny kod
        print("Widocznie kod pocztowy jest poprawny")
    except IndexError:
        print("Zły indeks")
    except AddressException as ex:  # będzie działało również z ZipCodeException
        print("Niepoprawny adres: " + str(ex))
    finally:
        print("Nieważne co się stało - ja się wypiszę!")
    print("A tu kod idzie dalej")
