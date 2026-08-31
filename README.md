# ボードゲームの検索アプリ作成のメモ

## 機能
- プレイ人数、時間でのゲームの絞り込み
- 該当ゲームのタイトルだけでなく画像一覧を表示

## データ仕様 (`data.json`)

### データ構造
- **id** (`str`): オブジェクトのキー
  - `title` (`str`): ゲームタイトル
  - `img_path` (`str`): 画像パス
  - `genre` (`str`): ジャンル
  - `min_players` (`int`): 最小人数
  - `max_players` (`int`): 最大人数
  - `min_play_time` (`int`): 最小プレイ時間
  - `max_play_time` (`int`): 最大プレイ時間

### データ例
```json
{
  "catan": {
    "title": "カタン",
    "img_path": "images/catan.jpg",
    "genre": "ボードゲーム",
    "min_players": 3,
    "max_players": 4,
    "min_play_time": 60,
    "max_play_time": 90
  }
}
```
