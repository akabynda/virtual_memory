import unittest
import random
import time
import os
import datetime
from virtual_memory import Memory

file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                                 'log' + str(random.randint(1,4)) + '.txt'),
                    encoding="utf - 8")
print(file)

class TestMemory(unittest.TestCase):
    print("Start of the test", datetime.datetime.now())
    memory = Memory()

    def test_making_log(self):
        print('Result of testing of making log:', )

    def test_FIFO_log(self):
        print('Result of testing of making FIFO log:', self.memory.FIFO_log(self.memory.making_log(file)))

    print("End of the test", datetime.datetime.now())

if __name__ == '__main__':
    unittest.main()