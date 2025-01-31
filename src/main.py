import logging

from .bigquery_utils import get_matching_info, initialize_bigquery_client
from .config import OUTPUT_FILE_NAME
from .google_services import initialize_gspread_client, update_sheet


def handler(event, context) -> None:
    # ログの設定
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s:%(message)s",
        handlers=[logging.StreamHandler()],
    )

    bq_client = initialize_bigquery_client()
    results = get_matching_info(bq_client)
    if results is None:
        raise Exception("マッチング情報の取得に失敗しました")
    results.to_csv("/tmp/" + OUTPUT_FILE_NAME, index=False)

    gs_client = initialize_gspread_client()
    flag = update_sheet(gs_client)
    if flag == -1:
        raise Exception("スプレッドシートへのアップロードに失敗しました")
