from datetime import date

class Donkey():
	def __init__(self, name, species, shift):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True

donkey = Donkey('Donnie Darko', 'donkey', 'morning')

print(f'{donkey.name} the {donkey.species} is available to pet during the {donkey.shift} shift.')
