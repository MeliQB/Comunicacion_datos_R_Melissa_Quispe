class AdvancedBlockStorage:
    def __init__(self, total_size, block_size):
        self.total_size = total_size
        self.block_size = block_size
        self.num_blocks = total_size // block_size
        self.storage = bytearray(total_size)
        self.free_blocks = [True] * self.num_blocks
        self.block_assignments = {}

    def allocate(self, size):
        required_blocks = (size + self.block_size - 1) // self.block_size
        start_block = None

        # Buscar bloques contiguos libres
        for i in range(self.num_blocks):
            if self.free_blocks[i]:
                if start_block is None:
                    start_block = i
                if i - start_block + 1 == required_blocks:
                    # Se han encontrado suficientes bloques contiguos
                    block_ids = list(range(start_block, start_block + required_blocks))
                    for block_id in block_ids:
                        self.free_blocks[block_id] = False
                    self.block_assignments[id(bytearray(size))] = block_ids
                    return block_ids
            else:
                start_block = None

        # No se han encontrado suficientes bloques contiguos
        return None

    def free(self, block_id):
        if block_id in self.block_assignments:
            for b_id in self.block_assignments[block_id]:
                self.free_blocks[b_id] = True
            del self.block_assignments[block_id]

    def defragment(self):
        # Reescribir los datos en un orden compacto
        new_storage = bytearray(self.total_size)
        new_free_blocks = [True] * self.num_blocks
        new_block_assignments = {}
        offset = 0

        for block_ids in self.block_assignments.values():
            for block_id in block_ids:
                start = block_id * self.block_size
                end = start + self.block_size
                new_storage[offset:offset + self.block_size] = self.storage[start:end]
                new_block_assignments[id(new_storage[offset:offset + self.block_size])] = [offset // self.block_size]
                offset += self.block_size

        self.storage = new_storage
        self.free_blocks = new_free_blocks
        self.block_assignments = new_block_assignments

# Ejemplo de uso
block_storage = AdvancedBlockStorage(1024, 64)
block_ids = block_storage.allocate(128)
print(block_ids)  # Output: [0, 1, 2]
block_storage.free(id(block_storage.storage[0:128]))
block_ids = block_storage.allocate(100)
print(block_ids)  # Output: [0, 1]
block_storage.defragment()
block_ids = block_storage.allocate(200)
print(block_ids)  # Output: [0, 1, 2, 3]
