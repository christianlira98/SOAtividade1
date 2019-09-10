import threading
import time
import random
from bean.Process import Process

#Variáveis globais auxiliares.
process_list = []
threads = []
counter = 0
turn = -1
shared_variable = 0


def strict_alternation(process):
    global turn, process_list
    while turn != process.process_id: #enquanto for verdadeiro não entre na região crítica.
        pass
    enter_critical_region(process)
    time.sleep(5) #espera 5 segundos
    leave_critical_region(process)
    turn = process_list[counter].process_id
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
    counter = (counter + 1) % len(process_list)

if __name__ == "__main__":

    # threads para emular os processos:
    print("Strict Alternation Solution: Christian Lira/Jonas Freire/Pedro Araújo")
    qtd_processos_iniciar = int(input("Quantidade de processos a ser iniciada: "))

    #iniciando os processos
    for i in range(qtd_processos_iniciar): #com cinco elementos a priori
        random.seed(time.time())
        process = Process(random.randint(0,999999999)) #gerando ids aleatórios para os processos.
        process_list.append(process)
        thread = threading.Thread(target = strict_alternation, args = (process,))
        threads.append(thread) #adicionando os processos.
        if i == 0:
            turn = process.process_id
        thread.start() # inicializando as threads


