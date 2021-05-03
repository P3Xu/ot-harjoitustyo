from database_connection import get_database_connection
from entities.default_set import DefaultSet

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS meals;')
    cursor.execute('DROP TABLE IF EXISTS ingredients;')
    cursor.execute('DROP TABLE IF EXISTS relations;')
    cursor.execute('DROP TABLE IF EXISTS menus;')
    cursor.execute('DROP TABLE IF EXISTS users')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE meals (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE relations (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            ingredientID INTEGER REFERENCES commodities
        );
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE menus (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            date DATE
        );
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT
        );
    """)
    connection.commit()

def insert_default_data(connection):
    cursor = connection.cursor()
    default_set = DefaultSet()

    meals = [(meal,) for meal in default_set.meals]
    ingredients = [(ingredient,) for ingredient in default_set.ingredients]
    relations = default_set.create_db_relations()

    cursor.executemany(
        "INSERT INTO meals (name) VALUES (?)", meals)
    cursor.executemany(
        "INSERT INTO ingredients (name) VALUES (?)", ingredients)
    cursor.executemany(
        "INSERT INTO relations (mealID, ingredientID) VALUES (?, ?)", relations)

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_default_data(connection)

if __name__ == "__main__":
    initialize_database()
