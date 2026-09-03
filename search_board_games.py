"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。

Todo:
  - 複数ジャンルでの検索を可能に(and,orの設定も可能にする？)
  - ジャンルを適切なものに設定
"""
import json
import streamlit as st
import os

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

def game_filter(datas:dict[str, dict[str, Any]], genre:str | None, players:int | None, play_time:int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """条件によってゲームを絞り込む"""
    if genre is None and players is None and play_time == 0:
        return list(datas.values()), []
    perfect = []
    good = []
    for data in datas.values():
        if genre is not None and genre not in data["genre"]:
            continue
        if players is not None:
            if not (data["min_players"] <= players <= data["max_players"]):
                continue
        if play_time != 0:
            if play_time >= data["max_play_time"]:
                perfect.append(data)
            elif play_time >= data["min_play_time"]:
                good.append(data)
        else:
            perfect.append(data)
    return perfect, good

def input_to_search() -> tuple[str | None, int | None, int]:
    """ゲームの絞り込みをするための条件(ジャンル、プレイ人数、プレイ時間)入力"""
    genre = st.selectbox("ジャンルを選んでください",[None,"協力","対戦","パズル","運"])
    players  = st.selectbox("プレイ人数を選択してください(人)", [None]+list(range(1,21)))
    play_time = st.slider("プレイ時間を選択してください(分)", 0, 240, 0)
    return genre, players, play_time

def display(data:dict[str, Any]) -> None:
    """データの表示、テスト用で画像表示なし"""
    with st.container(border=True):
        st.write(data["title"])
        if os.path.isfile(data["img_path"]):
            st.image(data["img_path"], caption = data["title"], width=300)
        else:
            st.write(f"{data['img_path']}が存在しません")
        st.write(f"{data['min_players']} ~ {data['max_players']} 人")
        st.write(f"{data['min_play_time']} ~ {data['max_play_time']} 分")

def main():
    """全体の処理"""
    
    path = "data.json"
    if not os.path.isfile(path):
        st.write("JSONファイル（ゲーム情報があるファイル）が存在しません")
    datas = load_datas(path)

    st.title("ボードゲーム検索アプリ")
    genre, players, play_time = input_to_search()

    perfect, good = game_filter(datas, genre, players, play_time)

    if (genre is not None or players is not None or play_time != 0) and not perfect and not good:
        st.write("条件に一致するゲームはありません")
    else:
        for i in perfect:
            st.text("perfect matchh")
            display(i)
        for i in good:
            st.text("good match")
            display(i)

if __name__ == "__main__":
    main()
    
