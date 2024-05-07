import pygame

class Button:
    def __init__(self, xpos1, ypos1, sizex, sizey, text):
        self.__xpos1 = xpos1
        self.__ypos1 = ypos1
        self.__sizex = sizex
        self.__sizey = sizey
        self.__text = text

    @property
    def xpos1(self):
        return self.__xpos1
    @property
    def ypos1(self):
        return self.__ypos1

    @property
    def sizex(self):
        return self.__sizex

    @property
    def sizey(self):
        return self.__sizey

    @property
    def text(self):
        return self.__text

    def mouseover(self, x, y):
        if (self.xpos1 <= x <= self.xpos1+self.sizex) and (self.ypos1 <= y <= self.ypos1+self.sizey):
            return True
        return False


