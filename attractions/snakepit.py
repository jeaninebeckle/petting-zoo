from attractions.attraction import Attraction

class SnakePit(Attraction):
  def __init__(self, attraction_name, description):
    super().__init__(attraction_name, description)

  @property
  def last_critter_added(self):
    return f'{self.animals[-1].name} was the last critter added to {self.attraction_name}'
