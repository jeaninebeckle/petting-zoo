from datetime import date

class Llama():
	def __init__(self, name, species, shift, food):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

	def __str__(self):
		return (f'{self.name} is a {self.species}')

llama = Llama('Luna Lovegood', 'llama', 'afternoon', 'llama chow')

print(f'{llama.name} the {llama.species} is available to pet during the {llama.shift} shift.')

print(llama.feed())
