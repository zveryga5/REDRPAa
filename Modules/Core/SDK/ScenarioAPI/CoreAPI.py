from Modules.Core.Abstract.SDK.ScenarioAPI.CoreAPI import AbstractScenarioAPI
from Modules.Core.Abstract.OS.Manager.WindowManager import AbstractWindowManager
from Modules.Core.Abstract.OS.Manager.WindowsTools import AbstractWindowsTools


class STDScenarioAPI(AbstractScenarioAPI):

    def __init__(self, win_name, win_helper: AbstractWindowsTools):
        win_desciptor = win_helper.get_window_by_name(win_name)
        window = win_helper.create_window(win_desciptor)
        window_manager = win_helper.create_window_manager(window)
        self._w_manager = window_manager

    def CV_scan(self):
        self._w_manager.cv_scan_for_objects()

    def click_on_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "click")

    def hover_on_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "hover")

    def double_click_on_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "double_click")

    def r_click_on_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "r_click")

    def double_r_click_on_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "double_r_click")

    def move_to_object(self, _object):
        _obj = self._w_manager.find_object(_object)
        self._w_manager.object_action(_obj, "move")

    def get_text(self):
        self._w_manager.object_action("get_text")

    def input_text(self, text):
        self._w_manager.object_action("input_text", text)

    def move_window(self, points):
        self._w_manager.move(points[0], points[1])

    def close_window(self):
        self._w_manager.close()

    def focus_window(self):
        self._w_manager.focus()
