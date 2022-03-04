'''
1. Написать умножение матриц случайной размерности
2. Написать перемножение каждой матрицы из списка друг с другом 
3. Распараллелить второй пункт с помощью multiprocessing
3. Вывести сравнение времени работы распараллеленного кода и не распараллеленного
'''

import numpy as np
from timeit import timeit
import multiprocessing
from random import randint

def mmul_native(matrix1, matrix2):
    '''
    Функция перемножения 2-ух матриц
    Пункт 1
    '''
    result = []
    '''Ваш код'''
    return result

def mmul(matrixs):
    '''
    Функция перемножения каждой матрицы с каждой
    Пункт 2
    '''
    result = []
    '''Ваш код'''
    return result

if __name__ == '__main__':
    '''
    Точка входа в программу
    '''
    matrices = []
    for z in range(4):
        matrices.append([[randint(1, 100) for i in range(10)] for j in range(10)]) # Создание матриц
    '''
    3 и 4 пункты
    '''
    '''Ваш код'''