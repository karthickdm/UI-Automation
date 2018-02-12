from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from Script.TrialTest import TrialTest


example_tests = TestLoader().loadTestsFromTestCase(TrialTest)

suite = TestSuite([example_tests])
kwargs = {
    "output": "TestReport",
    "report_name": "TrialTestReport",
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)