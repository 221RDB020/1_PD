import pygame

class Button():
	def __init__(self, image, hover_image, pos):
		self.image = image
		self.hover_image = hover_image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
	
	def hover(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = self.hover_image
		else:
			self.image = self.image

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False