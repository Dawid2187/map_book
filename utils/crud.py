def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']} opublikował: {user['posts']}")

def add_new_user(users: list) -> None:
    Kogo_szukasz = input("Podaj imie znajomego:")
    for user in users:
        if user['name'] == Kogo_szukasz:
            print(user)
def search_user(users: list) -> None:
    Kogo_szukasz = input("Podaj imie znajomego:")
    for user in users:
        if user['name'] == Kogo_szukasz:
            print(user)
def remove_user(users)-> None:
    Kogo_szukasz=input("Podaj imie znajomego:")
    for user in users:
        if user['name']==Kogo_szukasz:
            users.remove(user)
            print(users)