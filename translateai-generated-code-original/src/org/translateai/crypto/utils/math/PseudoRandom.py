class PseudoRandom:
    PRIMES = [32653, 32687, 32693, 32707, 32713, 32717, 32719, 32749]
    PRIMITIVE_ROOTS = [12596, 6261, 14002, 1229, 4289, 28941, 11367, 5520]

    def __init__(self):
        self.stateOfPowers = [x for x in self.PRIMITIVE_ROOTS]
        self.stateOfIndex = 0

    def getInt8(self):
        result = 0
        for i in range(8):
            result |= ((self.stateOfPowers[i] & (1 << self.stateOfIndex)) >> self.stateOfIndex) << i
        return result

    def shiftState(self):
        for i in range(len(self.PRIMES)):
            self.stateOfPowers[i] = (self.stateOfPowers[i] * self.PRIMITIVE_ROOTS[i]) % self.PRIMES[i]
        self.stateOfIndex += 1
        if self.stateOfIndex == 15:
            self.stateOfIndex = 0

    def nextInt8(self):
        result = self.getInt8()
        self.shiftState()
        return result