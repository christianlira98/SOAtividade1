#Classe representando um processo.

from bean.Enum_Priority import enum
class Process():

    def __init__(self, process_id, priority = 1, process_state="ready"):
        self.process_id = process_id
        self.process_state = process_state
        self.priority = 1 and priority # 1 significa low e 0 significa high

    def __repr__(self):
        priority_aux = None
        if self.priority == 0:
            priority_aux = "HIGH"
        elif self.priority == 1:
            priority_aux = "LOW"
        return "Process({}, {}, {})".format(self.process_id, self.process_state, priority_aux)

    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

