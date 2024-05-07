import pygame
import pygame_gui
import moviepy.editor as mpy

from GUI_Domain.Button import Button
#todo:
# create a nice title screen in aseprite
# work on main gameplay loop, add in roguelike elements
# add some replayability
pygame.init()
pygame.mixer.init()
class GUI:
    def __init__(self):
        self.display_width = 1900
        self.display_height = 1000

        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Battlefleet Gothic')

        self.black = (0,0,0)
        self.white = (255,255,255)

        self.clock = pygame.time.Clock()
        self.mainimg = pygame.image.load('battlefleetgothicmain.png')
        self.logoimg = pygame.image.load('batlefleetgothiclogo.png')
        self.buttonslist = []
        self.main_menu()


    def main(self, x, y):
        self.gameDisplay.blit(self.mainimg, (x, y))

    def logo(self, x, y):
        self.gameDisplay.blit(self.logoimg, (x, y))

    def add_button(self, button):
        self.buttonslist.append(button)
    def buttons_update(self, mouse):
        # light shade of the button
        button_color_light = (150, 50, 80)

        # dark shade of the button
        button_color_dark = (100, 20, 40)
        font = pygame.font.SysFont('parchment', 50)
        for button in self.buttonslist:
            if button.mouseover(mouse[0], mouse[1]):
                pygame.draw.rect(self.gameDisplay, button_color_light,[button.xpos1, button.ypos1, button.sizex, button.sizey])
            else:
                pygame.draw.rect(self.gameDisplay, button_color_dark,[button.xpos1, button.ypos1, button.sizex, button.sizey])
            buttontext = font.render(button.text,True, (255, 255, 160))
            self.gameDisplay.blit(buttontext, (button.xpos1 + button.sizex / 5, button.ypos1 - button.sizey / 4))

    def main_menu(self):
        mainx = (0)
        mainy = (-300)

        logox = (30)
        logoy = (80)
        # light shade of the button
        button_color_light = (150, 50, 80)

        # dark shade of the button
        button_color_dark = (100, 20, 40)
        new_game_button = Button(100, 300, 320, 40, "New    Game")
        self.add_button(new_game_button)
        story_button = Button(100, 360, 320, 40, "Story")
        self.add_button(story_button)
        exit_button = Button(1600, 900, 150, 40, "Quit")
        self.add_button(exit_button)
        text_color = (255, 200, 200)
        crashed = False
        while not crashed:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.load("maintheme.mp3")
                pygame.mixer.music.set_volume(0.8)
                pygame.mixer.music.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_button.mouseover(mouse[0], mouse[1]):
                        print("cox tony montana gios")
                        #todo: add game
                    if story_button.mouseover(mouse[0], mouse[1]):
                        pygame.mixer.music.stop()
                        pygame.mouse.set_visible(False)
                        video = mpy.VideoFileClip("Intro.mp4")
                        video.preview()
                        pygame.mouse.set_visible(True)
                    if exit_button.mouseover(mouse[0], mouse[1]):
                        pygame.quit()


            mouse = pygame.mouse.get_pos()

            self.gameDisplay.fill(self.white)
            self.main(mainx, mainy)
            self.logo(logox, logoy)

            self.buttons_update(mouse)
            pygame.display.update()
            self.clock.tick(60)
g = GUI()
pygame.quit()
quit()

