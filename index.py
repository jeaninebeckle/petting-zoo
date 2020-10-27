from datetime import date

from models.animals.swan import Swan
from models.animals.sheep import Sheep
from models.animals.mallard import Mallard
from models.animals.goldfish import Goldfish
from models.animals.catfish import Catfish
from models.animals.bass import Bass
from models.animals.python import Python
from models.animals.kingsnake import Kingsnake
from models.animals.cottonmouth import Cottonmouth
from models.animals.copperhead import Copperhead
from models.animals.anaconda import Anaconda
from models.animals.pig import Pig
from models.animals.llama import Llama
from models.animals.goat import Goat
from models.animals.donkey import Donkey

from models.attractions.pettingzoo import PettingZoo
from models.attractions.snakepit import SnakePit
from models.attractions.wetlands import Wetlands



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


varmint_village.animals.append(sheep)
varmint_village.animals.append(donkey)
varmint_village.animals.append(goat)
varmint_village.animals.append(llama)
varmint_village.animals.append(pig)

slither_inn.animals.append(anaconda)
slither_inn.animals.append(copperhead)
slither_inn.animals.append(cottonmouth)
slither_inn.animals.append(kingsnake)
slither_inn.animals.append(python)

critter_cove.animals.append(bass)
critter_cove.animals.append(catfish)
critter_cove.animals.append(goldfish)
critter_cove.animals.append(mallard)
critter_cove.animals.append(swan)


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


swan.feed()
