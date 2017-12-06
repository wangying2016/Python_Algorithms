import cProfile
from time import sleep


def wait():
    for i in range(1000):
        pass
    wait_first()


def wait_first():
    sleep(3)
    wait_second()


def wait_second():
    sleep(1)


if __name__ == '__main__':
    cProfile.run('wait()')


