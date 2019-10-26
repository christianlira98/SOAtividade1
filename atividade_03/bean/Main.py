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
from atividade_03.bean.Block import Block
from atividade_03.bean.GLOBAL import GLOBAL
from atividade_03.bean.Directory import Directory

if __name__ == '__main__':

    CONT_ID_FILE = 1

    CONST_BLOCK_SIZE = 2**14 # 16384 bits que é igual a 2048 KB (aproximadamente 2KB)

    #instanciando o dict
    FILE_ALLOCATION_TABLE = dict()

    #Mapa de bits
    #Key o objeto do bloco #value (0 ou 1) 0 - para bloco vago - 1 - para bloco ocupado.
    #exatamente como uma alocaçao utilizando bitmap funciona.

    BIT_MAP_TABLE = dict()

    constantes = GLOBAL(CONT_ID_FILE, CONST_BLOCK_SIZE, FILE_ALLOCATION_TABLE, BIT_MAP_TABLE)
    ##Lista inicializando blocos de 2KB cada
    ##Inicializando 100MB de blocos o que dá basicamente 50 000 blocos.

    for i in range(50000):
        block = Block(constantes.CONST_BLOCK_SIZE, i)
        constantes.BIT_MAP_TABLE[block] = 0 #colocando no bitmap como livre.


    new_directory = Directory('home', constantes)
    new_directory.list_directory()
    new_directory.create_file(2, 'test.txt')
    new_directory.create_file(4, 'README.md')
    new_directory.create_file(2, 'movie.mp4')
    new_directory.list_directory()













