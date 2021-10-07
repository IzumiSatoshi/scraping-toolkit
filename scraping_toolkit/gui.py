import PySimpleGUI as sg
from tkinter import messagebox

"""
コンポーネントの関数名はPythonの命名方法とかは無視して、Reactに寄せた書き方にしてみる。
パフォーマンスに問題があるかは分からん。
あんまり具体的すぎるコンポーネントを追及するのはやめようかな。切りがないし。
"""


def show_error(text):
    messagebox.showerror("エラー", text)


def ButtonLarge(text, key):
    button_style = {
        'font': ("", 20),
        'pad': (0, (0, 20))
    }
    return (
        [sg.Stretch(), sg.Button(text, key=key, **button_style), sg.Stretch()],
    )


def FileSelector(text, key):
    pad = (5, (0, 30))
    return (
        [sg.Text(text)],
        [sg.InputText(key=key, pad=pad, expand_x=True),
         sg.FileBrowse('選択', pad=pad)],
    )


def FolderSelector(text, key):
    pad = (5, (0, 30))
    return (
        [sg.Text(text)],
        [sg.InputText(key=key, pad=pad, expand_x=True),
         sg.FolderBrowse('選択', pad=pad)],
    )


def InputTextWithText(text, key, default=None):
    pad = (5, (0, 30))
    return (
        [sg.Text(text)],
        [sg.InputText(key=key, font=("", 12, "bold"),
                      default_text=default, pad=pad)]
    )


def ProgressBarWithText(text, text_key, bar_key, default_visible):
    pad = ((5, 5), (0, 30))
    return (
        [sg.Text(text, key=text_key, visible=default_visible,
                 expand_x=True)],
        [sg.ProgressBar(100, size=(40, 20), key=bar_key,
                        pad=pad, visible=default_visible)]
    )
