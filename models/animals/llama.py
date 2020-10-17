from datetime import date

class Llama():
	def __init__(self, name, species, shift):
		self.name = name
		self.species = species
		self.shift = shift
		self.date_added = date.today()
		self.walking = True
		
llama = Llama('Luna Lovegood', 'llama', 'afternoon')

print(f'{llama.name} the {llama.species} is available to pet during the {llama.shift} shift.')
