import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck


class WindowsManagerX11:
    def __init__(self):
        pass

    def get_windows(self):
        windows = self.__get_screen().get_windows()

        print(windows)

    def __get_screen(self):
        return Wnck.Screen.get(0)


if __name__ == "__main__":
    wm = WindowsManagerX11()
    wm.get_windows()
