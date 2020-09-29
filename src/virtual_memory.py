import argparse
import os
import time
from datetime import datetime

def parser_args():
    p = argparse.ArgumentParser()
    p.add_argument('--file', type=str)
    p.add_argument('--page', type=str)
    p.add_argument('--time', type=str)
    p.add_argument('--algo', type=str)
    return p

class Memory:

    def formating_time(self, time):
        time = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d;%H:%M:%S')
        return time

    def making_log(self, file):  # преобразуем прочитанный файл
        log = file.read().replace(' ', '').replace('#', '').replace('\n', ';') + ';'
        frames = [] # номера кадра
        times = [] # время манипуляции
        manipulations = [] # тип манипуляции
        pages = [] # страницы
        while (log!= ''): # трансформируем строку log в список
            f1 = log.index(',') # первая запятая
            N = log[:f1] # номер кадра
            frames.append(N) # добавляем номер кадра
            log = log[(f1 + 1):]
            f2 = log.index(',')
            T = log[:f2] # время
            log = log[(f2 + 1):]
            T = int(time.mktime(time.strptime(T, '%Y-%m-%d;%H:%M:%S')))
            times.append(T) # добавляем время
            f3 = log.index(',')
            M = log[:f3] # манипуляция
            log = log[(f3 + 1):]
            manipulations.append(M) # добавляем манипуляцию
            f4 = log.index(';') # конец операции
            P = log[:f4] # страница
            pages.append(P) # добавляем страницу
            log = log[(f4 + 1):] # обновляем лог
        log = [frames,times,manipulations,pages] # готовый список списков
        return log

    def OPT_log(self, log):
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
        for i in range(len(OPT_t)):  # находим макс. время
            if (OPT_t[i] > OPT_t_max):
                OPT_t_max = OPT_t[i]
        for i in range(len(frames)): # высчитываем относительно него разницу
            j = int(frames[i]) - 1
            OPT_t[j] = OPT_t_max - OPT_t[j]
        OPT_log = [OPT_t, OPT_p]
        print(OPT_log)
        return OPT_log

    def FIFO_log(self, log):  # преобразуем прочитанный файл под FIFO
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

    def LRU_log(self, log):  # преобразуем прочитанный файл под LRU
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

    def OPT_algorithm(self, OPT_log, page, time, file):
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
        OPT_t = OPT_log[0]
        OPT_p = OPT_log[1]
        OPT_bul = 0
        k = 0
        temp = OPT_t[0]
        for i in range(len(OPT_t)): # ищем самое раннее обращение
            if(OPT_t[i] > temp):
                k = i
                temp = OPT_t[i]
        for i in range(len(OPT_p)): # проверяем наличие страницы
            if (OPT_p[i] == int(page)):
                OPT_bul += 1
        if (OPT_bul == 0):  # счетчик OPT
            global OPT_count
            OPT_count += 1
        global algorithm
        if (algorithm == 'OPT'):
            if (OPT_bul == 0): # если страницы нет
                new_str = '/#' + str(k+1) + ' , ' + Memory().formating_time(time) + ' , w , ' + str(page)
            else:
                new_str ='/#' + str(k+1) + ' , ' + Memory().formating_time(time) + ' , r , ' + str(page)
            file.write(new_str.replace('/', '\n'))
        OPT_p[k] = int(page)
        for i in range (len(OPT_t)): # скорость работы не позволяет времени измениться, поэтому прибавляем
                                     # любую константу
            OPT_t[i] += 10
        OPT_t[k] = 0
        OPT_log = [OPT_t, OPT_p]
        return OPT_log

    def LRU_algorithm(self, LRU_log, page, time, file):
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
        LRU_p = LRU_log[1]
        LRU_t = LRU_log[0]
        LRU_m = LRU_log[2]
        LRU_bul = 0  # проверяется есть ли данная страница в оперативной памяти
        temp = LRU_t[0]
        k = 0
        for i in range(len(LRU_t)):  # ищем самое раннее обращение
            if (LRU_t[i] < temp and LRU_m[i] == 'r'):
                temp = LRU_t[i]
                k = i
        if(k == 0 and LRU_m[0] == 'w'):
            for i in range(len(LRU_t)):  # ищем самое раннее обращение
                if (LRU_t[i] < temp):
                    temp = LRU_t[i]
                    k = i
        for i in range(len(LRU_p)): # проверяем наличие страницы
            if (LRU_p[i] == int(page)):
                LRU_bul += 1
        LRU_t[k] = time
        LRU_p[k] = int(page)
        if (LRU_bul == 0):  # счетчик LRU
            global LRU_count
            LRU_count += 1
            LRU_m[k] = 'w'
        else:
            LRU_m[k] = 'r'
        global algorithm
        if(algorithm == 'LRU'):
            if (LRU_bul == 0): # если страници нет
                new_str = '/#' + str(k+1) + ' , ' + Memory().formating_time(LRU_t[k]) + ' , w , ' + str(LRU_p[k])
            else:
                new_str ='/#' + str(k+1) + ' , ' + Memory().formating_time(LRU_t[k]) + ' , r , ' + str(LRU_p[k])
            file.write(new_str.replace('/', '\n'))
        LRU_log = [LRU_t, LRU_p, LRU_m]
        file.close()
        return LRU_log # обновляем log

    def FIFO_algorithm(self, FIFO_log, page, time, file):
        file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'), 'a')
        FIFO_p = FIFO_log[1]
        FIFO_t = FIFO_log[0]
        FIFO_bul = 0  # проверяется есть ли данная страница в оперативной памяти
        temp = FIFO_t[0]
        k = 0
        for i in range(len(FIFO_t)):  # находим самое раннее обращение
            if (FIFO_t[i] < temp):
                temp = FIFO_t[i]
                k = i
        FIFO_t[k] = time
        for i in range(len(FIFO_p)): # проверяем наличие страницы
            if (FIFO_p[i] == int(page)):
                FIFO_bul += 1
        FIFO_p[k] = int(page)
        if (FIFO_bul == 0): # счетчик FIFO
            global FIFO_count
            FIFO_count += 1
        global algorithm
        if(algorithm == 'FIFO'):
            if (FIFO_bul == 0): # если страницы нет
                new_str = '/#' + str(k+1) + ' , ' + Memory().formating_time(FIFO_t[k]) + ' , w , ' + str(FIFO_p[k])
            else:
                new_str ='/#' + str(k+1) + ' , ' + Memory().formating_time(FIFO_t[k]) + ' , r , ' + str(FIFO_p[k])
            file.write(new_str.replace('/', '\n'))
        FIFO_log = [FIFO_t, FIFO_p]
        file.close()
        return FIFO_log # обновляем log

if __name__ == '__main__':
    memory1 = Memory()
    parser = parser_args()
    file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', parser.parse_args().file + '.txt'),
                encoding="utf - 8")
    pages = parser.parse_args().page + ';' # ввод страниц
    algorithm = parser.parse_args().algo # выбираем алгоритм, который будет работать с файлом
    print(file)
    original_log = memory1.making_log(file) # создаем оригинальный log
    file.close()
    OPT_count = LRU_count = FIFO_count = 0 # счетчик для теста
    LRU_log = memory1.LRU_log(original_log)
    FIFO_log = memory1.FIFO_log(original_log)
    OPT_log = memory1.OPT_log(original_log)
    while pages != '':
        f1 = pages.index(';')
        page = pages[:f1] # берем одну страницу
        pages = pages[(f1 + 1):] # удаляем ее из списка
        OPT_log = memory1.OPT_algorithm(OPT_log, page, time.time() + 60, file) # скорость работы привышает скорость
                                                                       # обновления времени, поэтому прибавляем
                                                                       # любую константу
        LRU_log = memory1.LRU_algorithm(LRU_log, page, time.time() + 60, file)
        FIFO_log = memory1.FIFO_algorithm(FIFO_log, page, time.time() + 60, file)
    print('OPT:', OPT_count, 'FIFO:', FIFO_count, 'LRU:', LRU_count)