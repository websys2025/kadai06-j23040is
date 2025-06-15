# kadai6-1.py
# e-Stat APIを使って、人口推計以外のデータを取得する例
# 選択したデータ: 「労働力調査」(失業率など)
# データ提供元: 総務省統計局
# e-Stat API ドキュメント: https://www.e-stat.go.jp/api/api-info/e-stat-manual

import requests
import json

# 自分のAPIキーを設定（e-Statのサイトで取得する必要があります）
APP_ID = 'ab6ee1d74f2dcaafe198a22bddb444c3f01770d0'

# e-Stat APIのエンドポイント（統計表情報取得）
URL = 'https://api.e-stat.go.jp/rest/3.0/app/getStatsData'

# 労働力調査の統計表ID（例：0003108653は「完全失業率」のデータ）
params = {
    'appId': APP_ID,
    'statsDataId': '0003108653',  # 完全失業率のデータID（例として使用）
    'lang': 'J',
    'metaGetFlg': 'N',
    'cntGetFlg': 'N',
    'explanationGetFlg': 'N',
    'sectionHeaderFlg': '1',
    'csvFlg': 'N'
}

response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    print("データ取得成功\n")

    # データの中から時系列の値を抽出
    for value in data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']:
        time = value["@time"]
        val = value["$"]
        print(f"{time} : {val}")
else:
    print("データ取得に失敗しました:", response.status_code)
