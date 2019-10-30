from datetime import datetime


class File:

    def __init__(self, file_id, file_size, file_name):
        self.file_id = file_id
        self.file_size = file_size
        self.file_name = file_name
        self.creation_date = datetime.now()

    def file_size_in_bytes(self):
        return self.file_size * 2**20   # actually file_size is in MB

    def formatted_creation_date(self):
        return self.creation_date.strftime("%d-%m-%Y %H:%M")

    def __repr__(self):
        return f"(File: {self.file_name} id: {self.file_id} size: {self.file_size} MB)"
