#!/usr/local/bin/python3

class Intern:

    def __init__(self, name="My name? I’m nobody, an intern, I have no name.") -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def work(self) -> str:
        raise Exception("I’m just an intern, I can’t do that...")

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def make_coffee(self) -> Coffee():
        return Intern.Coffee()


def main():
    print('Create intern with no Name...')
    intern = Intern()
    print(intern)
    print()
    print('Create intern Alex...')
    Alex = Intern('Alex')
    print('My name is', Alex)
    print()
    print('Intern is trying to work')
    try:
        intern.work()
    except Exception as e:
        print(e)
    print()
    print('Alex make coffee...')
    print(Alex.make_coffee())


if __name__ == '__main__':
    main()
