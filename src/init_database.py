from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS meals;')
    cursor.execute('DROP TABLE IF EXISTS ingredients;')
    cursor.execute('DROP TABLE IF EXISTS relations;')
    cursor.execute('DROP TABLE IF EXISTS menus;')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')
    connection.commit()

    cursor.execute('''
        CREATE TABLE meals (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')
    connection.commit()

    cursor.execute('''
        CREATE TABLE relations (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            ingredientID INTEGER REFERENCES commodities
        );
    ''')
    connection.commit()

    cursor.execute('''
        CREATE TABLE menus (
            id INTEGER PRIMARY KEY,
            mealID INTEGER REFERENCES meals,
            date DATE
        );
    ''')
    connection.commit()


def insert_test_data(connection):
    cursor = connection.cursor()

    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Makaronilaatikko\');')  # 1| 1,2,3
    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Kanasalaatti\');')  # 2| 4,5
    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Uunimakkara\');')  # 3| 6,7
    # 4| 8,9,10,11,12
    cursor.execute('INSERT INTO meals (name) VALUES (\'Pizza\');')
    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Pinaattilätyt\');')  # 5| 13
    # 6| 1,3,14,15
    cursor.execute('INSERT INTO meals (name) VALUES (\'Kaalilaatikko\');')
    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Possuwokki\');')  # 7| 16, 17
    cursor.execute(
        'INSERT INTO meals (name) VALUES (\'Kalapuikot\');')  # 8| 18

    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Jauheliha\');')  # 1
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Makaroni\');')  # 2
    cursor.execute('INSERT INTO ingredients (name) VALUES (\'Sipuli\');')  # 3
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Kanan fileesuikale\');')  # 4
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Salaatti\');')  # 5
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Lenkkimakkara\');')  # 6
    cursor.execute('INSERT INTO ingredients (name) VALUES (\'Juusto\');')  # 7
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Kinkkusuikale\');')  # 8
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Ananaspalat\');')  # 9
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Aurajuusto\');')  # 10
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Pizzajauhot\');')  # 11
    cursor.execute('INSERT INTO ingredients (name) VALUES (\'Hiiva\');')  # 12
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Pinaattilätty\');')  # 13
    cursor.execute('INSERT INTO ingredients (name) VALUES (\'Kaali\');')  # 14
    cursor.execute('INSERT INTO ingredients (name) VALUES (\'Riisiä\');')  # 15
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Possun fileesuikale\');')  # 16
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Wokkivihannekset\');')  # 17
    cursor.execute(
        'INSERT INTO ingredients (name) VALUES (\'Kalapuikot\');')  # 18

    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (1,1);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (1,2);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (1,3);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (2,4);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (2,5);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (3,6);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (3,7);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (4,8);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (4,9);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (4,10);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (4,11);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (4,12);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (5,13);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (6,1);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (6,3);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (6,14);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (6,15);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (7,16);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (7,17);')
    cursor.execute(
        'INSERT INTO relations (mealID, ingredientID) VALUES (8,18);')
    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_test_data(connection)


if __name__ == "__main__":
    initialize_database()
