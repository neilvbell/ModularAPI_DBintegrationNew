# Importing functions from my package files
from api import get_pokemon_data, get_pokemon_names_starting_with
from sqlite import create_database, insert_pokemon, delete_pokemon, search_pokemon, display_all_pokemon


# Menu search function to find Pokémon names by input search string.
# This will help the user identify viable names to input into get_pokemon_details.
def search_pokemon_names():
    search_string = input("Enter the starting letters of the Pokémon names you want to search for: ")
    # Calling one of the api.py functions
    matching_pokemon = get_pokemon_names_starting_with(search_string)

    # Some simple error handling to allow for incorrect names
    if matching_pokemon:
        print(f"Pokémon names starting with '{search_string}': {', '.join(matching_pokemon)}")
    else:
        print("No matching Pokémon found.")


# Menu function to get details of a viable Pokémon.
def get_pokemon_details():
    pokemon_name = input("Enter the name of the Pokémon you want to get details for: ")
    # Calling one of the api.py functions
    pokemon_data = get_pokemon_data(pokemon_name)

    # "If" statement for simple error-handling if no data is returned, such as from an incorrect Pokémon name.
    if pokemon_data:
        print(f"Name: {pokemon_data['name']}")
        print(f"Abilities: {', '.join(pokemon_data['abilities'])}")
        print(f"Types: {', '.join(pokemon_data['types'])}")
        print(f"Evolution Chain: {' -> '.join(pokemon_data['evolution_chain'])}")

        # User option to add Pokémon details from api request to database
        store = input("Do you want to store this Pokémon in your database of favourite Pokémon? (y/n): ")
        if store.lower() == "y":
            # Calling one of the sqlite.py functions
            insert_pokemon(pokemon_data)
            print(f"{pokemon_name} has been added to your database of favourite Pokémon.")
        else:
            print("Not added to database.")
    else:
        print("Pokémon not found.")


# Menu function to display names of all Pokémon currently in the database.
def display_all_favourite_pokemon():
    # Calling one of the sqlite.py functions
    display_all_pokemon()


# Menu function to get details of Pokémon from the database. As LIKE was used this should also accept starting strings.
def get_favourite_pokemon_details():
    pokemon_name = input("Enter the name of the Pokémon in your database you want to get details for: ")
    # Calling one of the sqlite.py functions
    search_pokemon(pokemon_name)


# Menu function to delete entry of named Pokémon from the database.
def delete_favourite_pokemon():
    pokemon_name = input("Enter the name of the Pokémon you want to delete from your database: ")
    # Calling one of the sqlite.py functions. Used = to match so shouldn't delete more than the named Pokémon.
    delete_pokemon(pokemon_name)
    print(f"{pokemon_name} has been deleted from your database of favourite Pokémon.")


# Main menu function. This is the starting function and runs a while loop to display and return to the menu until exited.
def main_menu():
    # Calling one of the sqlite.py functions. This will create the database if it doesn't already exist.
    create_database()

    while True:
        print("\nMenu:")
        print("1. Search for any Pokémon names beginning with the following letters")
        print("2. Get details for a Pokémon with the following name")
        print("3. Display names of the Pokémon in your my_favourite_pokemon database")
        print("4. Get details for a Pokémon in your my_favourite_pokemon database with the following name")
        print("5. Delete a Pokémon from your my_favourite_pokemon database with the following name")
        print("6. Exit")

        choice = input("Enter the number to select your choice: \n")
        # "match: case" selection rather than nested "if" as I am just using a small range of set options.
        match choice:
            case "1":
                search_pokemon_names()
            case "2":
                get_pokemon_details()
            case "3":
                display_all_favourite_pokemon()
            case "4":
                get_favourite_pokemon_details()
            case "5":
                delete_favourite_pokemon()
            case "6":
                print("Thank you for using my pokemon data app. \nThe database will still be here for next time. \nHave a nice day!")
                # I looked up a more formal way to exit rather than just using break, since that is to exit a loop, whereas I want to exit the script entirely.
                exit(0)
            # Simple error-handling if an invalid character is used.
            case _:
                print("Invalid choice. Please try again with one of the menu numbers then enter.")

# Call the main_menu() function to trigger the script.
if __name__ == "__main__":
    main_menu()



# Future improvements:
# Unit testing: add some basic unit testing to confirm some known results for the various user options.

# Export database data to a CSV. Potentially include a way to import as well. Might be awkward with json data so potentially need to sanitize the data before export?
