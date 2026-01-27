#3 imports below were added manually
from org.translateai.crypto.tests import Tests
import time
import traceback

class TestRunner:
    def anyTest(test, *params):
        # Line below does not work - it is a mere copy from Java, not correct Python replacement
        #startTime = System.currentTimeMillis()
        # Line below is the fixed one
        startTime = time.time()
        testDetails = f"Test {test} {' '.join(str(p) for p in params)}" if params else f"Test {test}"

        try:
            #the line below did not work
            #method = next((m for m in Tests.__dict__.values() if m.__name__ == test), None)
            #the line below is the replacement for the line above (the goal is to get function by name)
            method = getattr(Tests, test)
            if method is None:
                # Line below does not work - NoSuchMethodException was simply copied from Java, it does not exist in Python
                #raise NoSuchMethodException(f"No such test method: {test}")
                # Line below is fixed line above
                raise Exception(f"No such test method: {test}")
            # Line below does not work - we do not need this first parameter
            #method(None, *params)
            # Line below is fixed line above
            method(*params)
            # Line below does not work - same thing about System.currentTimeMillis
            #print(f"{testDetails} passed (time: {(System.currentTimeMillis() - startTime) / 1000.0:.1f} s).")
            # Line below is fixed line above
            print(f"{testDetails} passed (time: {(time.time() - startTime):.3f} s).")
        except Exception as e:
            # Line below does not work - same thing about System.currentTimeMillis
            #print(f"{testDetails} failed (time: {(System.currentTimeMillis() - startTime) / 1000.0:.1f} s).")
            # Line below is fixed line above
            print(f"{testDetails} failed (time: {(time.time() - startTime):.3f} s).")
            #The line below does not follow original logic - exception should not be raised, just printed, so running tests is not stopped
            #raise e
            #Correct line is below
            traceback.print_exc()
