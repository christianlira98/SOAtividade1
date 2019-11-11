#Implementação do escalonador LOOK

"""
Autores: Christian Lira, Jonas Freire;
"""


class Disk():

    def __init__(self, disk_positions):
        self.disk_positions_array = [i for i in range(disk_positions)]


def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))

def look(request_sequence, initial_head_pos, initial_direction, disk):
    seek_sequence = []
    current_track = initial_head_position
    seek_operations = 0
    if(initial_direction == 'R'):
        array_positions = disk.disk_positions_array
        pos = -1
        for i in range(initial_head_position, len(array_positions), 1):
            if array_positions[i] in request_sequence:
                request_sequence.remove(array_positions[i]) # tirando elemento já encontrado da lista.
                if(array_positions[i] not in seek_sequence):
                    seek_operations += abs(current_track - array_positions[i])
                    current_track = array_positions[i]
                    seek_sequence.append(array_positions[i])

            #Olha para frente verificando se há elementos requisitados na frente do disco, se não tiver começa a verificar
            #para o outro lado.

            array_intersection = intersection(array_positions[i: len(array_positions)], request_sequence)
            if(len(array_intersection) == 0): #Não há mais elementos requisitados nessa direção.
                pos = i
                break

        for i in range(pos, -1, -1):
            if array_positions[i] in request_sequence:
                request_sequence.remove(array_positions[i])  # tirando elemento já encontrado da lista.
                if (array_positions[i] not in seek_sequence):
                    seek_operations += abs(current_track - array_positions[i])
                    current_track = array_positions[i]
                    seek_sequence.append(array_positions[i])

            # Olha para frente verificando se há elementos requisitados na frente do disco, se não tiver para.

            array_intersection = intersection(array_positions[0: i], request_sequence)
            if (len(array_intersection) == 0):  # Não há mais elementos requisitados nessa direção.
                break
    else:
        array_positions = disk.disk_positions_array
        pos = -1
        for i in range(initial_head_position, -1, -1):
            if array_positions[i] in request_sequence:
                request_sequence.remove(array_positions[i])  # tirando elemento já encontrado da lista.
                if (array_positions[i] not in seek_sequence):
                    seek_operations += abs(current_track - array_positions[i])
                    current_track = array_positions[i]
                    seek_sequence.append(array_positions[i])

            # Olha para frente verificando se há elementos requisitados na frente do disco, se não tiver começa a verificar
            # para o outro lado.

            array_intersection = intersection(array_positions[0: i], request_sequence)
            if (len(array_intersection) == 0):  # Não há mais elementos requisitados nessa direção.
                pos = i
                break

        for i in range(pos, len(array_positions), 1):
            if array_positions[i] in request_sequence:
                request_sequence.remove(array_positions[i])  # tirando elemento já encontrado da lista.
                if (array_positions[i] not in seek_sequence):
                    seek_operations += abs(current_track - array_positions[i])
                    current_track = array_positions[i]
                    seek_sequence.append(array_positions[i])

            # Olha para frente verificando se há elementos requisitados na frente do disco, se não tiver para.

            array_intersection = intersection(array_positions[i: len(array_positions)], request_sequence)
            if (len(array_intersection) == 0):  # Não há mais elementos requisitados nessa direção.
                break
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
            break
        else:
            print(f"Sorry the initial position must be between 0 and {disk_positions - 1}")
    while True:
        initial_direction = input("Enter the initial direction R for right L for left: ")
        if (initial_direction == 'L' or initial_direction == 'R'):
            break

    look(requests, initial_head_position, initial_direction, disk)










