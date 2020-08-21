import random
from IPython.display import clear_output


#initial values        
random_pokemon = None
output = None
alreadyGuessed = ""
viable_guess = ""
hidden_list = []
Pokedex = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

# The game
def Hangman():
    random_pokemon = random.choice(Pokedex)
    random_pokemon = random_pokemon.lower()
    hidden_word = "_ " *len(random_pokemon)
    hidden_list = list(hidden_word)
    errors = 0
    alreadyGuessed = ""
    viable_guess = ""
    display = "".join(hidden_list) 
    while errors < 7:
        clear_output()
        if "_" not in hidden_list:
            clear_output()
            print(f"You got the word {random_pokemon}!")
            print("Thanks for playing!")
            break
        print(display)
        while True:
            print ('enter your letter')
            print(f"failed attempts:{errors}")
            Guess = input("your guess").lower()

            if len(Guess) != 1:
                print ('please enter only one letter')
            elif Guess in alreadyGuessed:
                print ('that letter has already been guessed. try again')
            elif Guess not in 'abcdefghijklmnopqrstuvwxyz':
                print ('only letters are acceptable guesses. try again.')
            else:
                viable_guess = Guess
                alreadyGuessed += Guess
                break
        if viable_guess in random_pokemon:
            indexed = [_ for _ in range(len(random_pokemon)) if random_pokemon.startswith(viable_guess, _)]
            for _ in indexed:
                _ += 1
                _ = (_ * 2) - 2 
                hidden_list[_] = viable_guess
                display = "".join(hidden_list)
        else:
            print("Incorrect guess. Try again...")
            errors += 1
            continue


Hangman()
Hangman()
Hangman()
Hangman()
Hangman()
Hangman()
Hangman()
Hangman()
