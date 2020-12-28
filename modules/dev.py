import multiprocessing as mp
import time


def foo(e):
    print('foo waiting at {}'.format(time.perf_counter()))
    e.wait()
    print('Done at {}'.format(time.perf_counter()))


if __name__ == '__main__':
    e = mp.Event()
    pr = mp.Process(target=foo, args=(e,))

    pr.start()
    print('Started')
    time.sleep(2)
    e.set()
    pr.join()
