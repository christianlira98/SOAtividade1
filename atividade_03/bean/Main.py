#
"""
Importante01
Criação do File Allocation Table
Será representado por um dictionary (não quero criar um objeto (: )

o padrão será assim, key será um id único do file, e o value é um ponteiro para um bloco com a lista de blocos desse file.
de acordo com o slide 48 (slide: sistemas de arquivos)

key - file #value (objeto do tipo AllocationBlock)

Importante02
É importante dizer, que os a estrutura de arquivos será vista como sequencias de bytes! Como visto no slide 13.
Então acho que devemos iniciar uma lista de blocos para representar os espaços  no disco, e a cada file que criarmos,
esses blocos serão utilizados. Podemos utilizar tamanho de bloco padrão de 2KB. e Iniciar 100 MB de blocos.
Não sei se isso é realmente necessário, mas acho que sim pq tem lá no ava isso:
"A cada operação realizada pelo usuário, a alocação deve ser simulada
(não apenas mostrar a interface para o usuário, mas também como ficaria em baixo nível)."
"""
import re

from atividade_03.bean.Block import Block
from atividade_03.bean.GLOBAL import GLOBAL
from atividade_03.bean.Shell import *

constantes = None
actual_directory_address = None


# def op(op, name=None, directory=None, size=None):
#     x = None
#     if name is not None:
#         x = re.findall("[.]", name)
#     file = []
#     direc = []
#
#     if(op == 'mkdir'):
#         return directory.add_sub_directory(Directory(name, constantes, directory))
#     elif(op == '>'):
#         return directory.create_file(size, name)
#     elif(op == 'ls'):
#         return directory.list_directory()
#     if(len(x) > 0 and op == 'rm'):
#         file = [z for z in directory.files if z.file_name == name]
#         if(len(file) > 0):
#             return directory.remove_file(file[0])
#     elif(len(x) == 0 and op == 'rm'):
#         direc = [z for z in directory.directories if z.directory_name == name]
#         if(len(direc) > 0):
#             return directory.wrapper_del_sub_directory(direc[0])
#     elif(op == 'cd'):
#         direc = [z for z in directory.directories if z.directory_name == name]
#         if(len(direc) > 0):
#             index = directory.directories.index(direc[0])
#             return directory.directories[index]
#
#         if(name == ".." and directory.father != None):
#             return directory.father
#         elif (name == ".." and directory.father == None):
#             print("Você já está no diretório raiz")
#             return
#
#     if (( len(file) == 0 or len(direc) == 0) and op == 'rm'):
#         print("Arquivo não encontrado!")
#         return
#     elif (len(direc) == 0 and op == 'cd'):
#         print("Diretório não encontrado!")
#         return


if __name__ == '__main__':

    CONT_ID_FILE = 1

    CONST_BLOCK_SIZE = 2**14 # 16384 bits que é igual a 2048 Bytes (aproximadamente 2KB)

    # instanciando o dict
    FILE_ALLOCATION_TABLE = dict()

    # Mapa de bits
    # Key o objeto do bloco #value (0 ou 1) 0 - para bloco vago - 1 - para bloco ocupado.
    # exatamente como uma alocacao utilizando bitmap funciona.

    BIT_MAP_TABLE = dict()

    constantes = GLOBAL(CONT_ID_FILE, CONST_BLOCK_SIZE, FILE_ALLOCATION_TABLE, BIT_MAP_TABLE)
    # Lista inicializando blocos de 2KB cada
    # Inicializando 100MB de blocos o que da basicamente 50 000 blocos.
    for i in range(50000):
        block = Block(constantes.CONST_BLOCK_SIZE, i)
        constantes.BIT_MAP_TABLE[block] = 0  # colocando no bitmap como livre.

    print("\t\t\t\t\t"+28*"*")
    print("\t\t\t\t\t\t"+"Sistema de Arquivos")
    print("\t\t\t\t\t" + 28 * "*")

    actual_directory = Directory('root', constantes)
    while True:
        q = input(actual_directory.get_path() + "$: ")
        q = q.lstrip(" ")
        q = q.rstrip(" ")
        option = re.split(r'[\s]', q)

        command = option[0]
        arguments = option[1:]

        if command == 'exit':
            break
        elif command == 'ls':
            ls(actual_directory, arguments)
        elif command == 'cd':
            actual_directory = cd(actual_directory, arguments)
        elif command == 'touch':
            touch(actual_directory, arguments)
        elif command == 'rm':
            rm(actual_directory, arguments)
        elif command == 'mkdir':
            mkdir(actual_directory, arguments)
