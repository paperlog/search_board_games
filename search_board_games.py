"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。

Todo:
  - ジャンル、プレイ人数、プレイ時間の入力
  - データの絞り込み
"""
import json
from pathlib import Path

def load_datas(path:str) -> dict[str, dict[str, Any]]:
    """jsonファイルからデータを読み込む"""
    with open(path,"r",encoding = "utf-8") as f:
        datas = json.load(f)
    return datas

def write_datas(path:str, add_id:str, add_data:dict[str, Any]) -> None:
    """jsonファイルにデータを書き込む"""
    datas = load_datas(path)
    datas[add_id] = add_data
    with open(path,"w",encoding = "utf-8") as f:
        json.dump(datas, f, ensure_ascii = False, indent=4)

def game_filter(datas:dict[str, dict[str, Any]], genre:str, players:int, play_time:int) -> dict[str, list[dict[str, Any]]]:
    """条件によってゲームを絞り込む"""
    perfect=[] #max<条件
    good=[] #min<条件
    for id,data in datas.items():
        judge=0
        if genre!=None:
            if genre  not in data["genre"]:
                continue
        if players!=None:
            if data["min_players"] <= players <= data["max_players"]:
                judge+=1
        if play_time!=None:
            if play_time>=data["max_play_time"]:
                judge+=100
            elif play_time>=data["min_play_time"]:
                judge+=10
        if judge//100==1 and judge%100==1:
            perfect.append(data)
        elif judge//10==1 and judge%10==1:
            good.append(data)
    return {"perfect":perfect, "good":good}

def display(datas:dict[str, dict[str, Any]]) -> None:
    """データの表示、テスト用で画像表示なし"""
    for inf in datas.values():
        print(inf["title"])
        print(f"{inf['min_players']} ~ {inf['max_players']} 人")
        print(f"{inf['min_play_time']} ~ {inf['max_play_time']} 分")
        print()

if __name__ == "__main__":
    path="data.json"
    datas=load_datas(path)
    display(datas)
