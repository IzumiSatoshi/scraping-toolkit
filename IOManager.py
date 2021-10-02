"""
スクレイピング結果のインプット、アウトプットを担当
"""
import os

import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def save(df, path):
    """
    出力先ファイルのパスの拡張子から、出力ファイル形式を自動で判断する。
    """
    extension = os.path.splitext(path)[-1]

    print(extension)
    if extension == ".xlsx":
        save_as_xlsx(df, path)
    elif extension == ".csv":
        save_as_csv(df, path)
    else:
        print("未知の拡張子が指定されました。保存できません。")


def save_as_xlsx(df, path):
    """
    dfをエクセルファイルに出力する
    """
    wb = Workbook()
    ws = wb.active

    # dfをシートに追加していく
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)

    wb.save(path)


def save_as_csv(df, path):
    """
    dfをcsvファイルに出力する
    """
    print('saving')
    df.to_csv(path, index=False)
