#import required modules for json and sqlite functions
import sqlite3
import json


# Function to create the "my_function_pokemon.db" database and "pokemon" table if they don't already exist.
# Creates the connection to sqlite local database and creates cursor.
def create_database():
    conn = sqlite3.connect("my_favourite_pokemon.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            name TEXT PRIMARY KEY,
            abilities TEXT,
            types TEXT,
            evolution_chain TEXT
        )
    """)
    conn.commit()
    conn.close()


# Function to insert Pokémon data from json file into database. Called from a menu function. Note: this is still json data. Future improvement might be to strip the data to a simpler format.
def insert_pokemon(pokemon_data):
    conn = sqlite3.connect("my_favourite_pokemon.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO pokemon (name, abilities, types, evolution_chain)
        VALUES (?, ?, ?, ?)
    """, (
        pokemon_data["name"],
        json.dumps(pokemon_data["abilities"]),
        json.dumps(pokemon_data["types"]),
        json.dumps(pokemon_data["evolution_chain"])
    ))
    conn.commit()
    conn.close()


# Function to delete Pokémon entries from database. Called from a menu function.
def delete_pokemon(pokemon_name):
    conn = sqlite3.connect("my_favourite_pokemon.db")
    c = conn.cursor()
    c.execute("""DELETE FROM pokemon WHERE name = ?""", (pokemon_name,))
    conn.commit()
    conn.close()


# Function to return data for Pokémon from local database. Using "LIKE" so that a partial match will return one or more matching Pokémon. Called from a menu function.
def search_pokemon(search_string):
    conn = sqlite3.connect("my_favourite_pokemon.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM pokemon WHERE name LIKE ?""", (f"%{search_string}%",))
    results = c.fetchall()
    conn.close()

    # Prints selected Pokémon details to screen. Note that this is stored in the database in json format. Future improvement might be to strip this to simpler format but not sure how to do that and keep the functionality of things like evolution chain.
    for row in results:
        name, abilities, types, evolution_chain = row
        print(f"Name: {name}")
        print(f"Abilities: {', '.join(json.loads(abilities))}")
        print(f"Types: {', '.join(json.loads(types))}")
        print(f"Evolution Chain: {' -> '.join(json.loads(evolution_chain))}")
        print()


# Function to select and print just the names of all Pokémon currently in the database, potentially to be used for the search_pokemon and delete_pokemon functions.
def display_all_pokemon():
    conn = sqlite3.connect("my_favourite_pokemon.db")
    c = conn.cursor()
    c.execute("SELECT name FROM pokemon")
    results = c.fetchall()
    conn.close()

    # Simple error-handling to return a response if nothing found.
    if results:
        print("Pokémon currently in your my_favourite_pokemon database:")
        for row in results:
            print(row[0])
    else:
        print("No Pokémon found in your database.")


# Test examples: need to add automated testing section using these.
# if __name__ == "__main__":
#     create_database()
#
#     # Insert a Pokémon record
#     pokemon_name = "pikachu"
#     pokemon_data = get_pokemon_data(pokemon_name)
#     if pokemon_data:
#         insert_pokemon(pokemon_data)
#
#     # Search for Pokémon records
#     search_string = "pi"
#     search_pokemon(search_string)
#
#     # Delete a Pokémon record
#     delete_pokemon("pikachu")