from datetime import date

class Pig():
	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.walking = True

pig = Pig('Peter Pan', 'pig')
