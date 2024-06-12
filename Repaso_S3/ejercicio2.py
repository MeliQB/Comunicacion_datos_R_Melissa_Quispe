import os

class FileStorage:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)

    def write(self, path, data):
        file_path = os.path.join(self.root_dir, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file:
            file.write(data)

    def read(self, path):
        file_path = os.path.join(self.root_dir, path)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                return file.read()
        else:
            return None

class VersionedFileStorage(FileStorage):
    def __init__(self, root_dir):
        super().__init__(root_dir)
        self.permissions = {}
        self.file_versions = {}

    def set_permission(self, path, permission):
        self.permissions[path] = permission

    def write_versioned(self, path, data):
        if path not in self.file_versions:
            self.file_versions[path] = []
        self.file_versions[path].append(data)
        self.write(path, data)

    def read_version(self, path, version):
        if path in self.file_versions and version < len(self.file_versions[path]):
            return self.file_versions[path][version]
        else:
            return None

    def read(self, path):
        if path in self.permissions and self.permissions[path] == 'read':
            return super().read(path)
        else:
            return None

    def write(self, path, data):
        if path in self.permissions and self.permissions[path] == 'write':
            return super().write(path, data)
        else:
            return None

# Ejemplo de uso
file_storage = VersionedFileStorage('storage')
file_storage.set_permission('file1.txt', 'read')
file_storage.write_versioned('file1.txt', b'Version 1')
file_storage.write_versioned('file1.txt', b'Version 2')
print(file_storage.read('file1.txt'))  # Output: b'Version 2'
print(file_storage.read_version('file1.txt', 0))  # Output: b'Version 1'
file_storage.set_permission('file1.txt', 'write')
file_storage.write('file1.txt', b'Version 3')
print(file_storage.read('file1.txt'))  # Output: b'Version 3'
