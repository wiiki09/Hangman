import time

class Hangman:

    
    def __init__(self):
        self.possible_words=['becode', 'learning', 'mathematics', 'sessions']
        self.life = 5
        self.well_guessed_letters = []
        self.bad_guessed_letters = set()
        self.turn_count = 0
        self.error_count = 0
        self.good_answers = set()
        #Initialize the ramdom word --> self.good_word
        self.random_word()
        #Calulate the index of each letter 
        self.word_index_initialize()
    


    def play(self):
        """
        Function who ask the player to type a letter and verify if the input is one
        """
        letter = input("Type a letter :")
        #Loop if the input is not alphabetical and if it's more than one character
        while not letter.isalpha() or len(letter) != 1 :
            print("This is not ONE LETTER")
            letter = input("Type a letter please :\n")
        #Check if the letter is on word and if we have not already propose this letter
        if letter in self.letter_map.keys() and not letter in self.good_answers :
            self.good_answers.add(letter)
            self.put_good_letter(letter)
        else :
            self.bad_guessed_letters.add(letter)
            self.error_count += 1
            self.life -= 1
    

    def put_good_letter(self, letter:str):
        """
        Function that put the letter on the goods positions of the research word

        Args:
            letter (str): the letter to be place
        """
        index_list = self.letter_map[letter]
        for index in index_list:
            self.well_guessed_letters[index] = letter

    def start_game(self):
        """
        Function that launch the game and break it the user win or lose the game.
        The loops is limited to 26 occurences like alphabet
        """
        print("\nWelcome to the Hangman game ! \n")
        print("The secret word is :", " ".join(self.well_guessed_letters), "\n")
        for i in range(25) :
            self.play()
            self.turn_count = i+1
            if self.life < 1 :
                self.game_over()
                break
            #Check if the player have found all the different letter of the search word
            if len(self.good_answers) == len(self.letter_map) :
                self.well_played()
                break
            print("\nSecret word : ", " ".join(self.well_guessed_letters), "\n")
            print("Bad guessed letter : ", self.bad_guessed_letters)
            print("Life : ", self.life)
            print("Turn : ", self.turn_count, "\n")
        
    
    def game_over(self):
        print("\nSorry it's game over...")

    def well_played(self): 
        print(f"\n You found the word: {''.join(self.good_word)} in {self.turn_count} turns with {self.error_count} errors!")


    def random_word(self) :
        """
        This function select a word in a list of word
        """
        #Use time in second and perform a modulo with the number of word
        #in the list to find a random index
        random_index = int(time.time()) % len(self.possible_words)
        self.good_word = list(self.possible_words[random_index])
        self.well_guessed_letters = list("_" * len(self.good_word))

    def word_index_initialize(self):
        """
        Function that check all letters of the word and save theyr position in the word
        """
        letter_map = {}
        for index, letter in enumerate(self.good_word) :
            if not letter in letter_map.keys() :
                letter_map[letter] = [index]
            else :
                letter_map[letter].append(index)
        self.letter_map = letter_map
        self.diferent_letter = {}   