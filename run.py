import random
import os

categories = {"animals" : ["dog", "cat", "lion", "chicken", "frog"],
              "technology" : ["robot", "computer", "printer", "camera"],
              "sports" : ["cycling", "soccer", "baseball", "tennis", "boxing"]}


class Player:
    """
    Create an instance of the player class
    """
    def __init__(self, name):
        self.name = name
        self.tries = 0 #Attribute specific to each instance
        self.correct_points = 0
        self.wrong_points = 0 
        self.wrong_letters = []
        self.wrong_words = []


    def add_points(self, name_counter):
        if name_counter == "tries":
            self.tries+=1
        elif name_counter == "correct_points":
            self.correct_points+=1
        else:
            self.wrong_points+=1

    def add_to_list(self, name_list, letter):
        if name_list == "wrong_letters":
            self.wrong_letters.append(letter)
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
        if main_menu:
            player_name = input("\nWhat is your name? ")
            new_player = Player(player_name)
            main_menu = False

        elif start_game:
            print(f"\nYou are playing with the {current_category} category\nType 'back' to choose another category\n-Words you got right: {new_player.correct_points}\n-Words you didn't get right: {new_player.wrong_points}\n")
            letters = []
            new_player.wrong_letters = []
            new_player.wrong_words = []
            display_hangman(0)
            word = select_a_word(current_category)
            player_word = display_underscores(word,letters)
            new_player.tries = 0
            while new_player.tries != 6 and player_word != word:
                letter_or_word = input("\n\nGuess a letter or a word: ").lower()

                if letter_or_word == "back":
                    start_game = False
                    break
                
                elif letter_or_word != "" and letter_or_word.upper() not in new_player.wrong_letters and letter_or_word.upper() not in new_player.wrong_words:
                    if letter_or_word == word:
                        letters = [letter for letter in word]
                        display_hangman(new_player.tries)
                        player_word = display_underscores(word, letters)

                    elif letter_or_word in word:
                        print(f"Used letters: {new_player.wrong_letters}")
                        print(f"Used words: {new_player.wrong_words}")
                        display_hangman(new_player.tries)
                        letters.append(letter_or_word) 
                        player_word = display_underscores(word, letters)
    
                    else:
                        new_player.add_to_list("wrong_letters", letter_or_word.upper()) if len(letter_or_word) == 1 else new_player.add_to_list("wrong_words", letter_or_word.upper())
                        print(f"Used letters: {new_player.wrong_letters}")
                        print(f"Used words: {new_player.wrong_words}")
                        new_player.add_points("tries")
                        display_hangman(new_player.tries)
                        display_underscores(word, letters)

                else:
                    print(f"\n\nUsed letters: {new_player.wrong_letters}")
                    print(f"Used words: {new_player.wrong_words}")
                    print(f"You've already used: {letter_or_word.upper()}") if letter_or_word != "" else print("No letter or word found")
                    display_hangman(new_player.tries)
                    display_underscores(word, letters)

            else:
                new_player.add_points("wrong_points") if new_player.tries == 6 else new_player.add_points("correct_points")
                print(f"\n\n-Words you got right: {new_player.correct_points}\n-Words you didn't get right: {new_player.wrong_points}")
                print("The correct word was: ", word) if new_player.tries == 6 else print(f"You got the word right! {new_player.name}")
                play_again = input(f"Type 'back' to change category\nPress enter or type anything else to continue playing with the {current_category} category: ").lower()
                start_game = False if play_again == "back" else True

        else:
            
            print("\nSelect one category below:")
            for i, c in enumerate(categories):
                print(i+1,c.capitalize())
            selection = input("Type a number or a name to select: ")

            if selection.lower() in categories_list:
                print(f"{selection} is correct")
                start_game = True
                current_category = selection.lower()
            elif selection.isdigit():
                selection = int(selection)
                if selection-1 < len(categories_list) and selection-1 != -1:
                    print(categories_list[selection-1])
                    start_game = True
                    current_category = categories_list[selection-1]
                else:
                    print(f"\n{selection} is not included, try again")
            else:
                print(f"\n{selection} is not an included category, try again")



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
    parts = ["O","|","/","\\","/","\\"]
    hangman = {
        "head" : "",
        "body" : "",
        "left_arm" : "",
        "right_arm" : "",
        "left_leg" : "",
        "right_leg" : ""
    } 
    hangman_list = [x for x in hangman]

    for x in range(num):
        hangman[hangman_list[x]] = parts[x]

        if x == 1:
            hangman["body"] = " |"
        elif x == 2:
            hangman["body"] = "|"
            
    print(f"  ------\n  |   |\n  |   {hangman["head"]}\n  |  {hangman["left_arm"]}{hangman["body"]}{hangman["right_arm"]}\n  |  {hangman["left_leg"]} {hangman["right_leg"]}\n__|__", end="    ") 


                
#word = display_underscores("chicken", ["c","c","h","n","e","e","i","k"])
#print(word)

#display_hangman(6)

main()
