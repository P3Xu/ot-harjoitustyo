from database_connection import get_database_connection
from entities.default_set import DefaultSet

connection = get_database_connection()

def drop_tables():
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS meals;')
    cursor.execute('DROP TABLE IF EXISTS ingredients;')
    cursor.execute('DROP TABLE IF EXISTS meal_relations;')
    cursor.execute('DROP TABLE IF EXISTS menus;')
    cursor.execute('DROP TABLE IF EXISTS users')
    connection.commit()

def create_tables():
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE meals (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE meal_relations (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            ingredientID INTEGER REFERENCES ingredients
        );
    """)

    cursor.execute("""
        CREATE TABLE menus (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            userID INTEGER REFERENCES users,
            date DATE
        );
    """)

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
    """)

    connection.commit()

def insert_default_data():
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
        "INSERT INTO meal_relations (mealID, ingredientID) VALUES (?, ?)", relations)

    connection.commit()

def initialize_database():
    drop_tables()
    create_tables()
    insert_default_data()

if __name__ == "__main__":
    initialize_database()
