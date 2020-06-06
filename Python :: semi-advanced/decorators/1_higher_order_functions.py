from typing import Callable, List


def say_hello(name: str) -> None:
    print(f"Hello {name}!")


def say_goodbye(name) -> None:
    print(f"Goodbye {name}!")


def use_greeting(greeting: Callable, name: str) -> None:
    greeting(name)


if __name__ == '__main__':
    use_greeting(say_hello, 'Ola')
    use_greeting(say_goodbye, 'Ola')
    use_greeting(say_goodbye, 'Przemek')
