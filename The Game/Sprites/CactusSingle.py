import pygame
class CactusSingle(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 17, 30)
        self.imageName = "Sprites/GameImages/smallCactus.png"

    def drawCharacter(self, canvas):
        canvas.blit(pygame.image.load(self.imageName), (self.x,self.y))
        self.hitbox = (self.x, self.y, 17, 30)
        pygame.draw.rect(canvas, (0, 255, 0), self.hitbox,2)

    def propagate(self, step):
        self.x -= step
