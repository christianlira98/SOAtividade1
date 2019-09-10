import random
import time
import threading
from bean.Process import Process
from bean.Enum_Priority import enum
from queue import PriorityQueue

shared_variable = 0
process_fifo = None

def fifo(process):
    global process_priority_queue, process_fifo

    while process_fifo == None or process.process_id != process_fifo[1].process_id:
        process_fifo = process_priority_queue.queue[0]
        threading.Lock().acquire(timeout=0.25) #bloqueia e verifica a cada 0.25 se pode ser desbloqueada

    enter_critical_region(process)
    time.sleep(5)  # espera 5 segundos
    leave_critical_region(process)

    if not process_priority_queue.empty():
        process_fifo = process_priority_queue.get() #tira da fila.

    print("==========================\n")

def enter_critical_region(process):
    global shared_variable

    process.process_state = "running"
    print(f"\nIniciando o {repr(process)}")
    print(f"O {repr(process)} está entrando na região crítica...")
    time.sleep(0.75)

    print(f"\nO {repr(process)} está com o acesso a variavél compartilhada...")
    time.sleep(0.75)
    random.seed(time.time())
    increment = random.randint(0, 10)

    print(f"Valor atual da variável compartilhada: {shared_variable}")
    time.sleep(0.75)
    shared_variable += increment

    print(f"\nO {repr(process)} executou a operação variavel compartilhada + {increment}...")
    time.sleep(0.75)

    print(f"Novo valor da variável compartilhada: {shared_variable}")

def leave_critical_region(process):
    global counter
    process.process_state = "Stopped"
    print(f"\nO {repr(process)} está saindo da região crítica...")



if __name__ == "__main__":

    # threads para emular os processos:
    print("FIFO with priority scheduler: Christian Lira/Jonas Freire/Pedro Araújo")

    qtd_processos_iniciar = None
    while qtd_processos_iniciar == None or qtd_processos_iniciar < 6:
        qtd_processos_iniciar = int(input("Quantidade de processos a ser iniciada (Obs: >= 6): "))

    qtd_low_priority = round((qtd_processos_iniciar/2)) - 1

    priority_enum = enum(LOW=1, HIGH=0) #a fila é ordenada com 0 sendo a prioridade mais alta e 1 a mais baixa.

    process_priority_queue = PriorityQueue()
    threads = []

    #iniciando os processos
    for i in range(qtd_processos_iniciar): #com cinco elementos a priori
        random.seed(time.time())
        process = None

        if i <= qtd_low_priority:
            process = Process(random.randint(0,999999999), priority = priority_enum.LOW) #gerando ids aleatórios para os processos.
        else:
            process = Process(random.randint(0, 999999999), priority = priority_enum.HIGH)  # gerando ids aleatórios para os processos.

        process_priority_queue.put((process.priority, process))
        thread = threading.Thread(target = fifo, args = (process,))
        threads.append(thread)


    for i in range(qtd_processos_iniciar):
        threads[i].start() # inicializando as threads
