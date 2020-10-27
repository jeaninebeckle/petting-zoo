from datetime import date

from animals import Swan
from animals import Sheep
from animals import Mallard
from animals import Goldfish
from animals import Catfish
from animals import Bass
from animals import Python
from animals import Kingsnake
from animals import Cottonmouth
from animals import Copperhead
from animals import Anaconda
from animals import Pig
from animals import Llama
from animals import Goat
from animals import Donkey

from attractions import PettingZoo
from attractions import SnakePit
from attractions import Wetlands



varmint_village = PettingZoo('Varmint Village', 'soft and cuddly farm animalss')
slither_inn = SnakePit('Slither Inn', 'animalss that might want to eat you')
critter_cove = Wetlands('Critter Cove', 'fish and feathered friends')

donkey = Donkey('Donnie Darko', 'donkey', 'morning', 'donkey chow', 23408)
goat = Goat('Gandalf the Grey', 'goat', 'midday', 'goat chow', 2340834)
llama = Llama('Luna Lovegood', 'llama', 'afternoon', 'llama chow', 24545)
sheep = Sheep('Spongebob Squarepants', 'sheep', 'morning', 'krabby patties', 4308540)
pig = Pig('Peter Pan', 'pig', 'afternoon', 'pig chow', 39473)

anaconda = Anaconda('Aragorn', 'anaconda', 'anaconda chow', 34574579)
copperhead = Copperhead('Captain Crunch', 'copperhead', 'cereal', 304584)
cottonmouth = Cottonmouth('Chewbacca', 'cottonmouth', 'babies', 4359485)
kingsnake = Kingsnake('Kirby', 'kingsnake', 'mice', 405439)
python = Python('Peter Pettigrew', 'python', 'python chow', 348509)

bass = Bass('Beetlejuice', 'bass', 'bass chow', 3204803)
catfish = Catfish('Cheshire Cat', 'catfish', 'catfish chow', 1844590)
goldfish = Goldfish('Godzilla', 'goldfish', 'goldfish chow', 897450)
mallard = Mallard('Minerva McGonagall', 'mallard', 'soggy pond bread slices', 756590)
swan = Swan('Severus Snape', 'swan', 'swan chow', 3049877)


varmint_village.add_animal(sheep)
varmint_village.add_animal(donkey)
varmint_village.add_animal(goat)
varmint_village.add_animal(llama)
varmint_village.add_animal(pig)

slither_inn.add_animal(anaconda)
slither_inn.add_animal(copperhead)
slither_inn.add_animal(cottonmouth)
slither_inn.add_animal(kingsnake)
slither_inn.add_animal(python)

critter_cove.add_animal(bass)
critter_cove.add_animal(catfish)
critter_cove.add_animal(goldfish)
critter_cove.add_animal(mallard)
critter_cove.add_animal(swan)


for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

for animal in slither_inn.animals:
    print(f'You can find {animal.name} the {animal.species} in {slither_inn.attraction_name}')

for animal in critter_cove.animals:
    print(f'You can find {animal.name} the {animal.species} in {critter_cove.attraction_name}')


def __repr__(self):
	return f'{self.name} is a {self.species} with chip number {self.chip_number}'

print(varmint_village.last_critter_added)
print(slither_inn.last_critter_added) 
print(critter_cove.last_critter_added)
