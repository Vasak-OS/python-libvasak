import gi

gi.require_version('Gtk', '3.0')
from functools import lru_cache as cache
from gi.repository import Gtk
import os


class VSKIconManager:
    def __init__(self):
        self.EXTENSIONS = (".png", ".svg", ".jpg", ".jpeg", ".gif", ".webp")
        self.SIZES = (64, 48, 32, 24)
        self.missing_icon = "image-missing"

    @cache(maxsize=None)
    def not_found(self, icon_name):
        print(f"Icon not found: {icon_name}")
        return self.get_icon(self.missing_icon)

    @cache(maxsize=None)
    def get_icon(self, icon: str) -> str:
        """
        :param icon:
        :return: icon name and path
        """
        if icon is None:
            icon = self.not_found(icon)

        if icon.endswith(self.EXTENSIONS):
            # if image has full icon path return icon.
            if icon.startswith("/"):
                return icon
            # if image has icon name and extension, but no path.
            else:
                for ext in self.EXTENSIONS:
                    if icon.endswith(ext):
                        icon = icon.replace(ext, '')

        icon_theme = Gtk.IconTheme.get_default()

        if not icon_theme.has_icon(icon):
            # check for icon in pixmaps directory.
            pixmaps = f"/usr/share/pixmaps/{icon}"
            for ext in self.EXTENSIONS:
                if os.path.isfile(f"{pixmaps}{ext}"):
                    return f"{pixmaps}{ext}"

        for size in self.SIZES:
            icon_name = icon_theme.lookup_icon(icon, size, 0)
            if icon_name:
                return icon_name.get_filename()

        icon = self.not_found(icon)

        return icon
