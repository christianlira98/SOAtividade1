import threading
import time
import random
from bean.Process import Process

#Variáveis globais auxiliares.
sem = None
shared_variable = 0

def semaphore_emulation(process):
    enter_critical_region(process)
    time.sleep(5)  # espera 5 segundos
    leave_critical_region(process)
    print("==========================\n")

def enter_critical_region(process):
    global shared_variable
    sem.acquire()
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
    process.process_state = "Stopped"
    print(f"\nO {repr(process)} está saindo da região crítica...")
    sem.release()

if __name__ == "__main__":

    # threads para emular os processos:
    print("Mutex Semaphore Solution: Christian Lira/Jonas Freire/Pedro Araújo")
    qtd_processos_iniciar = int(input("Quantidade de processos a ser iniciada: "))

    sem = threading.Semaphore(1) #Mutex

    #iniciando os processos
    for i in range(qtd_processos_iniciar): #com cinco elementos a priori
        random.seed(time.time())
        process = Process(random.randint(0,9000000)) #gerando ids aleatórios para os processos.
        thread = threading.Thread(target = semaphore_emulation, args = (process,))
        thread.start() # inicializando as threads




