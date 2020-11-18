#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import pygame
from _constants import *
from _board import Board


def Main():
    pygame.init()
    pygame.display.set_caption("Chess")
    pygame.display.set_icon(IMAGES["ic"])
    WINDOW = pygame.display.set_mode(SCREEN, pygame.RESIZABLE)

    clock = pygame.time.Clock()
    screen = SCREEN[:]
    board = Board()
    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.VIDEORESIZE:
                screen = (max(event.w, 540), max(event.h, 360))
                WINDOW = pygame.display.set_mode(screen, pygame.RESIZABLE)

        WINDOW.fill(BLACK)
        board.Draw(WINDOW, events, (50, 50), min(screen) - 100)


Main()