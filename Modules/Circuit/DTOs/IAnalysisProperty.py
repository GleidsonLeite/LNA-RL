from abc import ABC, abstractmethod
import numpy as np


class IAnalysisProperty(ABC):
    @abstractmethod
    def as_ndarray(self) -> np.ndarray:
        raise NotImplementedError
