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

donkey = Donkey('Donnie Darko', 'donkey', 'morning', 'donkey chow')
goat = Goat('Gandalf the Grey', 'goat', 'midday', 'goat chow')
llama = Llama('Luna Lovegood', 'llama', 'afternoon', 'llama chow')
sheep = Sheep('Spongebob Squarepants', 'sheep', 'morning', 'krabby patties')
pig = Pig('Peter Pan', 'pig', 'afternoon', 'pig chow')

anaconda = Anaconda('Aragorn', 'anaconda', 'anaconda chow')
copperhead = Copperhead('Captain Crunch', 'copperhead', 'cereal')
cottonmouth = Cottonmouth('Chewbacca', 'cottonmouth', 'babies')
kingsnake = Kingsnake('Kirby', 'kingsnake', 'mice')
python = Python('Peter Pettigrew', 'python', 'python chow')

bass = Bass('Beetlejuice', 'bass', 'bass chow')
catfish = Catfish('Cheshire Cat', 'catfish', 'catfish chow')
goldfish = Goldfish('Godzilla', 'goldfish', 'goldfish chow')
mallard = Mallard('Minerva McGonagall', 'mallard', 'soggy pond bread slices')
swan = Swan('Severus Snape', 'swan', 'swan chow')


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

def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

def __str__(self):
		return f"{self.name} is a {self.species}"
