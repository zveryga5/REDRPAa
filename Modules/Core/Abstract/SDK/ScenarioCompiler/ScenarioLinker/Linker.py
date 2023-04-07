from abc import ABC, abstractmethod


class AbstractScenarioLinker(ABC):

    @abstractmethod
    def link_names(self):
        pass
