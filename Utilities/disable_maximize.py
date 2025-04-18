import ctypes
import win32con
import win32gui

def disable_maximize():
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd:
        current_style = ctypes.windll.user32.GetWindowLongW(hwnd, win32con.GWL_STYLE)
        new_style = current_style & ~win32con.WS_MAXIMIZEBOX & ~win32con.WS_THICKFRAME
        ctypes.windll.user32.SetWindowLongW(hwnd, win32con.GWL_STYLE, new_style)
        ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0,
                                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE |
                                          win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED)

disable_maximize()
