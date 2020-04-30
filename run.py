import sys
import time
import pygame
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
white = 255, 255, 255
containers = [[0, 0, 200, 200]]
show = True
rrectangles = [[40, 30], [45, 45], [50, 50], [25, 50]]


def action(containers, rrectangles):

    # pick rectangle
    for rectangle in rrectangles:
        print("rectangle " + str(rectangle) +
              " needs to be placed in " + str(containers))
        # pick container to place rectangle in
        shortlistx = []
        shortlisty = []
        for container in containers:

            shortlistx.append(
                container[2]-rectangle[0])

            shortlisty.append(
                container[3]-rectangle[1])

        # iterate through axes of shortlist to find minimum side
        chosencontainerx = min(shortlistx)
        indexx = shortlistx.index(chosencontainerx)
        chosencontainery = min(shortlisty)
        indexy = shortlisty.index(chosencontainery)

        # placing the rectangle in minimum short side
        if chosencontainerx >= chosencontainery:

            rectangle.insert(0, containers[indexy][1])
            rectangle.insert(0, containers[indexy][0])

            removedcontainer = containers.pop(indexy)
            print(" I placed " + str(rectangle) +
                  " in " + str(removedcontainer))
            containers.append([rectangle[0], rectangle[3]+rectangle[1],
                               removedcontainer[2]-rectangle[0], removedcontainer[3]-rectangle[3]])
            containers.append([rectangle[0]+rectangle[2],
                               rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]-rectangle[1]])
            print(" I added these two containers to the possible list: " +
                  str(containers[-1]) + " and " + str(containers[-2]))

            #print("entire container list: " + str(containers))
        else:

            rectangle.insert(0, containers[indexx][1])
            rectangle.insert(0, containers[indexx][0])
            removedcontainer = containers.pop(indexx)
            print(" I placed " + str(rectangle) +
                  " in " + str(removedcontainer))
            containers.append([rectangle[0], rectangle[3]+rectangle[1],
                               removedcontainer[2]-rectangle[0], removedcontainer[3]-rectangle[3]])
            containers.append([rectangle[0]+rectangle[2],
                               rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]-rectangle[1]])
            print(" I added these two containers to the possible list: " +
                  str(containers[-1]) + " and " + str(containers[-2]))

        print("all currently available containers: " + str(containers))
        for container in containers:

            if pygame.Rect(
                    rectangle).collidelist(containers) != -1:
                containers.remove(container)
                print("removed")
            else:
                print("none removed")
        """print(containers)
        print(rectangle)"""


action(containers, rrectangles)

while show:
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))

    screen.fill(white)
    surface = pygame.Surface((400, 400))
    surface.fill(white)
    pygame.draw.rect(surface, (230, 230, 240), pygame.Rect([0, 0, 200, 200]))
    try:
        for i in range(len(rrectangles)):
            pygame.draw.rect(surface, (240 / (i+1), 240 / (i+2),
                                       200 / (i+1)), pygame.Rect(rrectangles[i]))
    except:
        pass
    try:
        for j in range(len(containers)):
            pygame.draw.rect(surface, (150 / (j+1), 100 / (j+2),
                                       10 / (j+3)), pygame.Rect(containers[j]))
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
