from abc import ABC, abstractmethod


class INGSPICE(ABC):
    @abstractmethod
    def remove_circuit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def destroy(self) -> None:
        raise NotImplementedError
