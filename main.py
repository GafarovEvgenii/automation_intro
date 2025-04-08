username = input('What is your name?')


def greet(name):
    print(f'Hello {name}!')


if username.startswith('E'):
    greet(username)
else:
    greet('world')
