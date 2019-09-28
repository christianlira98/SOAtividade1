import time
import random

from threading import Lock, Thread

from bean.Process import Process


lock_to_print = Lock()

actual_time = 0


def output(msg):
    global actual_time
    lock_to_print.acquire()
    print(f"{actual_time}s -> {msg}")
    lock_to_print.release()


def display_situation(processes):
    global actual_time
    while True:
        for process in processes:
            output(f"{repr(process)} ------")
        print(40 * '-')
        actual_time += 1
        time.sleep(1)


class LotteryProcess(Process):

    RUNNING = "running"
    STOPPED = "stopped"

    def __init__(self, process_id, process_state="stopped", tickets=[]):
        Process.__init__(self, process_id=process_id, process_state=process_state)
        self.tickets = tickets
    
    def run(self):
        while True:
            self.wait_by_stopped()
            time.sleep(0.01)

    def wait_by_stopped(self):
        while self.process_state == LotteryProcess.STOPPED:
            time.sleep(0.01)


class LotteryScheduler:

    def __init__(self, number_of_processes=10, quantum=5):
        self.processes = [LotteryProcess(process_id=k) for k in range(number_of_processes)]
        self.quantum = quantum
        self.actual_time = 0
        self.raffled_ticket = 0
        self.distribute_tickets(maximum_number_of_tickets=len(self.processes) * 100)

    def run_scheduler(self):
        for process in self.processes:
            process.start()
        
        while True:
            self.raffle_ticket()
            process_to_be_executed = self.get_raffled_process()
            output(f"{repr(process_to_be_executed)} sorteado")
            self.execute_process(process_to_be_executed)

    def actual_number_of_processes(self):
        return len(self.processes)
    
    def actual_number_of_tickets(self):
        maximum_number_of_tickets = 0
        for process in self.processes:
            maximum_number_of_tickets = max( max(process.tickets), maximum_number_of_tickets )
        return maximum_number_of_tickets
    
    def distribute_tickets(self, maximum_number_of_tickets):
        print(maximum_number_of_tickets)
        ticket_id = 0
        remaining_total_number_of_tickets = maximum_number_of_tickets - self.actual_number_of_processes()
        for process in self.processes:
            if remaining_total_number_of_tickets < 2:
                number_of_tickets_for_that_process = 0
            else:
                number_of_tickets_for_that_process = random.randint(0, remaining_total_number_of_tickets)
            number_of_tickets_for_that_process += 1
            tickets_to_add = []
            for k in range(number_of_tickets_for_that_process):
                tickets_to_add.append(ticket_id)
                ticket_id += 1
            process.tickets = tickets_to_add
            remaining_total_number_of_tickets -= number_of_tickets_for_that_process

    def raffle_ticket(self):
        self.raffled_ticket = random.randint(0, self.actual_number_of_tickets())

    def get_raffled_process(self):
        for process in self.processes:
            minimum_ticket_id = min(process.tickets)
            maximum_ticket_id = max(process.tickets)
            if minimum_ticket_id <= self.raffled_ticket <= maximum_ticket_id:
                return process

    def execute_process(self, process):
        process.process_state = LotteryProcess.RUNNING
        output(f"{repr(process)} iniciando execução")
        time.sleep(self.quantum)
        output(f"{repr(process)} preempção")
        process.process_state = LotteryProcess.STOPPED


number_of_processes = int(input('Número de Processos: '))
quantum = int(input('Valor do quantum: '))

scheduler = LotteryScheduler(number_of_processes=number_of_processes, quantum=quantum)
display = Thread(target=display_situation, args=(scheduler.processes,))
display.start()
scheduler.run_scheduler()