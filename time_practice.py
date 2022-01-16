from functools import lru_cache
import time

# .time() 1970/1/1からの経過を表示
print(time.time())
print(time.time()/(60*60*24*365))


# 処理時間の算出に使える
before = time.time()

@lru_cache #  キャッシュを有効活用する関数
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


before = time.time()
fib(10)
after = time.time()
print(after - before)


# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())

# .localtime() 構造化データで返す
lolaltime = time.localtime()
print(lolaltime)
print(lolaltime.tm_year)

# .sleep(secs) secs秒だけ待機する
# sec = 3
# time.sleep(sec)
# print(f"{sec}秒待ちました")


def timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} は {after - before} 秒かかりました")
    return inner


@timer
def lazy_func(sec):
    print("I'm working so hard")
    time.sleep(sec)
    print("I'm finally done")


lazy_func(3)
