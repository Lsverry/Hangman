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
    categories_list = [x for x in categories.keys()]
    main_menu = True
    selection = ""
    start_game = False
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
            elif selection.isdigit():
                selection = int(selection)
                if selection-1 < len(categories_list) and selection-1 != -1:
                    print(categories_list[selection-1])
                    start_game = True
                else:
                    print(f"\n{selection} is not included, try again")
            else:
                print(f"\n{selection} is not an included category, try again")

    


main()