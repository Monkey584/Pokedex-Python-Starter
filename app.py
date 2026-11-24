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
x = input("Select a language(english/japanese/chinese/french): ").casefold()
pokedex = open("./pokedex.json", encoding="utf8")
poketype = open("./types.json", encoding="utf8")
pokemoves = open("./moves.json", encoding="utf8")
data = json.load(pokedex)
type = json.load(poketype)
moves = json.load(pokemoves)

while x not in ["english", "japanese", "chinese", "french"]:
    x = input("The is not a language in the data, please reselect english, japanese, chinese or french: ")
else:
    for pokemon in data:
        print(pokemon["name"][x])

y = input("Search a type: ")
matching_type = next(
    (
        pokemon_type
        for pokemon_type in type
        if y.strip().casefold()
        == pokemon_type[x].casefold or pokemon_type["english"].casefold()
    ),
    None
)
if matching_type is None:
    print(f"No Pokémon type was found for: {y}")
else:
    matches = [
        pokemon
        for pokemon in data
        if matching_type["english"] in pokemon["type"]
    ]
    if matches:
        for pokemon in matches:
            print(pokemon["name"][x])

z = input("Search a name: ")
names = []
for pokemon in data:
    if z.strip().casefold() in pokemon["name"].get(x, pokemon["name"]["english"]).casefold():
        names.append(pokemon)

if not names:
    print(f"No Pokémon named {z} was found")
else:
    for pokemon in names:
        print(pokemon["name"][x])

m = input("Search for a pokemon to find possible moves: ")
matching_name = next(
    (
        pokemon_name
        for pokemon_name in data
        if m.strip().casefold()
        == pokemon_name["name"].get(x, pokemon_name["name"]["english"]).casefold()
    ),
    None
)
if matching_name is None:
    print(f"No Pokémon type was found for: {y}")
else:
    name = [
        pokemon
        for pokemon in data
        if matching_name["name"]["english"] in pokemon["name"]["english"]
    ]
    if name:
        for pokemon in name:
            print(pokemon["name"][x])
learn = next(
    (
    pokemon_move
    for pokemon_move in moves
    if pokemon_move["type"]
    in matching_name["type"]
    ),
    None
)
if learn is None:
    print(f"No moves for {matching_name["name"][x]}")
else:
    move = [
        pokemon
        for pokemon in matching_name
        if learn["type"] in matching_name["type"]
    ]
    if move:
        for pokemon_move in moves:
            print(pokemon_move["ename"])