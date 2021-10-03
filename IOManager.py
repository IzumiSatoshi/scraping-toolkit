"""
スクレイピング結果のインプット、アウトプットを担当
"""
import os

import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def read(path):
    """
    出力先ファイルのパスの拡張子から、出力ファイル形式を自動で判断する。
    失敗したらNoneが返される
    エラーハンドリングが微妙かも
    """
    extension = os.path.splitext(path)[-1]

    df = None

    if extension == '.xlsx':
        df = pd.read_excel(path)
    elif extension == '.csv':
        df = pd.read_csv(path)
    else:
        print("未知の拡張子が指定されました。")
        raise ValueError

    return df


def write(df, path):
    """
    出力先ファイルのパスの拡張子から、出力ファイル形式を自動で判断する。
    エラーハンドリングが微妙かも
    """
    extension = os.path.splitext(path)[-1]

    if extension == ".xlsx":
        write_as_xlsx(df, path)
    elif extension == ".csv":
        write_as_csv(df, path)
    else:
        print("未知の拡張子が指定されました。保存できません。")
        raise ValueError


def write_as_xlsx(df, path):
    """
    dfをエクセルファイルに出力する
    """
    wb = Workbook()
    ws = wb.active

    # dfをシートに追加していく
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)

    wb.save(path)


def write_as_csv(df, path):
    """
    dfをcsvファイルに出力する
    """
    df.to_csv(path, index=False)


def check_file_access(path) -> bool:
    """
    指定されたファイルの読み書きができるかを確認
    """
    df = pd.DataFrame()

    try:
        df = read(path)
    except:
        return False

    try:
        write(df, path)
    except:
        return False

    return True
