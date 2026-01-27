class TestRunner:
    def anyTest(test, *params):
        startTime = System.currentTimeMillis()
        testDetails = f"Test {test} {' '.join(str(p) for p in params)}" if params else f"Test {test}"

        try:
            method = next((m for m in Tests.__dict__.values() if m.__name__ == test), None)
            if method is None:
                raise NoSuchMethodException(f"No such test method: {test}")
            method(None, *params)
            print(f"{testDetails} passed (time: {(System.currentTimeMillis() - startTime) / 1000.0:.1f} s).")
        except Exception as e:
            print(f"{testDetails} failed (time: {(System.currentTimeMillis() - startTime) / 1000.0:.1f} s).")
            raise e