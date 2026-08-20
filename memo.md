# ボードゲームの検索アプリ作成のメモ

## 機能
- プレイ人数、時間でのゲームの絞り込み
- 該当ゲームのタイトルだけでなく画像一覧を表示

## データ
- jsonファイルで管理
- data.json
  - {id:{"title":title,"img_path":img_path,"genre":genre,"min_players":min_players,"max_players":max_players,"min_play_time":min_play_time,"max_paly_time":max_paly_time}}

id: str
title: str
img_path: str
genre: str
min_players: int
max_players: int
min_play_time: int
max_play_itme: int
