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
rrectangles = [[0, 0, 50, 50], [0, 0, 200, 200], [0, 0, 30, 40], [0, 0, 70, 70], [0, 0, 30, 30], [0, 0, 10, 40], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 30, 30], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 30, 30], [0, 0, 60, 30], [0, 0, 30, 30], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 50, 30], [0, 0, 60, 30], [0, 0, 60, 40], [0, 0, 60, 30], [0, 0, 4, 50], [0, 0, 26, 41], [0, 0, 40, 14]
               ]

""", [0, 0, 20, 20], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 100, 100], [0, 0, 40, 30], [0, 0, 60, 80], [
    0, 0, 20, 20], [0, 0, 20, 20], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 100, 100], [0, 0, 40, 30], [0, 0, 60, 80], [
    0, 0, 20, 20], [0, 0, 20, 20], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 100, 100], [0, 0, 40, 30], [0, 0, 60, 80], [
    0, 0, 20, 20], [0, 0, 20, 20], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 30, 30], [0, 0, 40, 50], [0, 0, 100, 100], [0, 0, 40, 30], [0, 0, 60, 80], [0, 0, 20, 20], [0, 0, 30, 30], [0, 0, 40, 50]"""
placedrectangles = []


def action(containers, rrectangles):

    # pick rectangle
    for rectangle in list(rrectangles):

        print("Rectangle " + str(rectangle) +
              " needs to be placed in " + str(containers))
        # pick container to place rectangle in
        shortlistx = []
        shortlisty = []
        for container in containers:

            shortlistx.append(abs(container[2]-rectangle[2]))

            shortlisty.append(
                abs(container[3]-rectangle[3]))
            """print("This is the shortlist: " + str(shortlistx))
            print("This is the shortlisty: " + str(shortlisty))"""
        # iterate through axes of shortlist to find minimum side

        l = 0
        p = True
        """print("This is the chosencontainerx " +
              str(chosencontainerx) + " and its index " + str(indexx))
        print("This is the chosencontainery " +
              str(chosencontainery) + " and its index " + str(indexy))"""
        # placing the rectangle in minimum short side
        # print(containers[indexy])
        while p == True:

            if l > len(containers):
                print("i cant find a solution")
                rrectangles.remove(rectangle)
                p = False
                break
            print("x")
            print(sorted(shortlistx))
            chosencontainerx = sorted(shortlistx)[l]

            print("y")
            print(sorted(shortlisty))
            indexx = shortlistx.index(chosencontainerx)
            chosencontainery = sorted(shortlisty)[l]
            indexy = shortlisty.index(chosencontainery)

            if chosencontainerx >= chosencontainery and containers[indexy][0] + containers[indexy][2] <= firstcontainer[2] and containers[indexy][1]+containers[indexy][3] <= firstcontainer[3] and rectangle[2]+containers[indexy][0] <= firstcontainer[2] and rectangle[3]+containers[indexy][1] <= firstcontainer[3] and rectangle[3] <= containers[indexy][3]:
                print("I take path links unten: ")
                rectangle[1] = containers[indexy][1]
                rectangle[0] = containers[indexy][0]
                # and rectangle[1]+rectangle[3] > container[1]

                if rectangle[1] > 0 and rectangle[1] + containers[indexx][1] <= firstcontainer[3] and rectangle[0] + rectangle[2] > containers[indexy][1]:
                    containers[indexx][3] = rectangle[1]
                    print("I split container into a new container " +
                          str(containers))
                removedcontainer = containers[indexy]
                # removedcontainer = containers.pop(indexy)
                print(" I placed " + str(rectangle) +
                      " in " + str(removedcontainer))
                removedcontainer[2] = removedcontainer[2] + \
                    removedcontainer[0] - rectangle[0]
                removedcontainer[3] = removedcontainer[3] + \
                    removedcontainer[1] - rectangle[1]
                print("this is the removed container: " + str(removedcontainer))
                containers.append(removedcontainer)
                print(" I added this old split container to the possible list: " +
                      str(containers[-1]))
                containers.append([rectangle[0], rectangle[3]+rectangle[1],
                                   removedcontainer[2], removedcontainer[3]-rectangle[3]])
                containers.append([rectangle[0]+rectangle[2],
                                   rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]])
                print(" I added these two containers to the possible list: " +
                      str(containers[-1]) + " and " + str(containers[-2]))

                print("entire container list: " + str(containers))
                if pygame.Rect(
                        rectangle).collidelist(containers) != -1:
                    print("entered the colliding domain left ")
                    containers[pygame.Rect(
                        rectangle).collidelist(containers)][3] = containers[pygame.Rect(
                            rectangle).collidelist(containers)][3] + \
                        containers[pygame.Rect(
                            rectangle).collidelist(containers)][1] - rectangle[1]
                p = False
                # placedrectangles.append(rectangle)
            elif chosencontainerx < chosencontainery and containers[indexx][0] + containers[indexx][2] <= firstcontainer[2] and containers[indexx][1]+containers[indexx][3] <= firstcontainer[3] and rectangle[2]+containers[indexx][0] <= firstcontainer[2] and rectangle[3]+containers[indexx][1] <= firstcontainer[3] and rectangle[2] <= containers[indexx][2]:
                print("I take path rechts oben: ")

                # placing the rectangles x and y in the containers x and y
                rectangle[1] = containers[indexx][1]
                rectangle[0] = containers[indexx][0]

                # if the rectangle has an x depth and the rectangle coordinate plus the chosencontainers x coordinate are
                if rectangle[0] > 0 and rectangle[0] + containers[indexy][0] <= firstcontainer[2] and rectangle[1] + rectangle[3] > containers[indexx][0]:
                    containers[indexy][2] = rectangle[0]

                    print("I split container into a new container " +
                          str(containers))
                removedcontainer = containers[indexx]
                # removedcontainer = containers.pop(indexx)
                print(" I placed " + str(rectangle) +
                      " in " + str(removedcontainer))
                removedcontainer[3] = removedcontainer[3] + \
                    removedcontainer[1] - rectangle[1]
                removedcontainer[2] = removedcontainer[2] + \
                    removedcontainer[0] - rectangle[0]
                containers.append(removedcontainer)
                print(" I added this old split container to the possible list: " +
                      str(containers[-1]))
                containers.append([rectangle[0], rectangle[3]+rectangle[1],
                                   removedcontainer[2], removedcontainer[3]-rectangle[3]])
                containers.append([rectangle[0]+rectangle[2],
                                   rectangle[1], removedcontainer[2]-rectangle[2], removedcontainer[3]])
                print(" I added these two containers to the possible list: " +
                      str(containers[-1]) + " and " + str(containers[-2]))
                if pygame.Rect(
                        rectangle).collidelist(containers) != -1:
                    print("entered the colliding domain right ")
                    containers[pygame.Rect(
                        rectangle).collidelist(containers)][2] = containers[pygame.Rect(
                            rectangle).collidelist(containers)][2] + \
                        containers[pygame.Rect(
                            rectangle).collidelist(containers)][0] - rectangle[0]
                p = False
                # placedrectangles.append(rectangle)
            else:
                print("doesnt fit bad container")
                l += 1

                """if chosencontainerx >= chosencontainery:
                    container.pop(indexy)
                elif chosencontainerx < chosencontainery:
                    container.pop(indexx)"""
            print("all currently available containers: " + str(containers))

        placedrectangles.append(rectangle)
        rrectangles.remove(rectangle)

        for container in list(containers):
            for rectangle in placedrectangles:
                if pygame.Rect(
                        rectangle).collidelist(containers) != -1:
                    print(containers)
                    print("removed container " + str(containers[pygame.Rect(
                        rectangle).collidelist(containers)]) +
                        " thats touching rectangle " + str(rectangle))
                    containers.remove(containers[pygame.Rect(
                        rectangle).collidelist(containers)])
                    """containers[pygame.Rect(
                        rectangle).collidelist(containers)][2] = containers[pygame.Rect(
                            rectangle).collidelist(containers)][2] + \
                        containers[pygame.Rect(
                            rectangle).collidelist(containers)][0] - rectangle[0]
                    containers[pygame.Rect(
                        rectangle).collidelist(containers)][3] = containers[pygame.Rect(
                            rectangle).collidelist(containers)][3] + \
                        containers[pygame.Rect(
                            rectangle).collidelist(containers)][1] - rectangle[1]"""

                    print(containers)
                elif container[0] + container[2] > firstcontainer[2] or container[1] + container[3] > firstcontainer[3]:
                    print(
                        "removed container thats larger than the border " + str(container))
                    try:
                        containers.remove(container)
                    except:
                        pass
                elif container[2] == 0 or container[3] == 0:
                    try:
                        print("This container is to small: " + str(container))
                        containers.remove(container)
                        print("Container is removed")
                    except:
                        pass
                else:
                    print("none removed")


rcount = 0
action(containers, rrectangles)
print("Placed rectangles " + str(len(placedrectangles)) +
      "and didnt place this many rects: " + str(len(rrectangles)))
print("Got " + str(len(containers)) + " containers left: " + str(containers))
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
        for i in range(len(placedrectangles)):
            pygame.draw.rect(surface, (240 / (i+1), 240 / (i+2),
                                       200 / (i+1)), pygame.Rect(placedrectangles[i]))

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

    # screen.blit(font.render(str(
    #    0) + " " + str(rrectangles[0]), True, (0, 0, 0)), (rrectangles[0][0], rrectangles[0][1]))
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
