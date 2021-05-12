from init_database import initialize_database
from init_default_set import initialize_default_set

def build():
    initialize_database()
    initialize_default_set()

if __name__ == "__main__":
    build()
