import argparse
import os
def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--page', type=str)
    p.add_argument('--time', type=str)
    p.add_argument('--algo', type=str)
    return p


def making_log(file):  # преобразуем прочитанный файл
    log = file.read().replace(' ', '').replace('#', '').replace(':', '').replace('\n', ';') + ';'
    frames = [] # номера кадра
    times = [] # время манипуляции
    manipulations = [] # тип манипуляции
    pages = [] # страницы
    while (log!= ''): # трансформируем строку log в список
        f1 = log.index(',') # первая запятая
        N = log[:f1] # номер кадра
        frames.append(N) # добавляем номер кадра
        T = log[(f1 + 1):(f1 + 5)] # время
        times.append(T) # добавляем время
        M = log[(f1 + 6):(f1 + 7)] # манипуляция
        manipulations.append(M) # добавляем манипуляцию
        f2 = log.index(';') # конец операции
        P = log[(f1 + 8):f2] # страница
        pages.append(P) # добавляем страницу
        log = log[(f2 + 1):] # обновляем лог
    log = [frames,times,manipulations,pages] # готовый список списков
    return log

def LRU_log(log):  # преобразуем прочитанный файл
    return log

def FIFO_log(log):  # преобразуем прочитанный файл под FIFO
    times = log[1]
    frames = log[0]
    pages = log[3]
    FIFO_t = []
    FIFO_p = []
    for i in range(int(max(frames))):
        FIFO_t.append(0)
        FIFO_p.append(0)
    for i in range(len(frames)):
        j = int(frames[i]) - 1
        FIFO_t[j] = int(times[i])
        FIFO_p[j] = int(pages[i])
    FIFO_log = [FIFO_t, FIFO_p]
    return FIFO_log

def FIFO_algorithm(FIFO_log, page, time):
    FIFO_p = FIFO_log[1]
    FIFO_t = FIFO_log[0]
    FIFO_bul = True  # проверяется есть ли данная страница в оперативной памяти
    for i in range(len(FIFO_p)):
        if (FIFO_p[i] != page):
            FIFO_bul = False
    if (FIFO_bul == False):
        temp = FIFO_t[0]
        k = 0
        for i in range(len(FIFO_t)):
            if (FIFO_t[i] < temp):
                temp = FIFO_t[i]
                k = i
        FIFO_t[k] = int(time)
        FIFO_p[k] = int(page)
    FIFO_log = [FIFO_t, FIFO_p]
    return FIFO_log


parser = parser_args()
file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), encoding="utf - 8")
page = parser.parse_args().page
time = parser.parse_args().time.replace(':', '')
algorithm = parser.parse_args().algo
original_log = making_log(file)

FIFO_log = FIFO_algorithm(FIFO_log(original_log), page, time)
print(FIFO_log)