

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