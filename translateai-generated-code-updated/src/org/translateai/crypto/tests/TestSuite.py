#imports below were updated
#from org.translateai.crypto.tests import TestRunner
#updated imports are below
from org.translateai.crypto.tests.TestRunner import TestRunner

def main(args):
    TestRunner.anyTest("before")
    TestRunner.anyTest("testPseudoRandom")
    TestRunner.anyTest("hashTest", "cary.txt", 16)
    TestRunner.anyTest("hashTest", "gary.txt", 16)
    TestRunner.anyTest("hashTest", "sunset.jpg", 8)
#added call below to actually run the tests
main("")