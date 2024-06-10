# import requests
# print("Hello world")
# r = requests.get("https://example.org")
# print(r.status_code)
# print(r.text)
# print("Bye")

import click
from domain.dto.user_dto import User

@click.command()
@click.argument('name')
@click.argument('password')
@click.option('--email', '-e', default='')
@click.option('--active', '-a', is_flag=True, default=True)
def main(name, password, email, active):
    user = User(name, password, email, active)
    print(user)

if __name__ == '__main__':
    main()