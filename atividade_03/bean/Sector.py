
class Sector:

    def __init__(self, address, size=512):
        self.address = address
        self.size = size
        self.data = []
        for k in range(size):
            self.data.append(0)
