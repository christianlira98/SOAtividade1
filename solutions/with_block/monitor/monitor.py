from threading import Lock


class IntegerMonitor:
    resource = 0

    lock = Lock()

    def set_resource(self, new_value):
        IntegerMonitor.lock.acquire()
        IntegerMonitor.resource = new_value
        IntegerMonitor.lock.release()

    def get_resource(self):
        return IntegerMonitor.resource
        

    def increment_value(self):
        IntegerMonitor.lock.acquire()
        IntegerMonitor.resource += 1
        IntegerMonitor.lock.release()
