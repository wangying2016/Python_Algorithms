from time import sleep
import cProfile


# in shell
# py -3 -m timeit -s "import TimeMyFunction as m" "m.test_function"
# output
# 10000000 loops, best of 3: 0.0278 usec per loop
def test_function():
    sleep(2)


test_function()

