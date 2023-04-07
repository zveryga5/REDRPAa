from abc import ABC, abstractmethod


class AbstractScenarioAPI(ABC):

    @abstractmethod
    def CV_scan(self):
        pass

    @abstractmethod
    def click_on_object(self, _object):
        pass

    @abstractmethod
    def hover_on_object(self, _object):
        pass

    @abstractmethod
    def double_click_on_object(self, _object):
        pass

    @abstractmethod
    def r_click_on_object(self, _object):
        pass

    @abstractmethod
    def double_r_click_on_object(self, _object):
        pass

    @abstractmethod
    def move_to_object(self, _object):
        pass

    @abstractmethod
    def move_window(self, points):
        pass

    @abstractmethod
    def close_window(self):
        pass

    @abstractmethod
    def focus_window(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def input_text(self, text):
        pass
