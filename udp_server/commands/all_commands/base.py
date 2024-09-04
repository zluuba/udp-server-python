from abc import ABC, abstractmethod
from typing import Optional

import log


class CommandBase(ABC):
    def __init__(self, tag: Optional[int] = None,
                 name: Optional[str] = None,
                 value: Optional[bytes] = None):

        self._tag = tag
        self._name = name
        self._value = value

        self._is_valid = None

    @property
    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def _validate(self):
        pass

    @property
    def tag(self):
        return self._tag

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def run(self, action: str = 'run_command'):
        if self.is_valid:
            log.write(action, self.name)
