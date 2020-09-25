import argparse
import os
def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    return p

def making_log(file):  #преобразуем прочитанный файл
    log = file.read().replace(' ', '').replace('#', '').replace(':', '').replace('\n', ';') + ';'
    a = []
    b = []
    c = []
    g = []
    while (log!= ''):
        f1 = log.index(',')
        n = log[:f1]
        a.append(n)
        t = log[(f1 + 1):(f1 + 5)]
        b.append(t)
        v = log[(f1 + 6):(f1 + 7)]
        c.append(v)
        f2 = log.index(';')
        d = log[(f1 + 8):f2]
        g.append(d)
        log = log[(f2 + 1):]
    log = [a,b,c,g]
    return log

def LRU_log(log):  # преобразуем прочитанный файл
    return log

def FIFO_log(log):  #преобразуем прочитанный файл
    return log

parser = parser_args()
file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file), encoding="utf - 8")
old_log = making_log(file)
FIFO_log = FIFO_log(old_log)
print(old_log)

#for i in range(a):
