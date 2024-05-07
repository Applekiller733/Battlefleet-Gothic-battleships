import pygame
import pygame_gui
#todo: testing around with different types of menus so far.
# create a nice title screen in aseprite
# add buttons to menu (new game, story, exit)

pygame.init()

display_width = 1900


display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Battlefleet Gothic')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False


mainimg = pygame.image.load('battlefleetgothicmain.png')
logoimg = pygame.image.load('batlefleetgothiclogo.png')


def main(x, y):
    gameDisplay.blit(mainimg, (x, y))

def logo(x, y):
    gameDisplay.blit(logoimg, (x, y))

mainx = (0)
mainy = (-300)

logox = (30)
logoy = (80)

# light shade of the button
button_color_light = (170, 170, 170)

# dark shade of the button
button_color_dark = (100, 100, 100)

text_color = (255, 255, 255)

fonttest = pygame.font.SysFont('parchment', 40)

testtext = fonttest.render('test', True, text_color)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if display_width / 2 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_height / 2 + 40:
                print("cox tony montana gios")

    mouse = pygame.mouse.get_pos()

    gameDisplay.fill(white)
    main(mainx, mainy)
    logo(logox, logoy)

    if display_width / 2 <= mouse[0] <= display_width / 2 + 140 and display_height / 2 <= mouse[1] <= display_height / 2 + 40:
        pygame.draw.rect(gameDisplay, button_color_light, [display_width / 2, display_height / 2, 140, 40])

    else:
        pygame.draw.rect(gameDisplay, button_color_dark, [display_width / 2, display_height / 2, 140, 40])

        # superimposing the text onto our button
    gameDisplay.blit(testtext, (display_width / 2 + 50, display_height / 2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

