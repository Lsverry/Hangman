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
        self.wrong_words = []
        self.correct_words = []


    def add_points(self, name_counter):
        if name_counter == "tries":
            self.tries+=1
        elif name_counter == "correct_points":
            self.correct_points+=1
        else:
            self.wrong_points+=1

    def add_word(self, name_list, word):
        if name_list == "wrong_words":
            self.wrong_words.append(word)
        else:
            self.correct_words.append(word)


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
            player_name = input("What is your name? ")
            new_player = Player(player_name)
            main_menu = False
        elif start_game:
            print("\nGuess a letter or a word\nYou only have 6 tries")
            input()


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
    print(categories[category][random.randint(0, number_of_words)])


def display_underscores(word, letters_list):
    """
    Shows underscores to indicate the number of letters in the word,
    shows the letters found in the word if they are matched.
    """
    for letter in word:
        if letter in letters_list:
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")

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
            
    print(f"  ------\n  |   |\n  |   {hangman["head"]}\n  |  {hangman["left_arm"]}{hangman["body"]}{hangman["right_arm"]}\n  |  {hangman["left_leg"]} {hangman["right_leg"]}\n__|__") 


                
#display_underscores("tiger", ["t","r","g"])

#display_hangman(1)

#main()
