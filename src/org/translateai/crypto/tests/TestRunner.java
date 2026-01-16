package org.translateai.crypto.tests;

import java.lang.reflect.Method;
import java.util.Arrays;
import java.util.stream.Stream;

public class TestRunner {
    /** Runs any test method from the Tests class by name with optional parameters.
     *
     * @param test   The name of the test method to run.
     * @param params Optional parameters to pass to the test method.
     */
    static void anyTest(String test, Object... params) {
        long startTime = System.currentTimeMillis();
        final String testDetails = "Test " + test + (params.length > 0 ? Arrays.toString(params) : "");

        try {
            Method method = Stream.of(Tests.class.getDeclaredMethods()).filter(m -> m.getName().equals(test)).findFirst()
                    .orElseThrow(() -> new NoSuchMethodException("No such test method: " + test));
            method.invoke(null, params);
            System.out.println(testDetails + " passed (time: " + (System.currentTimeMillis() - startTime) / 1000.0 + " s).");
        } catch (Exception | AssertionError e) {
            System.err.println(testDetails + " failed (time: " + (System.currentTimeMillis() - startTime) / 1000.0 + " s).");
            e.printStackTrace();
        }
    }
}
