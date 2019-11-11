#Implementação do escalonador SSTF

"""
Autores: Christian Lira, Jonas Freire;
"""


class Disk():

    def __init__(self, disk_positions):
        self.disk_positions_array = [i for i in range(disk_positions)]


def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))

def takeSecondElement(elem):
    return elem[1]

def sstf(request_sequence, initial_head_pos, disk):
    seek_sequence = []
    current_track = initial_head_position
    seek_operations = 0
    #ordenando a lsita de requisições pela distancia da cabeça
    novas_posicoes = []
    sorted_requests = sorted(request_sequence, key = takeSecondElement)
    request_sequence = [i for (i,j) in sorted_requests]


    i = 0
    array_positions = disk.disk_positions_array
    while i < len(sorted_requests):
        index = initial_head_pos + sorted_requests[i][1]
        pos = None
        if(index > len(array_positions)):
            pos = -1
        else:
            pos = array_positions[index]
        if pos in request_sequence:
            seek_operations += abs(current_track - array_positions[i])
            current_track = array_positions[i]
            seek_sequence.append(array_positions[i])
        else:
            index = array_positions[initial_head_pos - sorted_requests[i][1]]
            if (index < 0):
                pos = -1
                i += 1
                continue

            pos = array_positions[index]
            seek_operations += abs(current_track - array_positions[i])
            current_track = array_positions[i]
            seek_sequence.append(array_positions[i])
        i += 1

    print("Seek sequence is: ")
    print(seek_sequence)
    print("Total number of seek operations: "+str(seek_operations))


if __name__ == '__main__':

    disk_positions = int(input("Enter the number of disk positions: "))
    #inicializando o disco.
    disk = Disk(disk_positions)
    while True:
        requests = input("Enter the request sequence separated by comma: ")
        requests = requests.split(',')
        requests = [int(i) for i in requests]
        aux = requests.copy()
        aux.sort()
        if(aux[0] >= 0 and aux[len(aux) - 1] < disk_positions):
            break
        else:
            print(f"Sorry, you have to enter numbers between 0 and {disk_positions - 1}")
    while True:
        initial_head_position = int(input("Enter the initial head position: "))
        if(initial_head_position >= 0 and initial_head_position < disk_positions):
            for i in range(len(requests)): #transformando a lista de requests numa tupla com a primeira posição sendo o request, e a segunda a distancia da requisição para a cabeça inicial.
                for z in range(len(disk.disk_positions_array)):
                    requests[i] = (requests[i], abs(initial_head_position - requests[i))
            break
        else:
            print(f"Sorry the initial position must be between 0 and {disk_positions - 1}")

    sstf(requests, initial_head_position, disk)
