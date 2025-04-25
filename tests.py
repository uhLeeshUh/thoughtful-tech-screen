from main import sort, DispatchStack

# test consts
normal_mass = 15
normal_dimensions = {"width":10, "height":20, "length":25}

# correctly sorts heavy package
assert sort(**normal_dimensions, mass=35) == DispatchStack.SPECIAL.value
# correctly sorts bulky package by volume
assert sort(width=100, height=110, length=115, mass=normal_mass) == DispatchStack.SPECIAL.value
# correctly sorts bulky package by dimension, at 150
assert sort(width=10, height=20, length=150, mass=normal_mass) == DispatchStack.SPECIAL.value
# correctly sorts bulky package by dimension, over 150
assert sort(width=10, height=20, length=175, mass=normal_mass) == DispatchStack.SPECIAL.value
# correctly sorts heavy AND bulky package
assert sort(width=10, height=20, length=150, mass=50) == DispatchStack.REJECTED.value 
# correct sorts normal package
assert sort(**normal_dimensions, mass=normal_mass) == DispatchStack.STANDARD.value
# fails if any input is not an int
try:
    sort(**normal_dimensions, mass="twenty")
    assert False, "Should raise TypeError"
except TypeError:
    pass
# fails if any input is 0
try:
    sort(width=10, height=0, length=25, mass=normal_mass)
    assert False, "Should raise ValueError"
except ValueError:
    pass
# fails if any input is negative
try:
    sort(width=10, height=-20, length=25, mass=normal_mass)
    assert False, "Should raise ValueError"
except ValueError:
    pass


print("Test suite ran successfully.")
