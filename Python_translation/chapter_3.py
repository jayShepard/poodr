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