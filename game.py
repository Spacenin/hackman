import pygame

def gameTime(word):
    #Setup game logic
    incorrectLetters = []
    correctLetters = []
    status = 0

    for i in range(len(word)):
        correctLetters.append(0)

    #pygame stuffs
    pygame.init()

    screen = pygame.display.set_mode((800, 500))
    pygame.display.set_caption("Hackman")

    #Set up font, images, GUI stuff
    font = pygame.font.Font("freesansbold.ttf", 20)
    baseImage = pygame.image.load("assets/base.png")
    oneImage = pygame.image.load("assets/one.png")
    twoImage = pygame.image.load("assets/two.png")
    threeImage = pygame.image.load("assets/three.png")
    fourImage = pygame.image.load("assets/four.png")
    fiveImage = pygame.image.load("assets/five.png")
    deathImage = pygame.image.load("assets/death.png")

    text = font.render("Correctly guessed letters:", True, (255,255,255))    

    while True:
        if status == 0:
            screen.blit(baseImage, (-225, -125))
        elif status == 1:
            screen.blit(oneImage, (-225, -125))

        screen.blit(text, (75, 325))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

                return
            
            
        pygame.display.update()
