from attractions.attraction import Attraction
from movements import slithering

class SnakePit(Attraction):
  def __init__(self, attraction_name, description):
    super().__init__(attraction_name, description)

  def add_animal_pythonic(self, animal):
    try:
      if animal.slither_speed > -1:
        self.animals.append(animal)
        print(f'{animal.name} the {animal.species} now lives in {self.attraction_name}')
    except AttributeError as ex:
      print(f'{animal.name} is not a reptile, so please do not put it in the {self.attraction_name} attraction.')
  
  @property
  def last_critter_added(self):
    return f'{self.animals[-1].name} was the last critter added to {self.attraction_name}'
