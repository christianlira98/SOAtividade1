from threading import Thread
import time

from solutions.with_block.monitor.monitor import IntegerMonitor

increment_value = int(input('Valor total de incremento: '))
number_of_threads = int(input('Número de Threads: '))


global_variable = 0


def run_with_monitor(limit):
    global global_variable

    monitor = IntegerMonitor()

    for k in range(limit):
        monitor.increment_value()
    global_variable = monitor.get_resource()


def run_without_monitor(limit):
    global global_variable
    for k in range(limit):
        global_variable += 1


print(f'Incrementing a global variable {number_of_threads} Threads (each thread increment {increment_value}): ')
print('Without monitor:')

for k in range(10):
    list_of_threads_without_monitor = [Thread(target=run_without_monitor, args=(increment_value,)) for k in range(number_of_threads)]

    for thrd in list_of_threads_without_monitor:
        thrd.start()

    is_alive = True
    while is_alive:
        for thrd in list_of_threads_without_monitor:
            if thrd.is_alive():
                break
            is_alive = False

    print(f'Global variable = {global_variable}')
    global_variable = 0

print(40 * '-')

print('With monitor')

for k in range(10):
    list_of_threads_with_monitor = [Thread(target=run_with_monitor, args=(increment_value,)) for k in range(number_of_threads)]

    for thrd in list_of_threads_with_monitor:
        thrd.start()

    is_alive = True
    while is_alive:
        for thrd in list_of_threads_with_monitor:
            if thrd.is_alive():
                time.sleep(1)
                break
            is_alive = False

    print(f'Global variable = {global_variable}')
    global_variable = 0
    IntegerMonitor().set_resource(0)
