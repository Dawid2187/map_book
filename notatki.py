import psycopg2
import requests
import self
from bs4 import BeautifulSoup

db_params=psycopg2.connect(
    database="postgres",
    user="postgres",
    host="localhost",
    port="5432",
    password="postgres"
)

def add_user_to_table(db_params)-> None:
    name= input("Enter name: ")
    surname=input("Enter surname: ")
    posts=input("Enter posts: ")
    location=input("Enter location: ")
    url: str = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    response_html = BeautifulSoup(response.text, 'html.parser')
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    sql_add_query=f"INSERT INTO public.users( name, surname, post, location, coordinates) VALUES ('{name}', '{surname}', {posts}, '{location}', 'SRID=4326;POINT({longitude} {latitude})');"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    db_params.commit()

add_user_to_table(db_params)


def show_users(db_params)-> None:

    sql_add_query=f"SELECT * FROM public.users"
    cursor=db_params.cursor()
    cursor.execute(sql_add_query)
    #db_params.commit()
    users=cursor.fetchall()
    #print(users)
    for user in users:
        print(user)

#(db_params)

#DELETE FROM public.users
	#WHERE id=4

def remove_user_from_db(db_params)-> None:
    cursor = db_params.cursor()
    sql_remove_query=f"DELETE FROM public.users WHERE name='{input('Enter name')}';"
    cursor.execute(sql_remove_query)
    db_params.commit()


#remove_user_from_db(db_params)
#show_users(db_params)

#UPDATE public.users
	#SET name='aa', surname='bb', post='33'
	#WHERE id=4

def update_user_from_db(db_params)-> None:
    cursor = db_params.cursor()
    sql_update_query=f"UPDATE public.users SET name='{input('Enter name')}', surname='{input('Enter surname')}', post='{int (input('Enter posts'))}'WHERE id=5"
    cursor.execute(sql_update_query)
    db_params.commit()

#update_user_from_db(db_params)