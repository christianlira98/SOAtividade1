import time

from solutions.busy_wait.peterson.peterson import PetersonProcess


peterson1 = PetersonProcess(0, 5)
peterson2 = PetersonProcess(1, 5)
peterson3 = PetersonProcess(2, 5)

print("Result from peterson1: {}\nResult from peterson2: {}".format(
    peterson1.get_result(),
    peterson2.get_result()
))

peterson1.start()
peterson2.start()
peterson3.start()

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