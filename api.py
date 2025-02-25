# import requests module for API request functionality
import requests


# Function to get Pokémon data from the PokeAPI
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        name = data['name']
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        types = [poke_type['type']['name'] for poke_type in data['types']]

        species_url = data['species']['url']
        evolution_chain = get_evolution_chain(species_url)

        return {
            'name': name,
            'abilities': abilities,
            'types': types,
            'evolution_chain': evolution_chain
        }
    else:
        return None


# Function to request evolution chain data to then parse using the parse_evolution_chain function.
def get_evolution_chain(species_url):
    response = requests.get(species_url, verify=False)

    if response.status_code == 200:
        species_data = response.json()
        evolution_chain_url = species_data['evolution_chain']['url']

        response = requests.get(evolution_chain_url, verify=False)
        if response.status_code == 200:
            evolution_data = response.json()
            return parse_evolution_chain(evolution_data['chain'])
    return None


# Function to correctly parse Pokémon evolution chain data since this is not a simple entry.
def parse_evolution_chain(chain):
    evolution_chain = []
    current = chain

    while current:
        evolution_chain.append(current['species']['name'])
        if current['evolves_to']:
            current = current['evolves_to'][0]
        else:
            current = None

    return evolution_chain


# Function to get just Pokémon names based on a .startswith search string.
# This helps user find viable Pokémon names to enter into get_pokemon_data function.
def get_pokemon_names_starting_with(search_string):
    url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
        all_pokemon = data['results']
        matching_pokemon = [pokemon['name'] for pokemon in all_pokemon if
                            pokemon['name'].startswith(search_string.lower())]
        return matching_pokemon
    else:
        return None


# Test data: replace with testing functionality via a test.py
# pokemon_name = "pikachu"
# pokemon_data = get_pokemon_data(pokemon_name)
#
# if pokemon_data:
#     print(f"Name: {pokemon_data['name']}")
#     print(f"Abilities: {', '.join(pokemon_data['abilities'])}")
#     print(f"Types: {', '.join(pokemon_data['types'])}")
#     print(f"Evolution Chain: {' -> '.join(pokemon_data['evolution_chain'])}")
# else:
#     print("Pokémon not found.")
#
# # Example usage of the new function
# search_string = "pi"  # Replace with any search string
# matching_pokemon = get_pokemon_names_starting_with(search_string)
#
# if matching_pokemon:
#     print(f"Pokémon names starting with '{search_string}': {', '.join(matching_pokemon)}")
# else:
#     print("No matching Pokémon found.")
