import sys
import time
from TestResult import MyTestResult
from MyColorStream import _ColorWritelnDecorator


class MyTestRunner:
    def __init__(self,stream=sys.stderr,descriptions=1,verbosity=1):
        self.stream = _ColorWritelnDecorator(stream)
        self.descriptions = descriptions
        self.verbosity = verbosity
        
    def run(self,test):
        result = MyTestResult(self.stream,self.descriptions,self.verbosity)
        self.stream.yellow('Note:Your Unit Tests Starts')
        self.stream.writeln()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        run = result.testsRun
        self.stream.yellow("Ran %d test%s in %.3fs" % (run,run!=1 and "s" or"",timeTaken))
        self.stream.writeln()
        failed,errored = map(len,(result.failures,result.errors))
        self.stream.green("[ PASSED ] %d tests" % (run - failed - errored))
        self.stream.writeln()
        
        if not result.wasSuccessful():
            errorsummary = ""
            if failed:
                self.stream.red("[ FAILED ] %d tests,listed below:" % failed)
                self.stream.writeln()
                for failedtest,failederror in result.failures:
                    self.stream.red("[ FAILED ] %s" % failedtest)
                    self.stream.writeln()
            
            if errored:
                self.stream.red("[ ERRORED ] %d tests" % errored)
                for erroredtest,errormsg in result.errors:
                    self.stream.red("[ ERRORED ] %s" % erroredtest)
                    self.stream.writeln()
            self.stream.writeln()
            if failed:
                self.stream.write("%d ERRORED TEST" % failed)
            if errored:
                self.stream.write("%d ERRORED TEST" % errored)
        
        return result
    