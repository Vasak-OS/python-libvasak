import os

def list_windows():
    windows = []

    try:
        import Xlib.display
        # Try to use Xlib to list windows (for Xorg)
        display = Xlib.display.Display()
        root = display.screen().root
        window_list = root.query_tree().children
        windows.extend(window_list)
    except Xlib.error.XauthError:
        pass  # Ignore XauthError when running on Wayland



    return windows

if __name__ == "__main__":
    windows = list_windows()
    for window in windows:
        window_name = window.get_wm_name() if hasattr(window, 'get_wm_name') else None
        if window_name:
            print(f"Window: {window_name}")
        else:
            print("Window with no title")
