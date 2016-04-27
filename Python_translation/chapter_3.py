############## Page 36 ##############
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

    def gear_inches(self):
        return self.ratio() * Wheel(self.rim, self.tire).diameter()

    def ratio(self):
        return self.chainring / float(self.cog)

# ...


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

# ...

Gear(52, 11, 26, 1.5).gear_inches()

############## Page 39 ##############
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

    def gear_inches(self):
        return self.ratio() * Wheel(self.rim, self.tire).diameter()

# ...

Gear(52, 11, 26, 1.5).gear_inches()

############## Page 41 ##############
class Gear:
    def __init__(self, chainring, cog, wheel):
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

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

# ...

# Gear expects a 'Duck' that knows 'diameter'
Gear(52, 11, Wheel(26, 1.5)).gear_inches()

############## Page 43 ##############
class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._wheel = Wheel(rim, tire)

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def wheel(self):
        return self._wheel

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

# ...

############## Page 43 ##############
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

    @property
    def wheel(self):
        return self._wheel

    @wheel.setter
    def wheel(self):
        # Python doesn't have ||= but this does the same thing
        self._wheel = self._wheel or Wheel(self.rim, self.tire)

# ...

############## Page 44 ##############
def gear_inches(self):
    self.ratio * self.wheel.diameter()

############## Page 44 ##############
def gear_inches(self):
    # ... a efw lines of scary math
    foo = some_intermediate_results * self.wheel.diameter()
    # ... more lines of scary math
    return foo

############## Page 45 ##############
def gear_inches(self):
    # ... a few lines of scary math
    foo = some_intermediate_results * self.diameter
    # ... more lines of scary math
    return foo

@property
def diameter(self):
    return self.wheel.diameter()

############## Page 46 ##############
class Gear
    def __init__(self, chainring, cog, wheel):
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
# ...

Gear(52,
     11,
     Wheel(26, 1.5)).gear_inches()

############## Page 47 ##############
class Gear:
    # **kwargs is used to for unspecified number of named arguments
    def __init__(self, **kwargs):
        self._chainring = kwargs['chainring']
        self._cog = kwargs['cog']
        self._wheel = kwargs['wheel']
# ...

Gear(chainring=52,
     cog= 11,
     wheel= Wheel(26, 1.5)).gear_inches()

############## Page 48 ##############
    # specifying default using ||
    def __init__(self, **kwargs):
        self._chainring = kwargs['chainring'] || 40
        self._cog = kwargs['cog'] || 18
        self._wheel = kwargs['wheel']

############## Page 49 ##############
    # specifying defaults using get()
    def __init__(self, **kwargs):
        self._chainring = kwargs.get('chainring', 40)
        self._cog = kwargs.get('cog', 18)
        self._wheel = kwargs['wheel']

############## Page 49 ##############
    # specifying defaults by merging a default dictionary
    def __init_(self, **kwargs):
        # Note, the z = {**x, **y} syntax is new for python 3.5
        # Previous versions can use the following 2-step syntax:
        # z = x.copy()
        # z.update(y)
        args = {**kwargs, **self.defaults}
        self._chainring = args['chainring']
# ...

    @property
    def defaults(self):
        return {'chainring': 40, 'cog': 20}

############## Page 50 ##############
# This is getting tricky to translate here. So Python doesn't have a module
# keyword since, in Python, all .py files are modules by definition.

# When Gear is part of an external interface
# In a file called SomeFramework.py
class Gear:
    def __init__(self, chainring,cog, wheel):
        self._chainring = chainring
        self._cog = cog
        self._wheek = wheel

    # ...

# wrap the interface to protext yourself from changes
# In a file called GearWrapper.py
from SomeFramework import Gear, Wheel

def gear(**kwargs):
    return Gear(kwargs['chainring'],
                kwargs['cog'],
                kwargs['wheel'])

# In a file called test.py
import GearWrapper
GearWrapper.gear(chainring = 52,
                 cog = 11,
                 wheel = Wheel(26, 1.5)).gear_inches()