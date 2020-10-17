from datetime import date

class Swan():
	def __init__(self, name, species):
		self.name = name
		self.species = species
		self.date_added = date.today()
		self.swimming = True
		
swan = Swan('Severus Snape', 'swan')
