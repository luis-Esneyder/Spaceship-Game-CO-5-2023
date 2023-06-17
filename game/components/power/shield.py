from game.components.power.power import Power
from game.utils.constants import SHIELD, SHIELD_TYPE

class Shield(Power):
  
  def __init__(self) -> None:
    super().__init__(SHIELD, SHIELD_TYPE)