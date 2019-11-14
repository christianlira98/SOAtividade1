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

from atividade_04.RAID.RAID_0.bean.Block import Block
from atividade_04.RAID.RAID_0.bean.GLOBAL import GLOBAL
from atividade_04.RAID.RAID_0.bean.Shell import *
from atividade_04.RAID.RAID_0.bean.Directory import Directory

constantes = None
actual_directory_address = None


if __name__ == '__main__':

    CONT_ID_FILE = 1

    CONST_BLOCK_SIZE = 2**14 # 16384 bits que é igual a 2048 Bytes 2KiB

    # instanciando o dict
    FILE_ALLOCATION_TABLE = dict()

    # Mapa de bits
    # Key o objeto do bloco #value (0 ou 1) 0 - para bloco vago - 1 - para bloco ocupado.
    # exatamente como uma alocacao utilizando bitmap funciona.

    BIT_MAP_TABLE = dict()

    constantes = GLOBAL(CONT_ID_FILE, CONST_BLOCK_SIZE, FILE_ALLOCATION_TABLE, BIT_MAP_TABLE)
    # Lista inicializando blocos de 2KB cada
    # Inicializando 10MB de blocos o que da basicamente 5 000 blocos.
    for i in range(5000):
        block = Block(constantes.CONST_BLOCK_SIZE, i)
        #alterando aqui para None ser o padrão como vazio.
        constantes.BIT_MAP_TABLE[block] = None  # colocando no bitmap como livre.

    print("\t\t\t\t\t"+28*"*")
    print("\t\t\t\t\t\t"+"Sistema de Arquivos")
    print("\t\t\t\t\t" + 28 * "*")

    actual_directory = Directory('root', constantes)
    actual_directory.add_directory_to_bit_map_table(actual_directory)
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
        elif command == 'dump':
            # dump(actual_directory, arguments)
            dump_raid_0(actual_directory, arguments)
        else:
            print('Command not found')
