from org.translateai.crypto.tests import TestRunner

def main(args):
    TestRunner.anyTest("before")
    TestRunner.anyTest("testPseudoRandom")
    TestRunner.anyTest("hashTest", "cary.txt", 16)
    TestRunner.anyTest("hashTest", "gary.txt", 16)
    TestRunner.anyTest("hashTest", "sunset.jpg", 8)  