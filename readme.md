org.translateai.crypto provides implementations for the following cryptographic algorithms:
- hash function based on a long-period pseudorandom number generator, sensitive to changing a single bit in the input - ready for testing
- symmetric encryption/decryption algorithm - to do, if the initial testing of translation is fine
- digital signature - to do, if the initial testing of translation is fine

To run the tests, execute org.translateai.crypto.tests.TestSuite.main with no parameters
Currently, we have tests for:
- PseudoRandom (1 test to check the beginning of the sequence)
- Hash (three tests: two text files with 1 bit difference and one larger media file).
Console output will show the info about passed tests and details of failures, if any, along with the time spent.