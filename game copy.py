import random
import time

class Game:
    def __init__(self):
        self.level = Level()
      
        
# asks level and calls its level method from Level class
    def game_start(self):
        name = input("What is your name? ")
        print ("Hello, " + name, "Choose Game level: 1, 2, 3")
        level = input(":")
        print ("")
        if level == "1":
            x = game.level.easy_level() 
            return x
           
        if level == "2":
            x = game.level.normal_level()
            return x
            
        if level == "3":
           x = game.level.hard_level()
           return x
        else:
            return "Wrong Input"

    def play_game(self):     
        print ("Start guessing...")

        time.sleep(0.5)

        #gets word from chosen level
        
        word = self.game_start()
        word_length = len(word)

        #empty variable to store guesses
        guesses = ''

        #number of guesses
        allowed_guesses = 8

    
        while allowed_guesses > 0:       
            failed = 0  
        #checks if char in guesses
            for char in word:      
                if char in guesses:    
                    print (char)
                else:
                    print ("_")   
                    failed += 1    
            
            if failed == 0:       
                print ("You won" ) 
                break              

        
            #user char input word length
            print("Word length is", word_length)
            guess = input("guess a character:") 
            #store input value
            guesses += guess.upper()   
                             
            #checks if char not in guesses
            if guess not in word:  
                allowed_guesses -= 1        
                print ("Wrong")  
                print ("You have", + allowed_guesses, 'more guesses') 
        
                if allowed_guesses == 0:           
                    print("Word is", word) 
                    print( "You Lose")  


               
   
# class with all gam levels
class Level:
    def __init__(self):
        self.easy = []
        self.normal = []
        self.hard = []

# get data from file
    def open_file(self):
        with open('words.txt', 'r') as file:
            data = file.read().lower()
            words = [word for word in data.split()]
            return words
    
# if level 1 call this method (list of easy words)   
    def easy_level(self):
        words = self.open_file()
             
        for word in words:
            if len(word) >= 4 and len(word) < 6:
                self.easy.append(word)
                value = random.choice(self.easy)
                return value.upper()

# if level 2 call this method (list of normal words)  
    def normal_level(self):
        words = self.open_file()
        for word in words:
            if len(word) > 6 and len(word) < 8:
                self.normal.append(word)
                value = random.choice(self.normal)
                return value.upper()

# if level 3 call this method  (list of hard words)                
    def hard_level(self):
        words = self.open_file()
        for word in words:
            if len(word) > 8:
                self.hard.append(word)
                value = random.choice(self.hard)
                return value.upper()



game = Game()
game.play_game()
