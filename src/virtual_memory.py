import argparse
import os
def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--list', type=str)
    p.add_argument('--time', type=str)
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
list = parser.parse_args().list
time = parser.parse_args().time
old_log = making_log(file)
FIFO_log = []
print(old_log)
b = old_log[1]
a = old_log[0]
g = old_log[3]
c = old_log[2]
print(a)
print(b)
FIFO = []
FIFO_e = []
for i in range(int(max(a))):
    FIFO.append(0)
    FIFO_e.append(0)
for i in range(len(a)):
    j = int(a[i]) - 1
    FIFO[j] = int(b[i])
    FIFO_e[j] = int(g[i])
print(FIFO)
print(FIFO_e)
FIFO_bul = True #проверяется есть ли данная страница в оперативной памяти
for i in range(len(FIFO_e)):
    if(FIFO_e[i] != list):
        FIFO_bul = False
if(FIFO_bul == False):
    temp = FIFO[0]
    k = 0
    for i in range(len(FIFO)):
        if(FIFO[i] < temp):
            temp = FIFO[i]
            k = i
    FIFO[k] = int(time)
    FIFO_e[k] = int(list)
print(FIFO)
print(FIFO_e)