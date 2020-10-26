from datetime import date

class Animal: 
  def __init__(self, name, species, shift, food, chip_number):
    self.name = name
    self.species = species
    self.shift = shift
    self.date_added = date.today()
    self.food = food
    self.__chip_number = chip_number

  @property
  def chip_number(self):
    return self.__chip_number

  @chip_number.setter
  def chip_number(self, number):
    pass