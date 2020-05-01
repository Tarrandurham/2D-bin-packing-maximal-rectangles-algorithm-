import sys
import time
import pygame
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
white = 255, 255, 255


rectangle = [40, 0, 60, 80]
containers = [[40, 0, 260, 300]]
if pygame.Rect(rectangle).collidelist(containers) != -1:
    print("colliding")
    print(pygame.Rect(rectangle).collidelist(containers))
rrectangles = rectangle
show = True
while show:
    pygame.init()
    font = pygame.font.SysFont('Arial', 25)
    screen = pygame.display.set_mode((1000, 1000))
    text = []
    screen.fill(white)
    surface = pygame.Surface((400, 400))
    surface.fill(white)
    pygame.draw.rect(surface, (0, 0, 0),
                     pygame.Rect([0, 0, 300, 300]), 4)
    try:
        for i in range(len(rrectangles)):
            pygame.draw.rect(surface, (240 / (i+1), 240 / (i+2),
                                       200 / (i+1)), pygame.Rect(rrectangles))

    except:
        pass
    try:
        for j in range(len(containers)):
            pygame.draw.rect(surface, (150 / (j+1), 100 / (j+2),
                                       10 / (j+3)), pygame.Rect(containers[j]), 2)
    except:
        pass

    screensurface = pygame.Surface((1000, 1000))

    pygame.transform.scale(
        surface,
        # surface to be scaled
        (1000, 1000),  # scale up to (width, height)

        screensurface)  # surface that game_surface will be scaled onto
    screen.blit(screensurface, (0, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            show = False
            pygame.display.quit()
            pygame.quit()

    if cv2.waitKey(2000) & 0xFF == ord('q'):
        pygame.display.update()
        pygame.display.quit()
        pygame.quit()
        sys.exit(0)
