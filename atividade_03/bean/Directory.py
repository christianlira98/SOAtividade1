from atividade_03.bean.File import File


class Directory:

    def __init__(self, directory_name, constants, father=None):
        self.directory_name = directory_name
        self.father = father
        self.directories = []
        self.files = []
        self.constantes = constants
        self.bit_map_table = constants.BIT_MAP_TABLE  # ponteiro para o bitmap_table
        self.file_allocation_table = constants.FILE_ALLOCATION_TABLE  # ponteiro para a file_allocation_table
        self.block_size = constants.CONST_BLOCK_SIZE

    def __repr__(self):
        return f"Directory {self.directory_name} son of {self.father}"

    def list_directory(self):
        print(25 * '=')
        print('Directory ->', self.directory_name)
        print('%-5s %-20s' % ('size', 'filename/dirname'))
        print(25 * '-')
        if len(self.files) == 0 and len(self.directories) == 0:
            print('Empty Directory')
        else:
            if len(self.files) > 0:
                for file in self.files:
                    print('%-5d %-20s' % (file.file_size, file.file_name))
            if len(self.directories) > 0:
                for directory in self.directories:
                    print('%-15s %-20s' % ('', directory.directory_name))
        print(25 * '-')
        print('Total:', len(self.files) + len(self.directories))

    def add_sub_directory(self, directory):

        for direc in self.directories:
            if direc.directory_name == directory.directory_name:
                print("Já existe um diretório com esse nome.")
                return

        self.directories.append(directory)

    #tinha esquecido de desalocar todos os arquivos dentro do diretório que vai ser apagado.
    #algoritmo recursivo para fazer isso.
    def delete_sub_directory(self, directory):

        for file in directory.files[::-1]:
            directory.remove_file(file)

        #Condição de parada.
        if(len(directory.directories) == 0):
            self.directories.remove(directory)
            return
        # iterando de forma reversa, pq estou excluindo os itens da lista
        #Em tempo de excução no if da condição de parada.
        #E isso sendo iterado da forma convencional daria problema pois quando fosse excluido, os elementos posteriores da lista teriam
        # seu index atualizado, e fazendo isso da forma reversa os indices permanecem os mesmos.
        #E a função consegue realizar o trabalho direito.
        for direc in directory.directories[::-1]:
            directory.delete_sub_directory(direc)




    """
    Assumindo que file_size sempre venha em MB
    o retorno é um booleano dizendo se tem a quantidade de blocos disponivel
    e tambem quantos blocos sao.
    :param file_size: tamanho do arquivo em MB 
    :return: booleano informando se existem blocos disponiveis suficientes, e quantidade de blocos necessarios
    """
    def is_available_space(self, file_size):
        # Conversão para bits pois o padrão para o tamanho do bloco está em bits
        # Nesse caso é feita a conversão direta de MB para bits e adicionado o tamanho de mais 1 bloco.
        # pois esse bloco extra é preciso para estar no file_allocation_table e guardar os blocos
        # que serão usados nesse file.
        bit_size = (file_size * (2**20) * 8) + self.block_size
        aux_counter = 0.0
        for key, value in self.bit_map_table.items():
            if value == 0:
                aux_counter += key.block_size
            if aux_counter >= bit_size:
                break
        return aux_counter >= bit_size, aux_counter/self.block_size

    """
    O objetivo eh fazer o controle dos blocos bem como dos indices
    E supondo que o file_size sempre seja dado em MB.
    E o tamanho do bloco seja em KB.
    :param file_size: 
    :param file_name: 
    :return: 
    """
    def create_file(self, file_size, file_name):
        is_block_available, block_qtd = self.is_available_space(file_size)

        for file in self.files:
            if file.file_name == file_name:
                print("Já existe um arquivo com esse nome.")
                return

        if not is_block_available:
            print("Não foi possível criar o arquivo")
            return
        file = File(self.constantes.CONT_ID_FILE, file_size, file_name)
        self.constantes.CONT_ID_FILE += 1
        index_list = []  # essa lista auxiliar de acordo com o slide 48 (slide: sistemas de arquivos)
        for key, value in self.bit_map_table.items():
            if value == 0 and block_qtd != 1:
                self.bit_map_table[key] = 1  # setando como bloco usado
                index_list.append(key)
                block_qtd -= 1
            elif value == 0 and block_qtd == 1:
                # esse if eh para o bloco que sera usado para armazenar os outros blocos que foram usados
                # para alocar esse file
                # como no slide 48
                self.bit_map_table[key] = 1  # setando como bloco usado
                key.index_list = index_list  # setando a lista de blocos com os dados desse file.
                self.file_allocation_table[file.file_id] = key
                break
        self.files.append(file)

    def remove_file(self, file):
        index_block = self.file_allocation_table.get(file.file_id)
        index_list = index_block.index_list
        for i in index_list:
            self.bit_map_table[i] = 0  # setando como vago
        self.bit_map_table[index_block] = 0
        index_block.index_list.clear()
        del self.file_allocation_table[file.file_id]  # deletando ele do file_allocation_table
        self.files.remove(file)



