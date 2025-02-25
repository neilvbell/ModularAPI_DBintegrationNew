This project is an example of a simple API and SQLite integration coded in python.
Run main.py to access a command line menu interface:

Menu:
1. Search for any Pokémon names beginning with the following letters
2. Get details for a Pokémon with the following name
3. Display names of the Pokémon in your my_favourite_pokemon database
4. Get details for a Pokémon in your my_favourite_pokemon database with the following name
5. Delete a Pokémon from your my_favourite_pokemon database with the following name
6. Exit
Enter the number to select your choice:

Enter a number and press enter to select one of the options.
1. Will search for any Pokemon names that begins with the letters that you type. e.g.: cha will return all pokemon names starting with "cha", such as charmander, charizard, etc. This can be used to find viable names to enter into option 2.
2. Enter a full valid Pokemon name. This will return name, abilities, type and evolution chain for that Pokemon. Press y and enter to add the Pokmeon data to a local database of your favourite. Press n or any other input and enter to return to the menu without adding to the local database.
3. Show a list of names of the Pokemon in the local database.
4. Enter a valid Pokemon name, or start of names, to return details of any matching Pokmeon in your local database.
5. Enter a valid Pokemon name to delete that Pokemon from your local database.
6. Exit the script.
