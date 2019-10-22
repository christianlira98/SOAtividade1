
class Block:

    def __init__(self, block_address, number_of_sectors): # size of block is 512 Bytes
        self.size_of_block = number_of_sectors
        self.block_address = block_address
