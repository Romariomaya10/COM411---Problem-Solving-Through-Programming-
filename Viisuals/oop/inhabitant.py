from abc import ABC, abstractmethod

class Inhabitant(ABC):

  MAX_ENERGY = 100

  def __init__(self, name="Inhabitant", age=0):
    self.name = name
    self.age = age
    self.energy = Inhabitant.MAX_ENERGY

  def grow(self):
    self.age += 1

  def eat(self, ammount):
    self.energy += ammount
    if self.energy > Inhabitant.MAX_ENERGY:
      self.energy = Inhabitant.MAX_ENERGY

  def move(self, distance):
    self.energy -= distance
    if self.energy < 0:
      self.energy = 0

  @abstractmethod
  def something(self):
    pass