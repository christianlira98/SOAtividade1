
class File:

    def __init__(self, file_id, file_size, file_name):
        self.file_id = file_id
        self.file_size = file_size
        self.file_name = file_name

    def __repr__(self):
        return f"File {self.file_name} id {self.file_id} size {self.file_size}"
