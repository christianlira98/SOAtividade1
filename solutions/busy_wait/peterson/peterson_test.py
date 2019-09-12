import time

from solutions.busy_wait.peterson.peterson import PetersonProcess

from solutions.busy_wait.peterson.peterson import number_of_processes

number_of_processes = int(input('Número de processos: '))
number_of_iterations = int(input('Número de iterações: '))

processes = [PetersonProcess(k, number_of_iterations) for k in range(number_of_processes)]

for process in processes:
    process.start()

'''
while peterson1.is_running() or peterson2.is_running():
    time.sleep(0.05)
    print("Result from peterson1: {}\nResult from peterson2: {}".format(
        peterson1.get_result(),
        peterson2.get_result()
    ))
    print(20 * '-')
    pass

print("Result from peterson1: {}\nResult from peterson2: {}".format(
    peterson1.get_result(),
    peterson2.get_result()
))
'''