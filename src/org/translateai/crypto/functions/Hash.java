/**
 * Class implementing a simple hash function using a pseudo-random number generator.
 */
package org.translateai.crypto.functions;

import org.translateai.crypto.utils.io.FileUtils;
import org.translateai.crypto.utils.math.PseudoRandom;

public class Hash {
    /**
     * Calculates the hash of the given data.
     *
     * @param data         The input data to hash.
     * @param hashByteSize The desired size of the hash in bytes.
     * @return The calculated hash as a byte array.
     */
    public static byte[] calculate(byte[] data, int hashByteSize) {
        PseudoRandom prng = new PseudoRandom();
        int[] resultInt = new int[hashByteSize];

        for (byte b : data) {
            for (int i = 0; i < 8; i++) {
                int bit = (b >> i) & 1;

                for (int j = 0; j < hashByteSize; j++) {
                    if (bit == 1)
                        prng.shiftState();

                    resultInt[j] ^= prng.nextInt8();

                    if (bit == 0)
                        prng.shiftState();
                }
            }
        }

        byte[] result = new byte[hashByteSize];

        for (int i = 0; i < hashByteSize; i++) {
            result[i] = (byte) resultInt[i];
        }

        return result;
    }

    /**
     * Calculates the hash of a file's contents and saves it to another file.
     *
     * @param sourceFolder The folder containing the source file.
     * @param sourceFile   The name of the source file.
     * @param hashFolder   The folder to save the hash file.
     * @param hashFile     The name of the hash file.
     * @param hashByteSize The desired size of the hash in bytes.
     */
    public static void calculateAndSave(String sourceFolder, String sourceFile,
                                        String hashFolder, String hashFile,
                                        int hashByteSize) {
        byte[] sourceData = FileUtils.readFile(sourceFolder, sourceFile);
        byte[] hashData = calculate(sourceData, hashByteSize);
        FileUtils.writeFile(hashFolder, hashFile, hashData);
    }
}
