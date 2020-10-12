from datetime import date

class Donkey():
	def __init__(self, name, species, date_added):
		self.name = name
		self.species = species
		self.date_added = date_added
		self.walking = True

donkey = Donkey('Donnie Darko', 'donkey', date.today())

class Goat():
	def __init__(self, name, species, date_added):
		self.name = name
		self.species = species
		self.date_added = date_added
		self.walking = True

goat = Goat('Gandalf the Grey', 'goat', date.today())

class Pig():
	def __init__(self, name, species, date_added):
		self.name = name
		self.species = species
		self.date_added = date_added
		self.walking = True

pig = Pig('Peter Pan', 'pig', date.today())

class Llama():
	def __init__(self, name, species, date_added):
		self.name = name
		self.species = species
		self.date_added = date_added
		self.walking = True
		
llama = Llama('Luna Lovegood', 'llama', date.today())

class Sheep():
	def __init__(self, name, species, date_added):
		self.name = name
		self.species = species
		self.date_added = date_added
		self.walking = True
		
sheep = Sheep('Spongebob Squarepants', 'sheep', date.today())
