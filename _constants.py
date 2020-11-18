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

import os
import pygame
pygame.init()

SCREEN = (1280, 720)
FPS = 60
PARENT = os.path.realpath(os.path.dirname(__file__))

BLACK = (0, 0, 0)

IMAGES = {}
for file in os.listdir(os.path.join(PARENT, "images")):
    if file.endswith(".png"):
        key = file.replace(".png", "")
        if not file.startswith("ic"):
            key = file[1].upper() if file[0] == "w" else file[1].lower()
        IMAGES[key] = pygame.image.load(os.path.join(PARENT, "images", file))