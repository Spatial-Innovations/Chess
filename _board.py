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
import chess
from _constants import *


class Board:
    def __init__(self):
        self.position = chess.Board()
        self.flipped = False

    def Draw(self, window, loc, size):
        sqSize = size / 8

        for row in range(8):
            for col in range(8):
                currLoc = (loc[0] + col*sqSize, loc[1] + row*sqSize, sqSize+1, sqSize+1)
                color = BOARD_WHITE if (row + col) % 2 == 0 else BOARD_BLACK
                pygame.draw.rect(window, color, currLoc)

        for row in range(8):
            for col in range(8):
                square = 8*row + (7-col) if self.flipped else 8*(7-row) + col
                piece = self.position.piece_at(square)
                if piece is not None:
                    symbol = piece.symbol()
                    image = pygame.transform.scale(IMAGES[symbol], (int(sqSize*0.9), int(sqSize*0.9)))
                    currLoc = (col*sqSize + sqSize*0.05 + loc[0], row*sqSize + sqSize*0.05 + loc[1])
                    window.blit(image, currLoc)