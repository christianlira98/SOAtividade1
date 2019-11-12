# Implementação do escalonador SSTF
import numpy as np

"""
Autores: Christian Lira, Jonas Freire;
"""


class Disk:

    def __init__(self, disk_positions):
        self.disk_positions_array = [i for i in range(disk_positions)]


def find_closest_position_index(lst, k):
    array = np.array(lst)
    return np.abs(array - k).argmin()


def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))


def take_second_element(elem):
    return elem[1]


def sstf(request_sequence, initial_head_position, disk):
    seek_sequence = []
    actual_head_position = initial_head_position
    while len(request_sequence) > 0:
        # find first most near position
        index_closest_position = find_closest_position_index(request_sequence, actual_head_position)
        # get next position
        next_head_position = request_sequence.pop(index_closest_position)
        # append this position to seek sequence
        seek_sequence.append(next_head_position)
        # set the next head position as actual head position for next iteration
        actual_head_position = next_head_position

    return seek_sequence


if __name__ == '__main__':
    number_of_positions = int(input("Enter the number of disk positions: "))
    # disk initialization
    disk = Disk(number_of_positions)

    while True:
        requests = input("Enter the request sequence separated by comma: ")
        requests = requests.split(',')
        requests = [int(i) for i in requests]
        min_request, max_request = min(requests), max(requests)

        if min_request < 0 or max_request >= number_of_positions:
            print(f'Sorry, you have to enter numbers between 0 and {number_of_positions-1}')
        else:
            break

    head_position = 0
    while True:
        head_position = int(input('Enter the initial head position: '))

        if 0 > head_position >= number_of_positions:
            print(f'Sorry the initial position must be between 0 and {number_of_positions-1}')
        else:
            break

    sstf_sequence = sstf(requests, head_position, disk)
    print('SSTF sequence:')
    print(sstf_sequence)
