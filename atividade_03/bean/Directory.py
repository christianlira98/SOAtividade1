from atividade_03.bean import File


class Directory:

    def __init__(self, directory_name, bit_map_table, file_allocation_table, block_size):
        self.directory_name = directory_name
        self.files = []
        self.bit_map_table = bit_map_table #ponteiro para o bitmap_table
        self.file_allocation_table = file_allocation_table #ponteiro para a file_allocation_table
        self.block_size = block_size

    def list_directory(self):
        print(25 * '=')
        print('Directory ->', self.directory_name)
        print('%-5s %-20s' % ('size', 'filename'))
        print(25 * '-')
        if len(self.files) > 0:
            for file in self.files:
                print('%-5d %-20s' % (file.file_size, file.file_name))
        else:
            print('Empty Directory')
        print(25 * '-')
        print('Total:', len(self.files))

    #Assumindo que file_size sempre venha em MB
    def is_available_space(self, file_size):
        #Conversão para bits pois o padrão para o tamanho do bloco está em bits
        #Nesse caso é feita a conversão direta de MB para bits e adicionado o tamanho de mais 1 bloco.
        #pois esse bloco extra é preciso para estar no file_allocation_table e guardar os blocos que serão usados nesse file.
        bit_size = file_size * 8000000 + self.block_size

        aux_counter = 0.0
        for key, value in self.bit_map_table.items():
            if(value == 0):
                aux_counter += key.block_size
            # 1 KB  == 0.001 MB
            if(aux_counter * 0.001 >= bit_size):
                break
        return aux_counter * 0.001 >= bit_size


    #O objetivo é fazer o controle dos blocos bem como os índices
    #E supondo que o file_size sempre seja dado em MB.
    #E o tamanho do bloco seja em KB.
    def create_file(self, file_size, file_name):
        is_block_available = self.is_available_space(file_size)
        if(is_block_available == False):
            print("Não foi possível criar o arquivo")

        self.files.append( File(file_size, file_name) )


if __name__ == '__main__':
    new_directory = Directory('home')
    new_directory.list_directory()
    new_directory.create_file(4096, 'test.txt')
    new_directory.create_file(4096, 'README.md')
    new_directory.create_file(4096, 'movie.mp4')
    new_directory.list_directory()

