############## Page 18 ##############
chainring = 52 # number of teeth
cog = 11
ratio = chainring / float(cog)
print(ratio) # -> 4.72727272727

chainring = 30
cog = 27
ratio = chainring / float(cog)
print(ratio) # -> 1.11111111111

############## Page 19 ##############
class Gear:
    # Python has no attr_reader equivalent, instead it uses @property as a
    # getter
    def __init__(self, chainring, cog):
      self._chainring = chainring
      self._cog = cog

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    # In python it is necessary to use self when referring to an internal method
    # or variable, even if they've been given a @property tag
    def ratio(self):
        return self.chainring / float(self.cog)

print(Gear(52, 11).ratio()) # -> 4.72727272727
print(Gear(30, 27).ratio()) # -> 1.11111111111

############## Page 20 ##################
class Gear:

    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * (self.rim + (self.tire * 2))

print(Gear(52, 11, 26, 1.5).gear_inches())
# -> 137.0909090909091

print(Gear.new(52, 11, 24, 1.25).gear_inches())
# -> 125.27272727272728

############## Page 20 ##############
print(Gear(52, 11).ratio()) # didn't this used to work?
# Traceback (most recent call last):
#   File "<pyshell#21>", line 1, in <module>
#     Gear(52, 11).ratio()
# TypeError: __init__() missing 2 required positional arguments: 'rim' and
# 'tire'

############## Page 24 ##############
class Gear:
    def __init__(self, chainring, cog):
        self.chainring = chainring
        self.cog = cog

    def ratio(self):
        return self.chainring /float(self.cog) # -> road to ruin

############## Page 25 ##############
class Gear:
    # Using decorators is the closest we get in Python to attr_reader
    #
    def __init__(self, chainring, cog):
      self._chainring = chainring # using _naming to indicate internal attribute
      self._cog = cog

    @property # <-------
    def chainring(self):
        return self._chainring

    @property # <-------
    def cog(self):
        return self._cog

    def ratio(self):
        return self.chainring / float(self.cog) # <-------

############## Page 25 ##############
    # Python decorator for getting attribute
    @property
    def cog(self):
        return self._cog

############## Page 25 ##############
    # a simple reimplementation of cog
    @property
    def cog(self):
        return self._cog * unanticipated_adjustment_factor

############## Page 25 ##############
class ObscuringReferences:
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def diameter(self):
        # Python doesn't have a .collect, this does the same thing using list
        # comprehension
        return [[cell[0], cell[1]*2] for cell in self.data]

############## Page 27 ##############
# rim and tire sizes (now in milimeters!) in a 2d array
_data = [[622, 20], [622, 23], [559, 30], [559, 40]]

############## Page 28 ##############
from collections import namedtuple
class RevealingReference:
    def __init__(self, data):
        self._wheels = self.wheelify(data)

    @property
    def wheels(self):
        return self._wheels

    def diameters(self):
        return [wheel.rim + (wheel.tire * 2) for wheel in self.wheels]
    # ... now everyone can send rim/tire to wheel

    # namedtuple is similar to Stuct. Must be imported from collections
    Wheel = namedtuple('Wheel', ('rim', 'tire'))
    def wheelify(self, data):
        return [self.Wheel(cell[0], cell[1]) for cell in data]

############## Page 29 ##############
    def diameters(self):
        return [wheel.rim + (wheel.tire * 2) for wheel in self.wheels]

############## Page 29 ##############
    # first - iterate over array
    def diameters(self):
        return [self.diameter(wheel) for wheel in self.wheels]

    # second - calculate diameter of ONE wheel
    def diameter(self, wheel):
        return wheel.rim + (wheel.tire * 2)

############## Page 30 ##############
    def gear_inches(self):
        return self.ratio() * (self.rim + (self.tire * 2))

############## Page 30 ##############
    def gear_inches(self):
        self.ratio() + self.diameter()

    def diameter(self):
        self.rim + (self.tire * 2)

############## Page 32 ##############
class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._wheel = self.Wheel(rim, tire)

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def wheel(self):
        return self._wheel

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter

    # Python doesn't have any analog to the do .. end syntax in Ruby. It seems
    # the only options are to leave the diameter method exposed in the main
    # class, or create a new class for Wheel, which is the next example. I'm
    # open to suggestions though if someone knows a way to do it.
    #
    # Wheel = Struct.new(:rim, :tire) do
    #   def diameter
    #     rim + (tire * 2)
    #   end
    # end

############## Page 32 ##############
from math import pi
class Gear:
    def __init__(self, chainring, cog, wheel=None):
        self._chainring = chainring
        self._cog = cog
        self._wheel = wheel

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def wheel(self):
        return self._wheel

    def ratio(self):
        return self.chainring / float(self.cog)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter

class Wheel:
    def __init__(self, rim, tire):
        self._rim = rim
        self._tire = tire

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire

    def diameter(self):
        return self.rim + (self.tire * 2)

    def circumference(self):
        return self.diameter() * pi

wheel = Wheel(26, 1.5)
print(wheel.circumference())
# -> 91.106186954104

print(Gear(52, 11, wheel).gear_inches())
# -> 137.090909090909

print(Gear(52, 11).ratio())
# -> 4.72727272727273