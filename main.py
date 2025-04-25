from enum import Enum

## shared constants ##

class DispatchStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

BULKY_VOLUME = 1000000 # cubic centimeters
BULKY_DIMENSION = 150 # cm
HEAVY_MASS = 20 # kg


## helper functions ##

def validate_input(input: int) -> None:
    if not isinstance(input, int):
        raise TypeError(f"Input {input} is not a valid int. Please enter an integer and try again.")
    
    if input <= 0:
        raise ValueError(f"Input {input} must be a non-zero integer. Please enter a non-zero integer and try again.")

def is_bulky(width: int, height: int, length: int) -> bool:
    is_bulky_volume = (width * height * length) >= BULKY_VOLUME
    is_bulky_dimension = any(x >= BULKY_DIMENSION for x in [width, height, length])

    return is_bulky_volume or is_bulky_dimension

def is_heavy(mass: int) -> bool:
    return mass >= HEAVY_MASS


## sorter ##

def sort(width: int, height: int, length: int, mass: int) -> str:
    for arg in [width, height, length, mass]:
        validate_input(arg)

    is_bulky_package = is_bulky(width, height, length)
    is_heavy_package = is_heavy(mass)

    if is_bulky_package and is_heavy_package:
        return DispatchStack.REJECTED.value
    
    if is_bulky_package or is_heavy_package:
        return DispatchStack.SPECIAL.value
    
    return DispatchStack.STANDARD.value

