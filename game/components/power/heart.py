from game.components.power.power import Power
from game.utils.constants import HEART, HEART_TYPE
class Heart(Power):
  def __init__(self):
    super().__init__(HEART, HEART_TYPE)

