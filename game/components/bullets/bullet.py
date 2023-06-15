class Bullet:


  def __init__(self, image, center, type):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.center = center
    self.type = type

  def update(self):
    pass


  def draw(self, screen):
    screen.blit(self.image, self.rect)