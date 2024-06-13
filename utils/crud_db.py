import psycopg2

db_params = psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    port="5432",
    password="postgres"
)


def add_user_to_table(db_params) -> None:
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    posts = input("Enter posts: ")
    location = input("Enter location: ")

    sql_add_query = f"INSERT INTO public.users( name, surname, post, location, coordinates) VALUES ('{name}', '{surname}', {posts}, '{location}', 'SRID=4326;POINT(21.0 52.23)');"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()


def show_users(db_params) -> None:
    sql_add_query = f"SELECT * FROM public.users"
    cursor = db_params.cursor()
    cursor.execute(sql_add_query)
    users = cursor.fetchall()
    for user in users:
        print(user)


show_users(db_params)


def remove_user_from_db(db_params) -> None:
    cursor = db_params.cursor()
    sql_remove_query = f"DELETE FROM public.users WHERE name='{input('Enter name')}';"
    cursor.execute(sql_remove_query)
    db_params.commit()


def update_user_from_db(db_params) -> None:
    cursor = db_params.cursor()
    sql_update_query = f"UPDATE public.users SET name='{input('Enter name')}', surname='{input('Enter surname')}', post='{int(input('Enter posts'))}'WHERE id=5"
    cursor.execute(sql_update_query)
    db_params.commit()


update_user_from_db(db_params)
