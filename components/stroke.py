import pygame
from config.constants import *


class Stroke():

  def __init__(self, text, font, size, opx, color, ocolor, pos):
    self.text = text
    self.font = self.get_font(size, font)
    self.opx = opx
    self.color = color
    self.ocolor = ocolor
    self.pos = pos
    self._circle_cache = {}

  def get_font(self, size, font):
    if font == "bold":
      return pygame.font.Font(BOLD_FONT, size)
    elif font == "regular":
      return pygame.font.Font(REGULAR_FONT, size)

  def _circlepoints(self, r):
    r = int(round(r))
    if r in self._circle_cache:
      return self._circle_cache[r]
    x, y, e = r, 0, 1 - r
    self._circle_cache[r] = points = []
    while x >= y:
      points.append((x, y))
      y += 1
      if e < 0:
        e += 2 * y - 1
      else:
        x -= 1
        e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points

  def render(self, screen):
    if self.font is None:
      return
    textsurface = self.font.render(str(self.text), True,
                                   self.color).convert_alpha()
    w = textsurface.get_width() + 2 * self.opx
    h = self.font.get_height()
    osurf = pygame.Surface((w, h + 2 * self.opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))
    surf = osurf.copy()
    osurf.blit(
        self.font.render(str(self.text), True, self.ocolor).convert_alpha(),
        (0, 0))
    for dx, dy in self._circlepoints(self.opx):
      surf.blit(osurf, (dx + self.opx, dy + self.opx))
    surf.blit(textsurface, (self.opx, self.opx))
    screen.blit(surf, (self.pos[0] - surf.get_width() / 2,
                       self.pos[1] - surf.get_height() / 2))
