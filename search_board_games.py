"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。

Todo:
  - ボードゲームに関するデータの書き込み
  - ジャンル、プレイ人数、プレイ時間の入力
  - データの絞り込み
  - データの表示
"""
import json
from pathlib import Path

def load_data(path:str) -> dict[str, dict[str, Any]]:
    """jsonファイルからデータを読み込む"""
    with open(path,"r",encoding = "utf-8") as f:
        data = json.load(f)
    return data

def write_data(path:str, add_id:str, add_data:dict[str, Any]) -> None:
    """jsonファイルにデータを書き込む"""
    data = load_data(path)
    data[add_id] = add_data
    with open(path,"w",encoding = "utf-8") as f:
        json.dump(data, f, ensure_ascii = False, indent=4)
