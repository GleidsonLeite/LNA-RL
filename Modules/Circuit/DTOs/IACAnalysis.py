from Modules.Circuit.DTOs.IAnalysisProperty import IAnalysisProperty
from typing import Dict
from abc import ABC, abstractproperty


class IACANalysis(ABC):
    @abstractproperty
    def frequency(self) -> IAnalysisProperty:
        raise AttributeError

    @abstractproperty
    def nodes(self) -> Dict[str, IAnalysisProperty]:
        raise AttributeError
