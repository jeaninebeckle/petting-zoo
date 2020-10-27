from attractions.attraction import Attraction
from movements import Walking


class PettingZoo(Attraction):
  def __init__(self, attraction_name, description):
    super().__init__(attraction_name, description)

  def add_animal_pythonic(self, animal):
    try:
      if animal.walk_speed > -1:
        self.animals.append(animal)
        print(f'{animal.name} the {animal.species} now lives in {self.attraction_name}')
    except AttributeError as ex:
      print(f'{animal.name} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

  @property
  def last_critter_added(self):
    return f'{self.animals[-1].name} was the last critter added to {self.attraction_name}'

# when a function is part of a class it's called a method
