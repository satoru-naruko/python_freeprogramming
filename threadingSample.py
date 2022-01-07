import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)


def worker1(d, rlock):
    logging.debug('start')
    with rlock:
        i = d['x']
        time.sleep(5)
        d['x'] = i + 1
        logging.debug(d)
        with rlock:
            d['x'] = i + 1
    logging.debug('end')


def worker2(d, rlock):
    logging.debug('start')
    # memo -> "with rlock:" means rlock.acquire(). rlock.acquire needs rlock.release()
    with rlock:
        i = d['x']
        d['x'] = i + 1
        logging.debug(d)
        with rlock:
            d['x'] = i + 1
    logging.debug('end')


if __name__ == '__main__':
    d = {'x': 0}
    rlock = threading.RLock()
    t1 = threading.Thread(target=worker1(d, rlock))
    t2 = threading.Thread(target=worker2(d, rlock))
    t1.start()
    t2.start()

    t1.join()
    t2.join()
