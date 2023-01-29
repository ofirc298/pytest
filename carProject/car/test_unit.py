import unittest
import dotenv
from car.carClass import Car
from car.logfile import LogFile


class MyTestCase(unittest.TestCase):
    def setUp(self):
        dotenv.load_dotenv()
        self.car = Car()
        self.logCar = LogFile

    def test_startingTrip_starter(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if startingTrip function resets speed
                :return: pass/failed
        """
        try:
            self.car.startingTrip()
            self.assertEqual(self.car.starter,1)
            self.logCar.Log('pass : test_startingTrip and starter is 1')
        except AssertionError as asErr:
            self.logCar.Log('Failed : test_startingTrip with parmter: actual :0 excepted :1 ')

    def test_startingTrip_indrive(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if startingTrip function resets speed
                :return: pass/failed
        """
        try:
            self.car.startingTrip()
            self.assertEqual(self.car.inDrive,1)
            self.logCar.Log('pass : test_startingTrip_inDrive and inDrive is 1')
        except AssertionError as asErr:
            self.logCar.Log('Failed : test_startingTrip_inDrive with parmter: actual :0 excepted :1 ')


    def test_drive_fuel(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if drive fuel function resets speed
                :return: pass/failed
        """
        try:
            self.car.fuel = 0
            with self.assertRaises(Exception) :
                self.car.drive(50)
            self.logCar.Log("pass: test_drive_fuel beacuse fuel is 0")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")

    def test_drive_capacity(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if drive capacity function resets speed
                :return: pass/failed
        """
        try:
            self.car.fuel = 4
            with self.assertRaises(Exception) :
                self.car.drive(50)
            self.logCar.Log("pass: test_drive_capacity beacuse capacity is low")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")

    def test_drive_starter(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if drive starter function resets speed
                :return: pass/failed
        """
        try:
            self.car.fuel = 10
            self.car.starter =0
            with self.assertRaises(Exception) :
                self.car.drive(50)
            self.logCar.Log("pass: test_drive_starter beacuse starter is off")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")

    def test_drive(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if drive function resets speed
                :return: pass/failed
        """
        try:
            self.car.fuel = 20
            self.car.starter = 1
            self.car.drive(2)
            self.logCar.Log("pass: test_drive is ok")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")


    def test_fuelFilling_maxprice(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if fuelFilling maxprice function resets speed
                :return: pass/failed
        """
        try:
            self.car.maxPrice = 50
            with self.assertRaises(Exception) :
                self.car.fuelFilling(30)
            self.logCar.Log("pass: test_fuelFilling_maxprice beacuse not many")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")


    def test_fuelFilling_literToFill(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if fuelFilling literToFill function resets speed
                :return: pass/failed
        """
        try:
            self.car.maxFuel = 50
            self.car.fuel = 49
            with self.assertRaises(Exception) :
                self.car.fuelFilling(30)
            self.logCar.Log("pass: test_fuelFilling_literToFill is not enough")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")


    def test_fuelFilling(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if fuelFilling function resets speed
                :return: pass/failed
        """
        try:
            self.car.maxPrice = 500
            self.car.fuel = 10
            self.car.fuelFilling(20)
            self.logCar.Log("pass: test_fuelFilling is ok")
        except AssertionError as asErr:
            self.logCar.Log("pass: somthing wrong")

    def test_stop_starter(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if stop function resets speed
                :return: pass/failed
        """
        try:
            self.car.stop()
            self.assertEqual(self.car.starter,0)
            self.logCar.Log('pass : test_stop_starter and starter is 0')
        except AssertionError as asErr:
            self.logCar.Log('Failed : test_stop_starter with parmter: actual :1 excepted :0 ')

    def test_stop_indrive(self):
        """
                name : ofir cohen
                date : 23/01/2023
                :param : none
                function that checks if stop function resets speed
                :return: pass/failed
        """
        try:
            self.car.stop()
            self.assertEqual(self.car.inDrive,0)
            self.logCar.Log('pass : test_stop_indrive and inDrive is 0')
        except AssertionError as asErr:
            self.logCar.Log('Failed : test_stop_indrive with parmter: actual :1 excepted :0 ')




if __name__ == '__main__':
    unittest.main()
