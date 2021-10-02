import tkinter as tk
from tkinter import Widget, filedialog


class WidgetVar(tk.StringVar):
    """
    Stringだけで大丈夫かな
    tk.StringVar(value='hoge')が長いから、initだけオーバーライドした
    """

    def __init__(self, value=None):
        """
        引数
        value: 初期値（文字列）
        """
        super().__init__(value=value)


class WidgetsHolder:
    """
    gui.Widgetsできれいにそろってるのに、addしなきゃいけないwidgetだけインデントずれるのがちょっと嫌だ
    """

    def __init__(self):
        self.widgets_dict = dict()

    def add(self, widget_name, widget):
        self.widgets_dict[widget_name] = widget

    def get(self, widget_name):
        widget = self.widgets_dict[widget_name]
        return widget


def root(title, geometry):
    """
    tkinterのrootを返す

    引数
    title: ツールの名前
    geometry: 400x400みたいなwindowの大きさ
    """

    root = tk.Tk()
    root.title(title)
    root.geometry(geometry)
    return root


def scraping_start_button(parent, scraping_func):
    """
    スクレイピングを開始する時に押すボタン
    """

    main = button(
        parent=parent,
        button_var=WidgetVar("スクレイピング開始"),
        on_click=scraping_func,
        font=("", 14, "bold")
    )

    return main


def progress_label(parent, progress_var):
    """
    進捗を表示する時に使うラベル
    スクレイピング中のみ表示
    """
    main = label(
        parent=parent,
        label_var=progress_var,
        font=("", 14)
    )
    return main


def entry_with_label(parent, label_var=None, entry_var=None):
    """
    ラベルの下にエントリーがある

    引数
    parent: 親要素(rootなど)
    label_var: Labelに入るテキスト
    entry_var: Entryのウィジェット変数
    """

    # 構築
    main = frame(
        parent=parent,
        pady=10
    )
    title_label(
        parent=main,
        label_var=label_var,
    )
    entry(
        parent=main,
        entry_var=entry_var,
        font=("", 12, "bold"),
        pady=5
    )
    return main


def file_selector(parent, label_var, entry_var):
    """
    ファイル選択ダイアログを出す。
    selector_using_dialogがベースになっている

    引数
    parent: 親
    label_var: タイトル
    entry_var: パスが入るウィジェット変数
    """

    # 関数の定義
    def select_file():
        path = filedialog.askopenfilename()
        entry_var.set(path)

    # 構築
    main = selector_using_dialog(
        parent=parent,
        label_var=label_var,
        entry_var=entry_var,
        select_handler=select_file,
    )
    return main


def folder_selector(parent, label_var, entry_var):
    """
    フォルダ選択ダイアログを出す。
    selector_using_dialogがベースになっている。

    引数
    parent: 親
    label_var: タイトル
    entry_var: パスが入るウィジェット変数
    """

    # 関数の定義
    def select_folder():
        path = filedialog.askopenfilename()
        entry_var.set(path)

    # 構築
    main = selector_using_dialog(
        parent=parent,
        label_var=label_var,
        entry_var=entry_var,
        select_handler=select_folder
    )
    return main


def selector_using_dialog(parent, label_var, entry_var, select_handler):
    """
    参照ボタンを押すと、select_handlerが実行される 

    引数
    parent: 親
    label_var: タイトル
    entry_var: パスが入るウィジェット値
    select_handler: 参照ボタンが押されたら実行される
    """

    # 構築
    main = frame(
        parent=parent,
        pady=10
    )
    title_label(
        parent=main,
        label_var=label_var,
    )
    entry(
        parent=main,
        width=50,
        entry_var=entry_var,
        pack_side=tk.LEFT,
        padx=10
    )
    button(
        parent=main,
        button_var=tk.StringVar(value='参照'),
        on_click=select_handler,
        pack_side=tk.LEFT
    )
    return main


def title_label(parent, label_var):
    title_label = label(
        parent=parent,
        label_var=label_var,
        pady=10
    )
    return title_label


def button(parent, button_var, on_click=None, font=None, pack_side=None):
    button = tk.Button(parent, textvariable=button_var,
                       command=on_click, font=font)
    button.pack(side=pack_side)
    return button


def label(parent, label_var=None, font=None, pady=None, pack_side=None):
    label = tk.Label(parent, textvariable=label_var, font=font, pady=pady)
    label.pack(side=pack_side)
    return label


def entry(parent, entry_var=None, font=None, width=None, padx=None, pady=None, pack_side=None):
    entry = tk.Entry(parent, textvariable=entry_var, font=font, width=width)
    entry.pack(side=pack_side, padx=padx, pady=pady)
    return entry


def frame(parent, padx=None, pady=None):
    frame = tk.Frame(parent, padx=padx, pady=pady)
    frame.pack()
    return frame
