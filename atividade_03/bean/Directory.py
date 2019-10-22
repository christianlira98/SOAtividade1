from bean.File import File


class Directory:

    def __init__(self, directory_name):
        self.directory_name = directory_name
        self.files = []

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

    def create_file(self, file_size, file_name):
        self.files.append( File(file_size, file_name) )


if __name__ == '__main__':
    new_directory = Directory('home')
    new_directory.list_directory()
    new_directory.create_file(4096, 'test.txt')
    new_directory.create_file(4096, 'README.md')
    new_directory.create_file(4096, 'movie.mp4')
    new_directory.list_directory()

