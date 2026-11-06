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
for index, item in enumerate(data):
    print(item["id"],":" ,item["name"][f"{x}"])
y = input("Shearch a type: ")
if y == item["type"]:
    for index, item in enumerate(data):
        print(item["id"],":" ,item["name"][f"{x}"], item["type"])