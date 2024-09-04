class CommandPool:
    def __init__(self):
        self.__pool = []

    @property
    def pool(self):
        return self.__pool

    def add(self, command):
        self.__pool.append(command)

    def get_invalid(self) -> list:
        return [cmd for cmd in self.pool if not cmd.is_valid]
