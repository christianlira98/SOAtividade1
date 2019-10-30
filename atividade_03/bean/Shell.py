from atividade_03.bean.Directory import Directory


def ls(actual_directory, arguments=[]):
    if len(arguments) > 1:
        print('Incorrect arguments for ls')
        print('Usage: ls [desired_directory]')
        return
    elif len(arguments) == 1:
        temp_directory = cd(actual_directory, arguments)
        temp_directory.list_directory()
    else:
        actual_directory.list_directory()


def cd(actual_directory, arguments=[]):
    if len(arguments) > 1:
        print('Incorrect arguments for cd')
        print('Usage: cd [desired_directory]')
        return actual_directory
    desired_directory = arguments[0]
    if desired_directory == '.':
        return actual_directory
    elif desired_directory == '..':
        if actual_directory.father is None:  # if is root
            return actual_directory
        return actual_directory.father
    else:
        if actual_directory.exists_directory(desired_directory):
            return actual_directory.get_directory(desired_directory)
        else:
            print("Directory '%s' not found" % desired_directory)
            return actual_directory


def mkdir(actual_directory, arguments=[]):
    if len(arguments) > 1:
        print('Incorrect arguments for mkdir')
        print('Usage: mkdir [directory_name]')
        return
    directory_name = arguments[0]
    actual_directory.add_sub_directory_from_name(directory_name)


def touch(actual_directory, arguments=[]):
    if len(arguments) != 2:
        print('Incorrect arguments for touch')
        print('Usage: touch [file_name] [file_size]')
        return
    file_name = arguments[0]
    if not arguments[1].isdigit():
        print('file_size must be positive integer')
        return
    file_size = int(arguments[1])
    actual_directory.create_file(file_size, file_name)


def rm(actual_directory, arguments=[]):
    if len(arguments) > 1:
        print('Incorrect arguments for rm')
        print('Usage: rm [file_name or directory_name]')
        return
    name = arguments[0]
    # discover if is a file or a directory
    file = actual_directory.get_file(name)
    directory = actual_directory.get_directory(name)
    if file:
        actual_directory.remove_file(file)
    elif directory:
        actual_directory.wrapper_del_sub_directory(directory)
    else:
        print('File or directory not found')
        return


def dump(actual_directory, arguments):
    if len(arguments) > 2:
        print('Incorrect arguments for dump')
        print('Usage: dump [start_block] [end_block]')
        return
    bit_map_table = actual_directory.bit_map_table
    if len(arguments) == 2:
        if not arguments[0].isdigit() or not arguments[1].isdigit():
            print('Incorrect argument')
            return
        start_block = int(arguments[0])
        end_block = int(arguments[1])
    elif len(arguments) == 1:
        if not arguments[0].isdigit():
            print('Incorrect argument')
            return
        start_block = int(arguments[0])
        end_block = len(bit_map_table)
    else:
        start_block = 0
        end_block = len(bit_map_table) -1
    if start_block > end_block:
        return
    print('%-5s %-5s' % ('Block', 'Free'))
    for key, value in bit_map_table.items():
        block = key
        block_id = int(block.block_id)
        if start_block <= block_id < end_block:
            is_available = False
            if value is not None:
                is_available = repr(value)
            print('%-5s %-5s' % (block.block_id, is_available))
