class SnakePit():
  def __init__(self, attraction_name, description):
    self.attraction_name = attraction_name
    self.description = description
    self.animals = list()

  @property
  def last_critter_added(self):
    return f'{self.animals[-1].name} was the last critter added to {self.attraction_name}'
