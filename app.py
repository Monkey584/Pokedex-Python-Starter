import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
x = input("Select a language(english/japanese/chinese/french): ")
pokedex = open("./pokedex.json", encoding="utf8")
type = open("./types.json", encoding="utf8")
data = json.load(pokedex)
typing = json.load(type)

while x not in ["english", "japanese", "chinese", "french"]:
    x = input("The is not a language in the data, please reselect english, japanese, chinese or french: ")
else:
    for pokemon in data:
        print(pokemon["name"][x])

y = input("Search a type or a name: ")
matching_type = next(
    (
        pokemon_type
        for pokemon_type in typing
        if y.strip().casefold()
        == pokemon_type.get(x, pokemon_type["english"]).casefold()
    ),
    None,
)
matching_name = next(
    (  
        pokemon_name
        for pokemon_name in data
        if y.strip().casefold()
        == pokemon_name.get(x, pokemon_name["name"]["english"]).casefold()
    ),
    None,
)
if matching_type or matching_name is None:
    print(f"No Pokémon type or name was found for: {y}")
else:
    matches = [
        pokemon
        for pokemon in data
        if matching_type["english"] in pokemon["type"]
    ]
    names = [
        pokemon
        for pokemon in data
        if matching_name["english"] in pokemon["name"]
    ]
    if matches:
        for pokemon in matches:
            print(pokemon["name"][x])
    if names:
        for pokemon in names:
            print(pokemon["name"][x])

