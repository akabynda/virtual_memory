import unittest
import random
import time
import os
import datetime
from virtual_memory import Memory

class TestMemory(unittest.TestCase):
    print("Start of the test", datetime.datetime.now())
    memory = Memory()

    def test_working_with_logs(self):
        name_file = 'log' + str(random.randint(1, 4)) + '.txt'
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', name_file), encoding="utf - 8")
        original_log = self.memory.making_log(file)
        print('Result of testing of making FIFO log:', self.memory.FIFO_log(original_log))
        print('Result of testing of making LRU log:', self.memory.LRU_log(original_log))
        print('Result of testing of making OPT log:', self.memory.OPT_log(original_log))
        file.close()

    def test_for_algorithms(self):
        name_file = 'log' + str(random.randint(1, 4)) + '.txt'
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', name_file), encoding="utf - 8")
        print(file)
        original_log = self.memory.making_log(file)
        LRU_log = self.memory.LRU_log(original_log)
        FIFO_log = self.memory.FIFO_log(original_log)
        OPT_log = self.memory.OPT_log(original_log)
        OPT_count = LRU_count = FIFO_count = 0
        algo = 'NO'
        pages = []
        for i in range(50):                          # создаем случайный набор страниц
            pages.append(str(random.randint(1,12)))
        pages_str = ''
        for i in range(50):
            pages_str += (str(pages[i]) + ';')
        print('Result of FIFO algorithm:', self.memory.FIFO_algorithm(FIFO_log, pages_str, time.time() + 60, name_file, algo))
        print('Result of LRU algorithm:', self.memory.LRU_algorithm(LRU_log, pages_str, time.time() + 60, name_file, algo))
        print('Result of OPT algorithm:', self.memory.OPT_algorithm(OPT_log, pages_str, time.time() + 60, name_file, algo))
        file.close()

    print("End of the test", datetime.datetime.now())

if __name__ == '__main__':
    unittest.main()