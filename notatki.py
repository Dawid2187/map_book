from models.data import users
from utils.crud import show_users


def remove_user(users) -> None:
    Kogo_szukasz = input("Podaj imie znajomego:")
    for user in users:
        if user['name'] == Kogo_szukasz:
            users.remove(user)
            print(users)


def search_user(users) -> None:
    kogo_szukasz = input("Podaj imie znajomego:")
    for user in users:
        if user['name'] == kogo_szukasz:
            print(user)


#funkcja edycji uzytkownika
def update_user(users) -> None:
    Kogo_szukasz = input("Podaj imie znajomego:")
    for user in users:
        if user['name'] == Kogo_szukasz:
            user['name'] = input("Podaj nowe imie:")
            user['surname'] = input("Podaj nowe nazwisko:")
            user['posts'] = input("Podaj nową liczbę postów:")

print(users)
update_user(users)
print(users)
