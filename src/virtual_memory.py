import argparse
import os
def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--page', type=str)
    p.add_argument('--time', type=str)
    p.add_argument('--algo', type=str)
    return p


def formating_time(time):
    time = str(time)
    lenght = len(time)
    if (lenght < 4):
        time = '0' + time[0] + ':' + time[1:]
    else:
        time = time[:2] + ':' + time[2:]
    return time


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


def OPT_log(log):
    times = log[1]
    frames = log[0]
    pages = log[3]
    OPT_t = []  # значения времени в log OPT
    OPT_p = []
    for i in range(int(max(frames))): # заполняем log пустыми значениями
        OPT_t.append(0)
        OPT_p.append(0)
    for i in range(len(frames)): # загружаем в log последние операции
        j = int(frames[i]) - 1
        OPT_t[j] = int(times[i])
        OPT_p[j] = int(pages[i])
    OPT_t_max = OPT_t[0]
    for i in range(len(OPT_t)):
        if (OPT_t[i] > OPT_t_max):
            OPT_t_max = OPT_t[i]
    for i in range(len(frames)):
        j = int(frames[i]) - 1
        OPT_t[j] = OPT_t_max - OPT_t[j]
    OPT_log = [OPT_t, OPT_p]
    print(OPT_log)
    return OPT_log

def FIFO_log(log):  # преобразуем прочитанный файл под FIFO
    times = log[1]
    frames = log[0]
    pages = log[3]
    FIFO_t = [] # значения времени в log FIFO
    FIFO_p = [] # значение страницы в log FIFO
    for i in range(int(max(frames))): # заполняем log пустыми значениями
        FIFO_t.append(0)
        FIFO_p.append(0)
    for i in range(len(frames)): # загружаем в log последние операции
        j = int(frames[i]) - 1
        FIFO_t[j] = int(times[i])
        FIFO_p[j] = int(pages[i])
    FIFO_log = [FIFO_t, FIFO_p] # составляем целостный log
    return FIFO_log


def LRU_log(log):  # преобразуем прочитанный файл под LRU
    times = log[1]
    frames = log[0]
    pages = log[3]
    manipulations = log[2]
    LRU_t = [] # значения времени в log LRU
    LRU_p = [] # значение страницы в log LRU
    LRU_m = [] # значение манипуляции в log LRU
    for i in range(int(max(frames))): # заполняем log пустыми значениями
        LRU_t.append(0)
        LRU_p.append(0)
        LRU_m.append(0)
    for i in range(len(frames)): # загружаем в log последние операции
        j = int(frames[i]) - 1
        LRU_t[j] = int(times[i])
        LRU_p[j] = int(pages[i])
        LRU_m[j] = manipulations[i]
    LRU_log = [LRU_t, LRU_p, LRU_m] # составляем целостный log
    return LRU_log

def OPT_algorithm(OPT_log, page, time, file):
    file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
    OPT_t = OPT_log[0]
    OPT_p = OPT_log[1]
    OPT_bul = 0
    k = 0
    temp = OPT_t[0]
    for i in range(len(OPT_t)):
        if(OPT_t[i] > temp):
            k = i
            temp = OPT_t[i]
    for i in range(len(OPT_p)):
        if (OPT_p[i] == int(page)):
            OPT_bul += 1
    if (OPT_bul == 0): # если страницы нет
        new_str = ';#' + str(k+1) + ' , ' + formating_time(time) + ' , w , ' + str(page)
    else:
        new_str =';#' + str(k+1) + ' , ' + formating_time(time) + ' , r , ' + str(page)
    file.write(new_str.replace(';', '\n'))
    OPT_p[k] = int(page)
    OPT_t[k] = 0
    OPT_log = [OPT_t, OPT_p]
    return OPT_log


def LRU_algorithm(LRU_log, page, time, file):
    file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
    LRU_p = LRU_log[1]
    LRU_t = LRU_log[0]
    LRU_m = LRU_log[2]
    LRU_bul = 0  # проверяется есть ли данная страница в оперативной памяти
    temp = LRU_t[0]
    k = -1
    for i in range(len(LRU_t)):  # ищем самое раннее обращение
        if (LRU_t[i] < temp and LRU_m[i] == 'r'):
            temp = LRU_t[i]
            k = i
    if(k == -1):
        for i in range(len(LRU_t)):  # ищем самое раннее обращение
            if (LRU_t[i] < temp):
                temp = LRU_t[i]
                k = i
    for i in range(len(LRU_p)):
        if (LRU_p[i] == int(page)):
            LRU_bul += 1
    LRU_t[k] = int(time)
    LRU_p[k] = int(page)
    if (LRU_bul == 0): # если страници нет
        new_str = ';#' + str(k+1) + ' , ' + formating_time(LRU_t[k]) + ' , w , ' + str(LRU_p[k])
        LRU_m[k] = 'w'
        print(new_str)
    else:
        new_str =';#' + str(k+1) + ' , ' + formating_time(LRU_t[k]) + ' , r , ' + str(LRU_p[k])
        LRU_m[k] = 'r'
    file.write(new_str.replace(';', '\n'))
    LRU_log = [LRU_t, LRU_p , LRU_m]
    file.close()
    return LRU_log # обновляем log


def FIFO_algorithm(FIFO_log, page, time, file):
    file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
    FIFO_p = FIFO_log[1]
    FIFO_t = FIFO_log[0]
    FIFO_bul = 0  # проверяется есть ли данная страница в оперативной памяти
    temp = FIFO_t[0]
    k = 0
    for i in range(len(FIFO_t)):  # меняем время самого раннего обращение на новое
        if (FIFO_t[i] < temp):
            temp = FIFO_t[i]
            k = i
    FIFO_t[k] = int(time)
    for i in range(len(FIFO_p)):
        if (FIFO_p[i] == int(page)):
            FIFO_bul += 1
    FIFO_p[k] = int(page)
    if (FIFO_bul == 0): # если страницы нет
        new_str = ';#' + str(k+1) + ' , ' + formating_time(FIFO_t[k]) + ' , w , ' + str(FIFO_p[k])
        print(new_str)
    else:
        new_str =';#' + str(k+1) + ' , ' + formating_time(FIFO_t[k]) + ' , r , ' + str(FIFO_p[k])
    file.write(new_str.replace(';', '\n'))
    FIFO_log = [FIFO_t, FIFO_p]
    file.close()
    return FIFO_log # обновляем log


parser = parser_args()
file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), encoding="utf - 8")
page = parser.parse_args().page
time = parser.parse_args().time.replace(':', '')
algorithm = parser.parse_args().algo
original_log = making_log(file)
file.close()

OPT_log = OPT_algorithm(OPT_log(original_log), page, time, file)
print(OPT_log)