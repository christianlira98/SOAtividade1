
class Block():

    def __init__(self, block_size, block_id):
        self.block_size = block_size
        self.block_id = block_id


class AllocationBlock(Block):

    def __init__(self, block_size, block_id, block_list = []):
        super().__init__(block_size, block_id)
        self.block_list = block_list #ponteiro para os blocos do file.
