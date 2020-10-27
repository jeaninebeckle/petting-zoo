from datetime import date

class Animal: 
  def __init__(self, name, species, food, chip_number):
    self.name = name
    self.species = species
    self.date_added = date.today()
    self.food = food
    self.__chip_number = chip_number

  def feed(self):
	  print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

  @property
  def chip_number(self):
    return self.__chip_number

  @chip_number.setter
  def chip_number(self, number):
    pass
