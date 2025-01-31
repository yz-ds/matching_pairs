import os

# BQの認証情報
ROOT_BUCKET_NAME = "looker-studio"
BQ_OBJECT_KEY_NAME = "yz-aimatching-41e54dd85f98.json"

# クエリファイル
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUERY_PATH = os.path.join(BASE_DIR, "queries", "query.sql")

# Spreadsheets
SPREADSHEET_KEY = "1qITliFbZlUW760LY5OyR-4cnGspHG1z_yngihYzNDrM"

# 出力ファイル名
OUTPUT_FILE_NAME = "output.csv"
