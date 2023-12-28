import random
import time
import asyncio


async def sum_array(arr):
    return sum(arr)


async def main():
    arr = [random.randint(1, 100) for _ in range(1000000)]
    start_time = time.time()
    tasks = []
    for i in range(0, len(arr), 1000):
        tasks.append(asyncio.create_task(sum_array(arr[i:i + 1000])))
    result = sum(await asyncio.gather(*tasks))
    end_time = time.time()
    print(f"Сумма элементов массива: {result}")
    print(f"Время выполнения вычислений: {end_time - start_time:.5f} секунд")

asyncio.run(main())