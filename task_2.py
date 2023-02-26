from functools import wraps
from multiprocessing import cpu_count, Pool, current_process
import time


core = cpu_count()


def get_time(func):
    """Декоратор для визначення часу виконання функції"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"time: {finish-start}")
        return result

    return wrapper


@get_time
def factorize(*number):
    """Синхронна функція"""

    result = []
    for num in number:
        lst = []
        for n in range(1, num + 1):
            if num % n == 0:
                lst.append(n)
        result.append(lst)
    return result


@get_time
def factorize_1(*number):
    pass


if __name__ == "__main__":
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
