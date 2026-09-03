"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。

Todo:
  - ジャンル、プレイ人数、プレイ時間の入力
"""
import json
from pathlib import Path
import streamlit as st

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

def input_to_search() -> dict[str, Any]:
    """ゲームの絞り込みをするための条件(ジャンル、プレイ人数、プレイ時間)入力"""
    with st.form("is"):
        genre = st.selectbox("ジャンルを選んでください",[None,"協力","対戦","パズル","運"])
        players  = st.selectbox("プレイ人数を選択してください(人)", [None]+list(range(1,21)))
        play_time = st.slider("プレイ時間を選択してください(分)", 0, 240, None)
        if st.form_submit_button("送信"):
            return {"genre":genre, "players":players, "play_time":play_time}

def display(datas:dict[str, dict[str, Any]]) -> None:
    """データの表示、テスト用で画像表示なし"""
    for inf in datas.values():
        print(inf["title"])
        print(f"{inf['min_players']} ~ {inf['max_players']} 人")
        print(f"{inf['min_play_time']} ~ {inf['max_play_time']} 分")
        print()

def main():
    st.title("ボードゲーム検索アプリ")
    condition = input_to_search()
    st.write(condition)

if __name__ == "__main__":
    main()
    
