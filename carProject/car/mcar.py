from car.carClass import Car
from dotenv import load_dotenv

if __name__ == '__main__':
    mycar=Car()
    mycar.startingTrip()
    mycar.fuelFilling(30)
    mycar.drive(20)
    mycar.gearUp()
    mycar.gearUp()
    mycar.gearUp()
    mycar.gearDown()
    speed = mycar.speedCar()
    x = mycar.dataCar()
    print(x)