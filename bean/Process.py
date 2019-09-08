#Classe representando um processo.
class Process():

    def __init__(self, process_id, process_state="ready"):
        self.process_id = process_id
        self.process_state = process_state

    def __repr__(self):
        return "Process({}, {})".format(self.process_id, self.process_state)
