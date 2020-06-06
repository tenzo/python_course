from typing import Any


class FloatParamException(Exception):
    pass


class StrParamException(Exception):
    pass


class IntParamException(Exception):
    pass


def create_message(param: Any) -> str:
    return "Przekazano parametr o wartości " + str(param)


def raise_exception(param: Any) -> bool:
    if isinstance(param, float):
        raise FloatParamException(create_message(param))
    elif isinstance(param, int):
        if isinstance(param, bool):
            return True
        raise IntParamException(create_message(param))
    elif isinstance(param, str):
        raise StrParamException(create_message(param))
    else:
        return True


if __name__ == '__main__':

    parameter = 'hello'

    try:
        another_type = raise_exception(parameter)
        if another_type:
            print("Paramatr nie jest ani typu float, ani typu" + \
                  "string, ani typu int, jest typu " + str(type(parameter)))
        raise IndexError
    except (FloatParamException, IntParamException, StrParamException) as ex:  # to jest zbiorcze przechwytywanie
        print("Type exception: " + str(ex))
    # poniżej każdy z typów jest przechwytytwany w oddzielnym bloku except
    # except FloatParamException as ex:
    #     print("Float: " + str(ex))
    # except IntParamException as ex:
    #     print("Int: " + str(ex))
    # except StrParamException as ex:
    #     print("Str: " + str(ex))
    finally:
        print("Ten blok wykona się zawsze")

    # .....

    print("Dalsza część programu")
