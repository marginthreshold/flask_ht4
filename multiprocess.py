import random
import time
from multiprocessing import Pool


def sum_array(arr):
    return sum(arr)


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in range(1000000)]
    start_time = time.time()
    with Pool() as p:
        result = sum(p.map(sum_array, [arr[i:i + 1000] for i in range(0, len(arr), 1000)]))
    end_time = time.time()
    print(f"Сумма элементов массива: {result}")
    print(f"Время выполнения вычислений: {end_time - start_time:.5f} секунд")
