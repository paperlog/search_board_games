"""ボードゲーム条件絞り込み検索モジュール

ジャンル、プレイ人数、プレイ時間をもとにボードゲーム一覧から絞り込み検索を行う。
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
    perfect=[] #max<条件
    good=[] #min<条件
    for id,data in datas.items():
        judge=0
        if genre!=None:
            if genre  not in data["genre"]:
                continue
        else:
            judge-=1
        if players!=None:
            if data["min_players"] <= players <= data["max_players"]:
                judge+=1
        else:
            judge-=1
        if play_time!=0:
            if play_time>=data["max_play_time"]:
                judge+=100
            elif play_time>=data["min_play_time"]:
                judge+=10
        else:
            judge-=1
        if judge//100==1 and judge%100==1:
            perfect.append(data)
        elif judge//10==1 and judge%10==1:
            good.append(data)
        if judge == -3:
            perfect.append(data)
    return perfect, good

def input_to_search() -> tuple[str | None, int | None, int]:
    """ゲームの絞り込みをするための条件(ジャンル、プレイ人数、プレイ時間)入力"""
    with st.form("is"):
        genre = st.selectbox("ジャンルを選んでください",[None,"協力","対戦","パズル","運"])
        players  = st.selectbox("プレイ人数を選択してください(人)", [None]+list(range(1,21)))
        play_time = st.slider("プレイ時間を選択してください(分)", 0, 240, 0)
        if st.form_submit_button("送信"):
            return genre, players, play_time
        else:
            return None, None, 0

def display(data:dict[str, Any]) -> None:
    """データの表示、テスト用で画像表示なし"""
    with st.container(border=True):
        st.write(data["title"])
        if os.path.isfile(data["img_path"]):
            st.image(data["img_path"], caption = data["title"], width=300)
        else:
            st.write(f"{data["img_path"]}が存在しません")
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
    for i in perfect:
        st.text("perfect matchh")
        display(i)
    for i in good:
        st.text("good match")
        display(i)

if __name__ == "__main__":
    main()
    
