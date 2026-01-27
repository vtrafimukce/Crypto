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
        result = [resultInt[i] for i in range(hashByteSize)]
        return result
    
    def calculateAndSave(sourceFolder, sourceFile, hashFolder, hashFile, hashByteSize):
        sourceData = FileUtils.readFile(sourceFolder, sourceFile)
        hashData = calculate(sourceData, hashByteSize)
        FileUtils.writeFile(hashFolder, hashFile, hashData) 