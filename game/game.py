from engine import Game
from AI import AI

ais = [AI('right'), AI('left'), AI('up'), AI('left', b=True)]

Game(ais, tick=200)
