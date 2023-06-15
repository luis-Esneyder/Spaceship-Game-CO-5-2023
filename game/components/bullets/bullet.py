class Bullet:
  def __init__(self, image, center):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = center

  def update(self):
    pass

  def draw(self, screen):
    screen.blit(self.image, self.rect)