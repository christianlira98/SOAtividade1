from datetime import datetime

from atividade_04.RAID.RAID_1.bean.File import File


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
        self.creation_date = datetime.now()

    @property
    def bit_map_table(self):
        self.bit_map_table_raid_1 = self._bit_map_table.copy()
        return self._bit_map_table

    @bit_map_table.setter
    def bit_map_table(self, bit_map_table):
        self._bit_map_table = bit_map_table
        self.bit_map_table_raid_1 = self._bit_map_table.copy()

    def formatted_creation_date(self):
        return self.creation_date.strftime("%d/%m/%Y %H:%M")

    def __repr__(self):
        if self.father is None:
            return f"(Directory: {self.directory_name} Son of itself)"
        return f"(Directory: {self.directory_name} Son of directory:{self.father.directory_name})"

    def list_directory(self):
        # print(25 * '=')
        print('Directory:', self.directory_name)
        print('%-5s %-15s %-20s %-20s' % ('Type', 'Size', 'Creation', 'Name'))
        # print(25 * '-')
        if len(self.files) == 0 and len(self.directories) == 0:
            print(40*'-')
        else:
            if len(self.files) > 0:
                for file in self.files:
                    creation_date = file.formatted_creation_date()
                    file_size_in_bytes = file.file_size_in_bytes()
                    print('%-5s %-15s %-20s %-20s' % ('f', file_size_in_bytes, creation_date, file.file_name))
            if len(self.directories) > 0:
                for directory in self.directories:
                    creation_date = directory.formatted_creation_date()
                    directory_name = directory.directory_name
                    print('%-5s %-15s %-20s %-20s' % ('d', directory.block_size, creation_date, directory_name))
        # print(25 * '-')
        # print('Total:', len(self.files) + len(self.directories))

    def add_sub_directory(self, directory):
        is_available = self.is_available_space_for_directory()
        if self.exists_file(directory.directory_name):
            print("It already exists a file with this name")
            return
        if self.exists_directory(directory.directory_name):
            print("It already exists a directory with this name")
            return

        if not is_available:
            print("There's no enough space to allocate this repository.")
            return

        self.add_directory_to_bit_map_table(directory)
        self.directories.append(directory)

    def add_sub_directory_from_name(self, directory_name):
        if self.exists_file(directory_name):
            print("It already exists a file with this name")
            return
        if self.exists_directory(directory_name):
            print("It already exists a directory with this name")
            return
        candidate_directory = Directory(directory_name, self.constantes, father=self)
        self.add_sub_directory(candidate_directory)

    def wrapper_del_sub_directory(self, directory):
        self.delete_sub_directory(directory)
        self.directories.remove(directory)
        self.delete_directory_from_bit_map_table(directory)

    def wrapper_del_sub_directory_from_name(self, directory_name):
        directory = self.get_directory(directory_name)
        if directory is None:
            return
        self.delete_sub_directory(directory)
        self.directories.remove(directory)
        self.delete_directory_from_bit_map_table(directory)

    #tinha esquecido de desalocar todos os arquivos dentro do diretório que vai ser apagado.
    #algoritmo recursivo para fazer isso.
    def delete_sub_directory(self, directory):
        # iterando de forma reversa, pq estou excluindo os itens da lista
        #Em tempo de excução
        #E isso sendo iterado da forma convencional daria problema pois quando fosse excluido, os elementos posteriores da lista teriam
        # seu index atualizado, e fazendo isso da forma reversa os indices permanecem os mesmos.
        #E a função consegue realizar o trabalho direito.
        for file in directory.files[::-1]:
            directory.remove_file(file)
        #Condição de parada.
        if(len(directory.directories) == 0):
            return
        for direc in directory.directories[::-1]:
            self.delete_directory_from_bit_map_table(direc)
            directory.delete_sub_directory(direc)
            directory.directories.remove(direc)


    def delete_directory_from_bit_map_table(self, directory):
        for key, value in self.bit_map_table.items():
            if value == directory:
                self.bit_map_table[key] = None  # setando como vago
                break

    def add_directory_to_bit_map_table(self, directory):
        for key, value in self.bit_map_table.items():
            if value is None:
                self.bit_map_table[key] = directory  # setando como ocupado
                break

    """
    Assumindo que file_size sempre venha em MB
    o retorno é um booleano dizendo se tem a quantidade de blocos disponivel
    e tambem quantos blocos sao.
    :param file_size: tamanho do arquivo em MB 
    :return: booleano informando se existem blocos disponiveis suficientes, e quantidade de blocos necessarios
    """
    def is_available_space_for_file(self, file_size):
        # Conversão para bits pois o padrão para o tamanho do bloco está em bits
        # Nesse caso é feita a conversão direta de MB para bits e adicionado o tamanho de mais 1 bloco.
        # pois esse bloco extra é preciso para estar no file_allocation_table e guardar os blocos
        # que serão usados nesse file.
        # bit_size = (file_size * (2**20) * 8) + self.block_size
        bit_size = (file_size * (2 ** 10) * 8) + self.block_size
        aux_counter = 0.0
        for key, value in self.bit_map_table.items():
            if value is None:
                aux_counter += key.block_size
            if aux_counter >= bit_size:
                break
        return aux_counter >= bit_size, aux_counter/self.block_size

    def is_available_space_for_directory(self):
        bit_size = self.block_size
        aux_counter = 0.0
        for key, value in self.bit_map_table.items():
            if value is None:
                aux_counter += key.block_size
            if aux_counter >= bit_size:
                break
        return aux_counter >= bit_size

    """
    O objetivo eh fazer o controle dos blocos bem como dos indices
    E supondo que o file_size sempre seja dado em MB.
    E o tamanho do bloco seja em KB.
    :param file_size: 
    :param file_name: 
    :return: 
    """
    def create_file(self, file_size, file_name):
        is_block_available, block_qtd = self.is_available_space_for_file(file_size)
        if self.exists_file(file_name):
            print("It already exists a file with this name")
            return
        if self.exists_directory(file_name):
            print("It already exists a directory with this name")
            return
        if not is_block_available:
            print("It Wasn't possible to create the file")
            return
        file = File(self.constantes.CONT_ID_FILE, file_size, file_name)
        self.constantes.CONT_ID_FILE += 1
        index_list = []  # essa lista auxiliar de acordo com o slide 48 (slide: sistemas de arquivos)
        for key, value in self.bit_map_table.items():
            if value is None and block_qtd != 1:
                self.bit_map_table[key] = file  # setando como bloco usado
                index_list.append(key)
                block_qtd -= 1
            elif value is None and block_qtd == 1:
                # esse if eh para o bloco que sera usado para armazenar os outros blocos que foram usados
                # para alocar esse file
                # como no slide 48
                self.bit_map_table[key] = file  # setando como bloco usado
                key.index_list = index_list  # setando a lista de blocos com os dados desse file.
                self.file_allocation_table[file.file_id] = key
                break
        self.files.append(file)

    def remove_file(self, file):
        index_block = self.file_allocation_table.get(file.file_id)
        index_list = index_block.index_list
        for i in index_list:
            self.bit_map_table[i] = None  # setando como vago
        self.bit_map_table[index_block] = None
        index_block.index_list.clear()
        del self.file_allocation_table[file.file_id]  # deletando ele do file_allocation_table
        self.files.remove(file)

    def get_path(self):
        list_directories_name = []
        directory = self
        while directory.father is not None:
            list_directories_name.append(directory.directory_name)
            directory = directory.father
        list_directories_name.reverse()
        if len(list_directories_name) == 0:
            return '/'
        path = ''
        for directory_name in list_directories_name:
            path += '/' + directory_name
        return path

    def get_file(self, file_name):
        """
        Get if exists a file from the name
        :param name:
        :return: the file object with this name
        """
        for file in self.files:
            if file.file_name == file_name:
                return file
        return None

    def exists_file(self, name):
        """
        Know if exists a file from the name
        :param name:
        :return: true if exists a file with this name
        """
        return self.get_file(name) is not None

    def exists_directory(self, name):
        """
        Know if exists a directory from the name
        :param name:
        :return: true if exists a directory with this name
        """
        return self.get_directory(name) is not None

    def get_directory(self, directory_name):
        """
        Find a directory object from the directory name
        :param directory_name:
        :return: the directory object, return None if not exists directory with this name
        """
        for directory in self.directories:
            if directory.directory_name == directory_name:
                return directory
        return None


