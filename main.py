from models.data import users
from utils.crud import show_users
from utils.crud import add_new_user




if __name__ == "__main__":
    print("Witaj użytkowniku")
    while True:
        print("MENU:")
        print("0. Zakończ program")
        print("1. Wyświetl co u znajomych:")
        print("2. Dodaj użytkownika:")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
            add_new_user(users)
