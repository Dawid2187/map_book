from models.data import users
from utils.crud import show_users
from utils.crud import add_new_user
from utils.crud import remove_user
from utils.crud import search_user




if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("MENU:")
        print("0. Zakończ program")
        print("1. Wyświetl co u znajomych:")
        print("2. Dodaj użytkownika:")
        print("3. Usuń użytkownika:")
        print("4. Znajdz użytkownika:")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
            add_new_user(users)
        if menu_option == "3":
            remove_user(users)
        if menu_option == "4":
            search_user(users)
