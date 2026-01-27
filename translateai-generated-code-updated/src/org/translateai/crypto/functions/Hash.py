#2 imports below were added manually
from org.translateai.crypto.utils.math.PseudoRandom import PseudoRandom
from org.translateai.crypto.utils.io.FileUtils import FileUtils

class Hash:
    def calculate(data, hashByteSize):
        prng = PseudoRandom()
        resultInt = [0] * hashByteSize

        for b in data:
            for i in range(8):
                bit = (b >> i) & 1

                for j in range(hashByteSize):
                    if bit == 1:
                        prng.shiftState()

                    resultInt[j] ^= prng.nextInt8()

                    if bit == 0:
                        prng.shiftState()
        #line below creates not the object that we need here (list of ints instead of bytes)
        #result = [resultInt[i] for i in range(hashByteSize)]
        #line below is the fixed one
        result = bytes(resultInt)
        return result
    
    def calculateAndSave(sourceFolder, sourceFile, hashFolder, hashFile, hashByteSize):
        sourceData = FileUtils.readFile(sourceFolder, sourceFile)
        # Line below does not work, added Hash. before calculate
        #hashData = calculate(sourceData, hashByteSize)
        # Line below is the fixed one
        hashData = Hash.calculate(sourceData, hashByteSize)
        FileUtils.writeFile(hashFolder, hashFile, hashData) 
