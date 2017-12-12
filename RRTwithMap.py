#!/usr/bin/env python

# This program generates a simple random tree on an existing map,
# refering to rrt.py from http://msl.cs.uiuc.edu/~lavalle/code.html.

# The maps come from http://rkala.in/codes.php,
# Could also get Matlab codes from this web.

# Exploring random tree (RRT) in a 500*500 map
# and planning path from source to goal.
#
# Written by LiQi from Shanghai Maritime University.Dec 2017
# More details in

import sys, random, pygame
from math import sqrt,cos,sin,atan2
import matplotlib.image as mpimg

#constants
XDIM = 500
YDIM = 500
WINSIZE = [XDIM, YDIM]
EPSILON = 7.0
NUMNODES = 5000
source = [10,10]
goal = [490,490]

# get map shape
map_raw = mpimg.imread('map/map2.bmp')
[width,height] = [len(map_raw[0]),len(map_raw[1])]


def dist(p1,p2):
    return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def step_from_to(p1,p2):
    if dist(p1,p2) < EPSILON:
        return p2
    else:
        theta = atan2(p2[1]-p1[1],p2[0]-p1[0])
        return p1[0] + EPSILON*cos(theta), p1[1] + EPSILON*sin(theta)


def main():

    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption('TEST')
    map = pygame.image.load('map/map2.bmp').convert()
    screen.blit(map,[0,0])
    pygame.display.flip()
    blue = [0,0,255]

    nodes = []
    nodes.append((source[0],source[1])) # Start in the center

    for i in range(NUMNODES):
        rand = random.randint(0,499), random.randint(0,499)
        while map.get_at(rand)[0:3] != (255,255,255):
            rand = random.randint(0, 499), random.randint(0, 499)
        nn = nodes[0]
        for p in nodes:
            if dist(p,rand) < dist(nn,rand):
                nn = p
        newnode = step_from_to(nn,rand)
        while map.get_at((int(round(newnode[0])),int(round(newnode[1]))))[0:3]!=(255,255,255):
            rand = random.randint(0, 499), random.randint(0, 499)
            while map.get_at(rand)[0:3] != (255, 255, 255):
                rand = random.randint(0, 499), random.randint(0, 499)
            nn = nodes[0]
            for p in nodes:
                if dist(p, rand) < dist(nn, rand):
                    nn = p
            newnode = step_from_to(nn, rand)

        nodes.append(newnode)
        pygame.draw.line(screen,blue,nn,newnode)
        pygame.display.update()
        if dist(newnode,goal) <= EPSILON:
            print newnode,'Found Path'
            break

# if python says run, then we should run
if __name__ == '__main__':
  main()
  input("Prease <Esc>")
