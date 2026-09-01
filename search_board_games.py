"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。

Todo:
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

def display(data:dict[str, dict[str, Any]]) -> None:
    """データの表示、テスト用で画像表示なし"""
    for inf in data.values():
        print(inf["title"])
        print(f"{inf['min_players']} ~ {inf['max_players']} 人")
        print(f"{inf['min_play_time']} ~ {inf['max_play_time']} 分")
        print()

if __name__ == "__main__":
    path="data.json"
    data=load_data(path)
    display(data)
