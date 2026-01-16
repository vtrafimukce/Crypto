package org.translateai.crypto.tests;

import org.translateai.crypto.functions.Hash;
import org.translateai.crypto.utils.io.FileUtils;
import org.translateai.crypto.utils.math.PseudoRandom;

import java.nio.file.Paths;

public class Tests {
    private static final String TEST_FOLDER = Paths.get(System.getProperty("user.dir"), "tests").toString();
    private static final String TEST_SOURCE_FOLDER = Paths.get(TEST_FOLDER, "source").toString();
    private static String resultsFolder;

    /** Sets up the test environment by creating a results folder. */
    static void before() {
        resultsFolder = FileUtils.createTestSubFolder(TEST_FOLDER);
    }

    /** Tests the PseudoRandom number generator. */
    static void testPseudoRandom() {
        PseudoRandom rand = new PseudoRandom();
        int[] expectedValues = {122, 217, 21, 65, 131, 248, 215, 147};

        for (int i = 0; i < 8; i++) {
            int actualValue = rand.nextInt8();

            if (actualValue != expectedValues[i]) {
                throw new AssertionError("PseudoRandom sequence item #" + i + " is wrong; expected: " +
                        expectedValues[i] + ", actual: " + actualValue);
            }
        }
    }

    /** Tests the hash calculation for a given file.
     *
     * @param fileName The name of the file to test.
     * @param hashSize The size of the hash in bytes.
     */
    static void hashTest(String fileName, int hashSize) {
        final String hashFileName = fileName + ".hash";
        Hash.calculateAndSave(
                TEST_SOURCE_FOLDER,
                fileName,
                resultsFolder,
                hashFileName,
                hashSize
        );
        boolean matched = FileUtils.areEqual(
                TEST_SOURCE_FOLDER,
                hashFileName,
                resultsFolder,
                hashFileName
        );

        if (!matched) {
            throw new AssertionError("Hash does not match for file: " + fileName);
        }
    }
}
