package org.translateai.crypto.utils.math;

public class PseudoRandom {
    private static final int[] PRIMES = {
            32653, 32687, 32693, 32707, 32713, 32717, 32719, 32749
    };

    private static final int[] PRIMITIVE_ROOTS = {
            12596, 6261, 14002, 1229, 4289, 28941, 11367, 5520
    };

    private final int[] stateOfPowers;
    private int stateOfIndex;

    public PseudoRandom() {
        stateOfPowers = new int[PRIMES.length];
        System.arraycopy(PRIMITIVE_ROOTS, 0, stateOfPowers, 0, PRIMES.length);
        stateOfIndex = 0;
    }

    private int getInt8() {
        int result = 0;

        for (int i = 0; i < 8; i++) {
            result |= ((stateOfPowers[i] & (1 << stateOfIndex)) >> stateOfIndex) << i;
        }

        return result;
    }

    public void shiftState() {
        for (int i = 0; i < PRIMES.length; i++) {
            stateOfPowers[i] = (stateOfPowers[i] * PRIMITIVE_ROOTS[i]) % PRIMES[i];
        }

        stateOfIndex++;

        if (stateOfIndex == 15)
            stateOfIndex = 0;
    }

    public int nextInt8() {
        int result = getInt8();
        shiftState();
        return result;
    }
}
