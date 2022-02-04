import pygame

class Game:
    #Set up initial conditions
    guyStatus = 0
    guessedLetters = []
    wrongLetters = []

    def __init__(self, word):
        #Begin gameplay loop
        self.running = True
        self.word = word

        #Set up pygame stuff
        pygame.init()
        self.screen = screenSetup()

        print(word)

        for i in range(len(word)):
            self.guessedLetters.append(0)

        self.draw()

    #Checks if the game should quit
    def checkRunning(self):
        letterCount = 0

        #Check if the user has filled up the right word
        for i in self.guessedLetters:
            if i == 0:
                pass
            else:
                letterCount += 1

        if letterCount == len(self.word):
            print("You got it all right! Your word was:", self.word)

            return(False)
        
        #Check if user has guessed max letters
        elif self.guyStatus >= 6:
            print("You have reached the maximum incorrect guesses!")

            return(False)

        else:
            return(True)
        

    #Draw the screen with letters guessed
    def draw(self):
        while self.running:
            print("---|---")

            if self.guyStatus == 0:
                print("No misses yet!")

            elif self.guyStatus == 1:
                print("   0   ")

            elif self.guyStatus == 2:
                print("   0   ")
                print("\__|   ")

            elif self.guyStatus == 3:
                print("   0   ")
                print("\__|__/")
            
            elif self.guyStatus == 4:
                print("   0   ")
                print("\__|__/") 
                print(" __|   ")
                print("/")
            
            elif self.guyStatus == 5:
                print("   0   ")
                print("\__|__/") 
                print(" __|__ ")
                print("/     \\")

                print("---YOU HAVE ONE GUESS LEFT---")
            
            print("So far you have guessed:", self.guessedLetters)
            print("...and gotten wrong:", self.wrongLetters)

            guessedLetter = getLetter()

            #Check if the guessed letter is in the word, if so then add it to correct letters
            if guessedLetter in self.word:
                for i in range(len(self.word)):
                    if self.word[i] == guessedLetter:
                        self.guessedLetters[i] = guessedLetter

                print("You guessed correctly!")
            
            #...if not, then add it to missed letters
            else:
                self.guyStatus += 1
                self.wrongLetters.append(guessedLetter)

                print("You guessed incorrectly!")

            print("\n")

            #Check if the game should continue
            self.running = self.checkRunning() 

#Get letter from user
def getLetter():
    looper = True

    print("Enter your letter: ", end='')

    #Keep prompting until getting a letter
    while looper:
        guessed = str(input())

        if guessed.isalpha():
            looper = False

            return(guessed)

        else:
            print("That is not a letter! Please try again: ", end='')

#Set up pygame display screen
def screenSetup():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hackman")

    return(screen)
