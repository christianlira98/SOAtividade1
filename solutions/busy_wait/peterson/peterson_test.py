from peterson import PetersonProcess

peterson1 = PetersonProcess(0, 10000)
peterson2 = PetersonProcess(1, 10000)

print("Result from peterson1: {}\nResult from peterson2: {}".format(
    peterson1.get_result(),
    peterson2.get_result()
))