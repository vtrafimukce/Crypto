import os
#imports below were updated
#from org.translateai.crypto.functions import Hash
#from org.translateai.crypto.utils.io import FileUtils
#from org.translateai.crypto.utils.math import PseudoRandom
#updated imports are below
from org.translateai.crypto.functions.Hash import Hash
from org.translateai.crypto.utils.io.FileUtils import FileUtils
from org.translateai.crypto.utils.math.PseudoRandom import PseudoRandom

TEST_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")
TEST_SOURCE_FOLDER = os.path.join(TEST_FOLDER, "source")
resultsFolder = None

def before():
    global resultsFolder
    resultsFolder = FileUtils.createTestSubFolder(TEST_FOLDER)

def testPseudoRandom():
    rand = PseudoRandom()
    expectedValues = [122, 217, 21, 65, 131, 248, 215, 147]

    for i in range(8):
        actualValue = rand.nextInt8()

        if actualValue != expectedValues[i]:
            raise AssertionError("PseudoRandom sequence item #" + str(i) + " is wrong; expected: " +
                                 str(expectedValues[i]) + ", actual: " + str(actualValue))

def hashTest(fileName, hashSize):
    hashFileName = fileName + ".hash"
    Hash.calculateAndSave(TEST_SOURCE_FOLDER,
                          fileName,
                          resultsFolder,
                          hashFileName,
                          hashSize)
    matched = FileUtils.areEqual(TEST_SOURCE_FOLDER,
                                 hashFileName,
                                 resultsFolder,
                                 hashFileName)

    if not matched:
        raise AssertionError("Hash does not match for file: " + fileName)
