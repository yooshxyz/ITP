from math import pi
# you can also just import math and then do math.pi instead of just pi.
radInput = float(input("What is the radius?"))
# int are only whole numbers.
# float => numbers that might have decimal points
area = pi*radInput*radInput  # can also be written as rad**2
print(f"The area is {area}")

