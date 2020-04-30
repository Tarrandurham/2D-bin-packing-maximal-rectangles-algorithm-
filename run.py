import sys
import time
import pygame
import cv2
import pickle
import numpy as np
import matplotlib.pyplot as plt
white = 255, 255, 255

containers = [[0, 0, 300, 300]]
firstcontainer = containers[0]

show = True
rrectangles = [[0, 0, 40, 30], [0, 0, 60, 80]
               ]  # [0, 0, 210, 80], [0, 0, 45, 45], [
# 0, 0, 50, 50], [0, 0, 25, 50]


def action(containers, rrectangles):

    # pick rectangle
    for rectangle in rrectangles:
        print("Rectangle " + str(rectangle) +
              " needs to be placed in " + str(containers))
        # pick container to place rectangle in
        shortlistx = []
        shortlisty = []
        for container in containers:

            shortlistx.append(
                container[2]-rectangle[0])

            shortlisty.append(
                container[3]-rectangle[1])
            """print("This is the shortlist: " + str(shortlistx))
            print("This is the shortlisty: " + str(shortlisty))"""
        # iterate through axes of shortlist to find minimum side
        chosencontainerx = min(shortlistx)
        indexx = shortlistx.index(chosencontainerx)
        chosencontainery = min(shortlisty)
        indexy = shortlisty.index(chosencontainery)
        """print("This is the chosencontainerx " +
              str(chosencontainerx) + " and its index " + str(indexx))
        print("This is the chosencontainery " +
              str(chosencontainery) + " and its index " + str(indexy))"""
        # placing the rectangle in minimum short side
        # print(containers[indexy])
        if chosencontainerx >= chosencontainery and containers[indexy][0] + containers[indexy][2] <= firstcontainer[2] and containers[indexy][1]+containers[indexy][3] <= firstcontainer[3] and rectangle[2]+containers[indexy][0] < firstcontainer[2] and rectangle[3]+containers[indexy][1] < firstcontainer[3]:
            print("I take path a: /n")
            rectangle[1] = containers[indexy][1]
            rectangle[0] = containers[indexy][0]
            if rectangle[1] > 0:
                containers[indexx][3] = rectangle[1]
                print("I split container into a new container ")
                print(containers)
            removedcontainer = containers.pop(indexy)
            print(" I placed " + str(rectangle) +
                  " in " + str(removedcontainer))
            removedcontainer[2] = removedcontainer[2] - rectangle[0]
            containers.append(removedcontainer)
            containers.append([rectangle[0], rectangle[3]+rectangle[1],
                               removedcontainer[2], removedcontainer[3]-rectangle[3]])
            containers.append([rectangle[0]+rectangle[2],
                               rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]])
            print(" I added these two containers to the possible list: " +
                  str(containers[-1]) + " and " + str(containers[-2]))

            print("entire container list: " + str(containers))
        elif chosencontainerx < chosencontainery and containers[indexx][0] + containers[indexx][2] <= firstcontainer[2] and containers[indexx][1]+containers[indexx][3] <= firstcontainer[3] and rectangle[2]+containers[indexx][0] < firstcontainer[2] and rectangle[3]+containers[indexx][1] < firstcontainer[3]:
            print("I take path b: ")
            rectangle[1] = containers[indexx][1]
            rectangle[0] = containers[indexx][0]
            if rectangle[0] > 0:
                containers[indexy][2] = rectangle[0]

                print("I split container into a new container ")
                print(containers)
            removedcontainer = containers.pop(indexx)
            print(" I placed " + str(rectangle) +
                  " in " + str(removedcontainer))
            removedcontainer[3] = removedcontainer[3] - rectangle[1]
            containers.append(removedcontainer)
            containers.append([rectangle[0], rectangle[3]+rectangle[1],
                               removedcontainer[2], removedcontainer[3]-rectangle[3]])
            containers.append([rectangle[0]+rectangle[2],
                               rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]])
            print(" I added these two containers to the possible list: " +
                  str(containers[-1]) + " and " + str(containers[-2]))
        else:
            print("doesnt fit bad container")
            continue
            """if chosencontainerx >= chosencontainery:
                container.pop(indexy)
            elif chosencontainerx < chosencontainery:
                container.pop(indexx)"""
        print("all currently available containers: " + str(containers))
        for container in containers:
            if pygame.Rect(rectangle).collidelist(containers) != -1:
                print("colliding")
            if pygame.Rect(
                    rectangle).collidelist(containers) != -1:
                print("removed container " + str(container) +
                      " thats touching rectangle " + str(rectangle))
                containers.remove(container)

            elif container[0] > firstcontainer[2] or container[1] > firstcontainer[3]:
                print("removed container thats larger than the border " + str(rectangle))
                containers.remove(container)
            else:
                print("none removed")
        print(containers)


action(containers, rrectangles)

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
                                       200 / (i+1)), pygame.Rect(rrectangles[i]))

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

    screen.blit(font.render(str(
        0) + " " + str(rrectangles[0]), True, (0, 0, 0)), (rrectangles[0][0], rrectangles[0][1]))
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
