package org.translateai.crypto.tests;

import static org.translateai.crypto.tests.TestRunner.anyTest;

public class TestSuite {
    /** Main method to run the test suite. */
    public static void main(String[] args) {
        anyTest("before");
        anyTest("testPseudoRandom");
        anyTest("hashTest", "cary.txt", 16);
        anyTest("hashTest", "gary.txt", 16);
        anyTest("hashTest", "sunset.jpg", 8);
    }
}
