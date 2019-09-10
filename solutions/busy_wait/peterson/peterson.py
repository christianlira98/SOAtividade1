from bean.Process import Process

number_of_processes = 5

level_of_process = [-1 for k in range(number_of_processes)]
last_to_enter = [0 for k in range(number_of_processes)]

shared_global_variable = 0

class PetersonProcess(Process):

    def __init__(self, process_id, iterations = 5):
        Process.__init__(self, process_id)
        self.iterations = iterations



    def lock(self):
        global level_of_process, last_to_enter
        actual_process_number = self.process_id
        
        for stage_number in range(len(level_of_process)):
            level_of_process[actual_process_number] = stage_number
            last_to_enter[stage_number] = actual_process_number
            self.busy_wait(stage_number, actual_process_number)



    def busy_wait(self, stage_number, actual_process_number):
        global level_of_process, last_to_enter

        while True:
            if last_to_enter[stage_number] != actual_process_number:
                break

            exists_process_with_greater_level = False
            for k in range(len(level_of_process)):
                if k == actual_process_number:
                    continue

                if level_of_process[k] >= level_of_process[actual_process_number]:
                    exists_process_with_greater_level = True
            
            if not exists_process_with_greater_level:
                break
                


    def unlock(self):
        global level_of_process
        actual_process_number = self.process_id

        level_of_process[actual_process_number] = -1



    def critical_region(self):
        global shared_global_variable
        shared_global_variable += 1



    def run(self):
        for k in range(self.iterations):
            self.lock()
            self.critical_region()
            self.unlock()
    

    
    def get_result(self):
        global shared_global_variable
        return shared_global_variable