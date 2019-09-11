from threading import Thread
import time

from solutions.with_block.monitor.monitor import IntegerMonitor

increment_value = 100000

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


print(f'Incrementing a global variable 5 Threads (each thread increment {increment_value}): ')
print('Without monitor:')

for k in range(10):
    thread1 = Thread(target=run_without_monitor, args=(increment_value,))
    thread1.start()
    thread2 = Thread(target=run_without_monitor, args=(increment_value,))
    thread2.start()
    thread3 = Thread(target=run_without_monitor, args=(increment_value,))
    thread3.start()
    thread4 = Thread(target=run_without_monitor, args=(increment_value,))
    thread4.start()
    thread5 = Thread(target=run_without_monitor, args=(increment_value,))
    thread5.start()

    while thread1.is_alive() or thread2.is_alive() or thread3.is_alive() or thread3.is_alive() or thread4.is_alive() or thread5.is_alive():
        time.sleep(2)
        pass

    print(f'Global variable = {global_variable}')
    global_variable = 0

print(40 * '-')

print('With monitor')

for k in range(10):
    thread1 = Thread(target=run_with_monitor, args=(increment_value,))
    thread1.start()
    thread2 = Thread(target=run_with_monitor, args=(increment_value,))
    thread2.start()
    thread3 = Thread(target=run_with_monitor, args=(increment_value,))
    thread3.start()
    thread4 = Thread(target=run_with_monitor, args=(increment_value,))
    thread4.start()
    thread5 = Thread(target=run_with_monitor, args=(increment_value,))
    thread5.start()

    while thread1.is_alive() or thread2.is_alive() or thread3.is_alive() or thread3.is_alive() or thread4.is_alive() or thread5.is_alive():
        time.sleep(2)
        pass

    print(f'Global variable = {global_variable}')
    global_variable = 0
    IntegerMonitor().set_resource(0)
