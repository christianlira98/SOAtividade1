from bean.Process import Process

number_of_processes = 5

level_of_process = [-1 for k in range(number_of_processes)]
last_to_enter = [0 for k in range(number_of_processes)]

shared_global_variable = 0


class PetersonProcess(Process):

    STATE_RUNNING = "running"
    STATE_WAITING = "waiting"
    STATE_STOPPED = "stopped"

    def __init__(self, process_id, iterations=5):
        global level_of_process, last_to_enter
        level_of_process = [-1 for k in range(number_of_processes)]
        last_to_enter = [0 for k in range(number_of_processes)]
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

            print(f"{repr(self)} busy wait")

    def unlock(self):
        global level_of_process
        actual_process_number = self.process_id

        level_of_process[actual_process_number] = -1

    def critical_region(self):
        global shared_global_variable
        shared_global_variable += 1

    def run(self):
        self.process_state = PetersonProcess.STATE_RUNNING
        for k in range(self.iterations):
            self.lock()
            print(f"{repr(self)} entrando na Região Crítica")
            self.critical_region()
            print(f"{repr(self)} saindo da Região Crítica")
            self.unlock()
        self.process_state = PetersonProcess.STATE_STOPPED

    def get_result(self):
        global shared_global_variable
        return shared_global_variable

    def is_running(self):
        return self.process_state == PetersonProcess.STATE_RUNNING