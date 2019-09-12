import time
import random
from bean.Process import Process


#Variáveis globais auxiliares.
process_list = []
counter = 0
turn = -1
shared_variable = 0

class Strict_alternation_process(Process):


    def __init__(self, process_id, priority = 1, process_state="ready"):
        Process.__init__(self, process_id, priority, process_state)

    def run(self):
        global turn, process_list
        while turn != self.process_id:  # enquanto for verdadeiro não entre na região crítica.
            pass
        self.enter_critical_region()
        time.sleep(5)  # espera 5 segundos
        self.leave_critical_region()
        turn = process_list[counter].process_id
        print("==========================\n")

    def enter_critical_region(self):
        global shared_variable

        self.process_state = "running"
        print(f"\nIniciando o {repr(self)}")
        print(f"O {repr(self)} está entrando na região crítica...")

        print(f"\nO {repr(self)} está com o acesso a variavél compartilhada...")
        random.seed(time.time())
        increment = random.randint(0, 10)

        print(f"Valor atual da variável compartilhada: {shared_variable}")
        shared_variable += increment

        print(f"\nO {repr(self)} executou a operação variavel compartilhada + {increment}...")

        print(f"Novo valor da variável compartilhada: {shared_variable}")

    def leave_critical_region(self):
        global counter
        self.process_state = "Stopped"
        print(f"\nO {repr(self)} está saindo da região crítica...")
        counter = (counter + 1) % len(process_list)


if __name__ == "__main__":

    # threads para emular os processos:
    print("Strict Alternation Solution: Christian Lira/Jonas Freire/Pedro Araújo")
    qtd_processos_iniciar = int(input("Quantidade de processos a ser iniciada: "))

    #iniciando os processos
    for i in range(qtd_processos_iniciar): #com cinco elementos a priori
        random.seed(time.time())
        process = Strict_alternation_process(i) #gerando ids aleatórios para os processos.
        process_list.append(process)
        if i == 0:
            turn = process.process_id
        process.start() # inicializando as threads

