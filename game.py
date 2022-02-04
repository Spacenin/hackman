class Game:
    running = False
    guyStatus = 0
    guessedLetters = []
    wrongLetters = []

    def __init__(self, word):
        self.running = True
        self.word = word

        print(word)

        for i in range(len(word)):
            self.guessedLetters.append(0)

        self.checkRunning()

    def checkRunning(self):
        letterCount = 0

        for i in self.guessedLetters:
            if i == 0:
                pass
            else:
                letterCount += 1

        if letterCount == len(self.word):
            print("You got it all right! Your word was:", self.word)

            return
        
        if self.guyStatus >= 6:
            self.running = False

        if self.running == False:
            print("GAME OVER")
            print("Your word was:", self.word)

            return
        
        else:
            self.draw()


    def draw(self):
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

        if guessedLetter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guessedLetter:
                    self.guessedLetters[i] = guessedLetter

            print("You guessed correctly!")
            
        else:
            self.guyStatus += 1
            self.wrongLetters.append(guessedLetter)

            print("You guessed incorrectly!")

        print("\n")

        self.checkRunning() 


def getLetter():
    looper = True

    print("Enter your letter: ", end='')

    while looper:
        guessed = str(input())

        if guessed.isalpha():
            looper = False

            return(guessed)

        else:
            print("That is not a letter! Please try again: ", end='')
        




        


