import random

# Dictionary with the categories and words of the game.
categories = {"animals": ["dog",
                          "cat",
                          "elephant",
                          "lion",
                          "tiger",
                          "giraffe",
                          "monkey",
                          "bear",
                          "rabbit",
                          "snake",
                          "dolphin",
                          "penguin",
                          "kangaroo",
                          "fox",
                          "wolf",
                          "horse",
                          "zebra",
                          "gorilla",
                          "owl",
                          "eagle"],
              "technology": ["computer",
                             "software",
                             "hardware",
                             "internet",
                             "programming",
                             "algorithm",
                             "database",
                             "cybersecurity",
                             "encryption", "network",
                             "server",
                             "cloud",
                             "smartphone",
                             "tablet",
                             "laptop",
                             "router",
                             "mouse",
                             "keyboard",
                             "monitor"],
              "sports": ["soccer",
                         "basketball",
                         "tennis",
                         "swimming",
                         "volleyball",
                         "baseball",
                         "golf",
                         "cycling",
                         "boxing",
                         "running",
                         "skiing",
                         "surfing",
                         "wrestling",
                         "cricket",
                         "rugby",
                         "hockey",
                         "badminton",
                         "athletics",
                         "climbing"],
              "vehicles": ["car",
                           "truck",
                           "bus",
                           "motorcycle",
                           "bicycle",
                           "train",
                           "airplane",
                           "helicopter",
                           "boat",
                           "ship",
                           "submarine",
                           "scooter",
                           "van",
                           "taxi",
                           "ambulance",
                           "firetruck",
                           "tractor",
                           "spaceship",
                           "rocket"],
              "professions": ["actor",
                              "artist",
                              "baker",
                              "chef",
                              "doctor",
                              "engineer",
                              "firefighter",
                              "journalist",
                              "lawyer",
                              "musician",
                              "nurse",
                              "painter",
                              "photographer",
                              "pilot",
                              "plumber",
                              "scientist",
                              "teacher",
                              "veterinarian",
                              "writer"],
              "fruits": ["apple",
                         "banana",
                         "blueberry",
                         "cherry",
                         "grape",
                         "kiwi",
                         "lemon",
                         "mango",
                         "orange",
                         "peach",
                         "pear",
                         "pineapple",
                         "plum",
                         "raspberry",
                         "strawberry",
                         "watermelon",
                         "apricot",
                         "blackberry",
                         "cranberry",
                         "fig"],
              "countries": ["argentina",
                            "australia",
                            "brazil",
                            "canada",
                            "china",
                            "egypt",
                            "france",
                            "germany",
                            "india",
                            "italy",
                            "japan",
                            "mexico",
                            "nigeria",
                            "russia",
                            "eeuu",
                            "spain",
                            "sweden",
                            "thailand",
                            "turkey",
                            "ireland"],
              "instruments": ["accordion",
                              "banjo",
                              "cello",
                              "clarinet",
                              "drums",
                              "flute",
                              "guitar",
                              "harp",
                              "keyboard",
                              "mandolin",
                              "oboe",
                              "piano",
                              "saxophone",
                              "trombone",
                              "trumpet",
                              "ukulele",
                              "violin",
                              "xylophone",
                              "zither"],
              "clothes": ["shirt",
                          "pants",
                          "dress",
                          "skirt",
                          "jacket",
                          "sweater",
                          "coat",
                          "blouse",
                          "jeans",
                          "shorts",
                          "hat",
                          "scarf",
                          "gloves",
                          "socks",
                          "shoes",
                          "boots",
                          "tie",
                          "belt",
                          "hoodie",
                          "sneakers"],
              "colors": ["red",
                         "orange",
                         "yellow",
                         "green",
                         "blue",
                         "purple",
                         "pink",
                         "brown",
                         "black",
                         "white",
                         "gray",
                         "cyan",
                         "magenta",
                         "turquoise",
                         "lavender",
                         "maroon",
                         "gold",
                         "silver",
                         "teal",
                         "olive"]}


class Player:
    """
    Create an instance of the player class
    """
    def __init__(self, name):
        self.name = name
        self.tries = 0  # Attribute specific to each instance
        self.correct_points = 0
        self.wrong_points = 0
        self.letters = []
        self.wrong_words = []

    def add_points(self, name_counter):
        """
        Adds points to the counter you specify as argument
        """
        if name_counter == "tries":
            self.tries += 1
        elif name_counter == "correct_points":
            self.correct_points += 1
        else:
            self.wrong_points += 1

    def add_to_list(self, name_list, letter):
        """
        Adds a letter or word to the list you specify
        """
        if name_list == "letters":
            self.letters.append(letter)
        else:
            self.wrong_words.append(letter)


def main():
    """
    Main function that is in charge of creating the navigation menu,
    validating the answers, and using the rest of the functions.
    """
    categories_list = [x for x in categories.keys()]
    main_menu = True
    selection = ""
    start_game = False
    current_category = ""
    new_player = ""
    while True:
        # This if is responsible for creating an instance of the player class.
        if main_menu:
            try:
                player_name = input("\nEnter your name: ").strip()
                if player_name.isalpha():
                    new_player = Player(player_name.capitalize())
                    main_menu = False
                else:
                    print("Only letters and no spaces are allowed")
            except KeyboardInterrupt:
                print("\nKeyboard interruption detected, try again.")

        # When selecting a category in the else executes this elif.
        elif start_game:
            print(f"\nYou are playing with the '{current_category}' category\nType 'back' to choose another category\n-Words you got right: {new_player.correct_points}\n-Words you didn't get right: {new_player.wrong_points}\n")
            new_player.letters = []
            new_player.wrong_words = []
            display_hangman(0)
            word = select_a_word(current_category).upper()
            player_word = display_underscores(word, new_player.letters)
            new_player.tries = 0

            while new_player.tries != 6 and player_word != word:
                try:
                    letter_or_word = input("\n\nGuess a letter or a word: ").upper().strip()

                    if letter_or_word == "BACK":
                        start_game = False
                        break

                    # Enter this if it is not an empty string if it is not in both lists and if it is alphanumeric.
                    elif letter_or_word != "" and letter_or_word not in new_player.letters and letter_or_word not in new_player.wrong_words and letter_or_word.isalpha():
                        # If the word is exactly the same, the game will end and you will earn one point.
                        if letter_or_word == word:
                            letters = [letter for letter in word]
                            display_hangman(new_player.tries)
                            player_word = display_underscores(word, letters)
                        # This line checks if you are guessing only one letter and that it is included in the word.
                        elif letter_or_word in word and len(letter_or_word) == 1:
                            new_player.add_to_list("letters", letter_or_word)
                            print(f"\n\nUsed letters: {new_player.letters}")
                            print(f"Used words: {new_player.wrong_words}")
                            display_hangman(new_player.tries)
                            player_word = display_underscores(word, new_player.letters)
                        # It will enter this else if you don't get a letter or word right and draw a part of the hangman.
                        else:
                            new_player.add_to_list("letters", letter_or_word) if len(letter_or_word) == 1 else new_player.add_to_list("wrong_words", letter_or_word)
                            print(f"\n\nUsed letters: {new_player.letters}")
                            print(f"Used words: {new_player.wrong_words}")
                            new_player.add_points("tries")
                            display_hangman(new_player.tries)
                            display_underscores(word, new_player.letters)

                    # #If not, it will inform you that something has gone wrong but it will count as a hit or miss.
                    else:
                        print(f"\n\nUsed letters: {new_player.letters}")
                        print(f"Used words: {new_player.wrong_words}")
                        print(f"You've already used: {letter_or_word}") if letter_or_word in new_player.letters or letter_or_word in new_player.wrong_words else print("No valid letters or words found")
                        display_hangman(new_player.tries)
                        display_underscores(word, new_player.letters)

                # In case of keyboard interruption it will allow you to continue playing.
                except KeyboardInterrupt:
                    print("\nKeyboard interruption detected, try again.")
                    print(f"\n\nUsed letters: {new_player.letters}")
                    print(f"Used words: {new_player.wrong_words}")
                    display_hangman(new_player.tries)
                    display_underscores(word, new_player.letters)

            # At the end it will check if you have reached the maximum number of attempts.
            else:
                new_player.add_points("wrong_points") if new_player.tries == 6 else new_player.add_points("correct_points")
                print(f"\n\n-Words you got right: {new_player.correct_points}\n-Words you didn't get right: {new_player.wrong_points}")
                print("The correct word was: ", word) if new_player.tries == 6 else print(f"You got the word right! {new_player.name}")
                play_again = input(f"Type 'back' to change category\nPress enter or type anything else to continue playing with the {current_category} category: ").lower()
                start_game = False if play_again == "back" else True

        # This else is in charge of creating the category selection menu.
        else:

            try:
                print("\nSelect one category below:")
                for i, c in enumerate(categories):
                    print(i+1, c.capitalize())
                selection = input("Type a number or a name to select: ").strip()

                # Select by name or by number.
                if selection.lower() in categories_list:
                    start_game = True
                    current_category = selection.lower()

                elif selection.isdigit():
                    selection = int(selection)
                    if selection-1 < len(categories_list) and selection-1 != -1:
                        start_game = True
                        current_category = categories_list[selection-1]

                    else:
                        print(f"\n'{selection}' is not included, try again")
                else:
                    print(f"\n'{selection}' is not an included category, try again") if selection != "" else print("\nNo category found")

            except KeyboardInterrupt:
                print("\nKeyboard interruption detected, try again.")


def select_a_word(category):
    """
    Selects and returns a random word based on the category passed to it.
    """

    number_of_words = len(categories[category])-1
    return categories[category][random.randint(0, number_of_words)]


def display_underscores(word, letters_list):
    """
    Shows underscores to indicate the number of letters in the word,
    shows the letters found in the word if they are matched.
    """
    current_word = ""
    for letter in word:
        if letter in letters_list:
            current_word = current_word + letter
            print(letter.upper(), end=" ")
        else:
            current_word = current_word + "-"
            print("_", end=" ")
    return current_word


def display_hangman(num):
    """
    Use a number between 1 and 6 to create the parts of the hangman.
    """

    parts = ["O", "|", "/", "\\", "/", "\\"]
    hangman = {
        "head": "",
        "body": "",
        "left_arm": "",
        "right_arm": "",
        "left_leg": "",
        "right_leg": ""
    }
    hangman_list = [x for x in hangman]

    for x in range(num):
        hangman[hangman_list[x]] = parts[x]

        if x == 1:
            hangman["body"] = " |"
        elif x == 2:
            hangman["body"] = "|"

    print(f"  ------\n  |   |\n  |   {hangman["head"]}\n  |  {hangman["left_arm"]}{hangman["body"]}{hangman["right_arm"]}\n  |  {hangman["left_leg"]} {hangman["right_leg"]}\n__|__", end="    ")


main()
