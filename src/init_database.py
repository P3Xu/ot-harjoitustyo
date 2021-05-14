"""Moduuli, joka alustaa tarvittavat tietokantarakenteet tietokantaan."""

from database_connection import get_database_connection

connection = get_database_connection()

def drop_tables():
    """Poistaa samannimiset taulut, mikäli sellaisia on jo olemassa."""

    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS meals;')
    cursor.execute('DROP TABLE IF EXISTS ingredients;')
    cursor.execute('DROP TABLE IF EXISTS meal_relations;')
    cursor.execute('DROP TABLE IF EXISTS menus;')
    cursor.execute('DROP TABLE IF EXISTS users')
    connection.commit()

def create_tables():
    """Luo tarvittavat tietokantataulut kantaan."""

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
            userID INTEGER REFERENCES users,
            mealID INTEGER REFERENCES meals,
            ingredientID INTEGER REFERENCES ingredients,
            PRIMARY KEY(userID, mealID, ingredientID)
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

def initialize_database():
    """Kutsuu alustusmetodeja."""

    drop_tables()
    create_tables()

if __name__ == "__main__":
    initialize_database()
