from abc import ABC, abstractmethod
from src.domain.command import Command
from src.domain.command_response import CommandResponse


class CommandHandler(ABC):

    @abstractmethod
    def process(self, command: Command) -> CommandResponse:
        pass
