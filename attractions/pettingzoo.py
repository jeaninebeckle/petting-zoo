from attractions.attraction import Attraction

class PettingZoo(Attraction):
  def __init__(self, attraction_name, description):
    super().__init__(attraction_name, description)

  @property
  def last_critter_added(self):
    return f'{self.animals[-1].name} was the last critter added to {self.attraction_name}'

# when a function is part of a class it's called a method
