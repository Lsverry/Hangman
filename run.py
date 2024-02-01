import random

categories = {"animals" : ["dog", "cat", "lion", "chicken", "frog"],
              "technology" : ["robot", "computer", "printer", "camera"],
              "sports" : ["cycling", "soccer", "baseball", "tennis", "boxing"]}


class player():
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
    while True:
        if main_menu:
            print("\nSelect one option below:\n")
            print("1.New Game")
            print("2.Load Game")
            selection = input("\nType 1 or 2: ")

            if selection == "1" or selection.lower() == "new game":
                print("\nCreate new game")
                main_menu = False
                
            elif selection == "2" or selection.lower() == "load game":
                print("\nLoading game")
                main_menu = False

            else:
                print(f"\n{selection} is not a valid option.")
                continue
        
        elif start_game:
            input("Starting game :")

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
    Returns the same number as the number passed to it.
    """
    parts = ["O","|","/","\\","/","\\"]
    if num <= 2:
        for part in range(num):
            print("    " + parts[part])
    else:

        print("    " + parts[0])
        print("   " + parts[2], end = "")
        print(parts[1], end="")
        
        if num > 3:
            print(parts[3])
            if num > 4:
                print("   ", end="")
                for part in range(4,num):
                    print(parts[part], end = " ")
    return num


                
#display_underscores("tiger", ["t","r","g"])

#main()