import pytest
import dotenv
from car.carClass import Car
from car.logfile import LogFile


@pytest.fixture
def mycar():
    dotenv.load_dotenv()
    logCar = LogFile
    return Car()

def test_startingTrip_starter(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if startingTrip function resets speed
            :return: pass/failed
    """
    try:
        mycar.startingTrip()
        assert mycar.starter == 1
        mycar.logCar.Log('pass : test_startingTrip and starter is 1')
    except AssertionError as asErr:
        mycar.logCar.Log('Failed : test_startingTrip with parmter: actual :0 excepted :1 ')

def test_startingTrip_indrive(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if startingTrip function resets speed
            :return: pass/failed
    """
    try:
        mycar.startingTrip()
        assert mycar.inDrive == 1
        mycar.logCar.Log('pass : test_startingTrip_inDrive and inDrive is 1')
    except AssertionError as asErr:
        mycar.logCar.Log('Failed : test_startingTrip_inDrive with parmter: actual :0 excepted :1 ')


def test_drive_fuel(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if drive fuel function resets speed
            :return: pass/failed
    """
    try:
        mycar.fuel = 0
        with pytest.raises(Exception):
            mycar.drive(50)
        mycar.logCar.Log("pass: test_drive_fuel beacuse fuel is 0")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")

def test_drive_capacity(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if drive capacity function resets speed
            :return: pass/failed
    """
    try:
        mycar.fuel = 4
        with pytest.raises(Exception):
            mycar.drive(50)
        mycar.logCar.Log("pass: test_drive_capacity beacuse capacity is low")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")

def test_drive_starter(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if drive starter function resets speed
            :return: pass/failed
    """
    try:
        mycar.fuel = 10
        mycar.starter =0
        with pytest.raises(Exception):
            mycar.drive(50)
        mycar.logCar.Log("pass: test_drive_starter beacuse starter is off")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")

def test_drive(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if drive function resets speed
            :return: pass/failed
    """
    try:
        mycar.fuel = 20
        mycar.starter = 1
        mycar.drive(2)
        mycar.logCar.Log("pass: test_drive is ok")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")


def test_fuelFilling_maxprice(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if fuelFilling maxprice function resets speed
            :return: pass/failed
    """
    try:
        mycar.maxPrice = 50
        with pytest.raises(Exception):
            mycar.fuelFilling(30)
        mycar.logCar.Log("pass: test_fuelFilling_maxprice beacuse not many")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")


def test_fuelFilling_literToFill(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if fuelFilling literToFill function resets speed
            :return: pass/failed
    """
    try:
        mycar.maxFuel = 50
        mycar.fuel = 49
        with pytest.raises(Exception):
            mycar.fuelFilling(30)
        mycar.logCar.Log("pass: test_fuelFilling_literToFill is not enough")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")


def test_fuelFilling(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if fuelFilling function resets speed
            :return: pass/failed
    """
    try:
        mycar.maxPrice = 500
        mycar.fuel = 10
        mycar.fuelFilling(20)
        mycar.logCar.Log("pass: test_fuelFilling is ok")
    except AssertionError as asErr:
        mycar.logCar.Log("pass: somthing wrong")

def test_stop_starter(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if stop function resets speed
            :return: pass/failed
    """
    try:
        mycar.stop()
        assert mycar.starter == 0
        mycar.logCar.Log('pass : test_stop_starter and starter is 0')
    except AssertionError as asErr:
        mycar.logCar.Log('Failed : test_stop_starter with parmter: actual :1 excepted :0 ')

def test_stop_indrive(mycar):
    """
            name : ofir cohen
            date : 23/01/2023
            :param : none
            function that checks if stop function resets speed
            :return: pass/failed
    """
    try:
        mycar.stop()
        assert mycar.inDrive == 0
        mycar.logCar.Log('pass : test_stop_indrive and inDrive is 0')
    except AssertionError as asErr:
        mycar.logCar.Log('Failed : test_stop_indrive with parmter: actual :1 excepted :0 ')



