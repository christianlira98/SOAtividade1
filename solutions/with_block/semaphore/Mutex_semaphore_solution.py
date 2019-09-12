import threading
import time
import random
from bean.Process import Process
from bean.Semaphore import Semaphore


#Variáveis globais auxiliares.
sem = None
shared_variable = 0
lock = threading.Lock()

class Mutex_process(Process):

    def __init__(self, process_id, priority = 1, process_state="ready"):
        Process.__init__(self, process_id, priority, process_state)

    def run(self):
        self.enter_critical_region()
        time.sleep(5)  # espera 5 segundos
        self.leave_critical_region()
        print("==========================\n")

    def enter_critical_region(self):
        global shared_variable, lock

        sem.wait(lock)
        self.process_state = "running"
        print(f"\nIniciando o {repr(process)}")
        print(f"O {repr(self)} está entrando na região crítica...")


        print(f"\nO {repr(self)} está com o acesso a variavél compartilhada...")
        random.seed(time.time())
        increment = random.randint(0, 10)

        print(f"Valor atual da variável compartilhada: {shared_variable}")
        shared_variable += increment

        print(f"\nO {repr(self)} executou a operação variavel compartilhada + {increment}...")

        print(f"Novo valor da variável compartilhada: {shared_variable}")

    def leave_critical_region(self):
        self.process_state = "Stopped"
        print(f"\nO {repr(self)} está saindo da região crítica...")
        sem.done()

if __name__ == "__main__":

    # threads para emular os processos:
    print("Mutex Semaphore Solution: Christian Lira/Jonas Freire/Pedro Araújo")
    qtd_processos_iniciar = int(input("Quantidade de processos a ser iniciada: "))


    sem = Semaphore(1)  # semaforo mutex
    #iniciando os processos
    for i in range(qtd_processos_iniciar): #com cinco elementos a priori
        random.seed(time.time())
        process = Mutex_process(random.randint(0,999999999)) #gerando ids aleatórios para os processos.
        process.start() # inicializando as threads



