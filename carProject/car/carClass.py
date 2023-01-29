import dotenv
import os
from car.logfile import LogFile
dotenv.load_dotenv()

class Car:
  def __init__(self):
    self.speed = int(os.getenv('speed'))
    self.speedToGear = int(os.getenv('speedToGear'))
    self.gear = int(os.getenv('gear'))
    self.fuel = int(os.getenv('fuel'))
    self.maxFuel = int(os.getenv('maxFuel'))
    self.km = int(os.getenv('km'))
    self.pricePerLiter = int(os.getenv('pricePerLiter'))
    self.maxPrice = int(os.getenv('maxPrice'))
    self.starter = int(os.getenv('starter'))
    self.inDrive = int(os.getenv('inDrive'))
    self.logCar = LogFile

  def startingTrip(self):
    self.starter = 1
    self.inDrive = 1

  def drive(self,kmToDrive):
    newFuel = kmToDrive/self.km

    tofuel = newFuel - self.fuel
    if tofuel > 0:
      self.fuelFilling(tofuel);

    if self.fuel <= 0:
      raise Exception(os.getenv("car_fuel"))
    if newFuel > self.fuel:
      raise Exception(os.getenv("enough_fuel"))
    if self.starter == 0:
      raise Exception(os.getenv("car_drive"))

    self.fuel -= newFuel

  def speedCar(self):
    self.speed = self.speedToGear * self.gear
    return self.speed

  def stop(self):
    self.starter = 0
    self.inDrive = 0

  def fuelFilling(self, literToFill):
    sum = literToFill * self.pricePerLiter

    if sum > self.maxPrice:
      raise Exception(os.getenv("no_many"))

    if literToFill >= (self.maxFuel - self.fuel):
      raise Exception(os.getenv('space_tank'))

    self.maxPrice -= sum
    self.fuel += literToFill

  def gearUp(self):
    if self.starter == 0:
      raise Exception(os.getenv('engine_off'))
    if self.gear == 6:
      raise Exception(os.getenv('max_gear'))
    else:
      self.gear += 1
      self.speedCar()

  def gearDown(self):
    if self.starter == 0:
      raise Exception(os.getenv('engine_off'))
    if self.gear == 1:
      raise Exception(os.getenv('min_gear'))
    else:
      self.gear += 1
      self.speedCar()

  def dataCar(self):
    obj = {
      self.speed,
      self.speedToGear,
      self.gear,
      self.fuel,
      self.maxFuel,
      self.km,
      self.pricePerLiter,
      self.maxPrice,
      self.starter,
      self.inDrive,
    }

    return obj