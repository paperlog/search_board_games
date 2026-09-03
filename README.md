# ボードゲームの絞り込みアプリ

## 機能
- プレイ人数、時間でのゲームの絞り込み
- 該当ゲームのタイトルだけでなく画像一覧を表示

## 使い方
- ジャンルをセレクトボックスから選択、複数選択不可
- プレイ人数をセレクトボックスから選択、最大２０
- プレイ時間をスライダーで選択、指定した時間内で終了するゲームを全部表示する
  - perfect: ゲームプレイ時間の想定最大値が収まる
  - good: ゲームプレイ時間の想定最大値は収まらないが想定最小値は収まる

## データ仕様 (`data.json`)

### データ構造
- **id** (`str`): オブジェクトのキー
  - `title` (`str`): ゲームタイトル
  - `img_path` (`str`): 画像パス
  - `genre` (`list[str]`): ジャンル
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
    "genre": ["パズル","対戦"],
    "min_players": 3,
    "max_players": 4,
    "min_play_time": 60,
    "max_play_time": 90
  }
}
```
