import csv
import json
import logging

import boto3
import gspread
from google.oauth2.service_account import Credentials

from .config import (
    BQ_OBJECT_KEY_NAME,
    OUTPUT_FILE_NAME,
    ROOT_BUCKET_NAME,
    SPREADSHEET_KEY,
)


def initialize_gspread_client() -> gspread.Client | None:
    """
    Gspreadクライアントを初期化する。

    Returns:
        gspread.Client: Gspreadクライアント
    """
    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(ROOT_BUCKET_NAME)
        obj = bucket.Object(BQ_OBJECT_KEY_NAME)
        credentials = Credentials.from_service_account_info(
            json.loads(obj.get()["Body"].read().decode("utf-8")),
            scopes=["https://spreadsheets.google.com/feeds"],
        )
        gs_client = gspread.authorize(credentials)
        return gs_client
    except Exception as e:
        logging.error(f"Gspreadクライアントの初期化に失敗しました: {e}")
        return None


def update_sheet(client: gspread.Client) -> int:
    """
    Gspreadにデータをアップロードする。

    Parameters:
        client (gspread.Client): Gspreadクライアント
    """
    try:
        workbook = client.open_by_key(SPREADSHEET_KEY)
        workbook.values_clear("シート1")
        workbook.values_update(
            "シート1",
            params={"valueInputOption": "USER_ENTERED"},
            body={
                "values": list(
                    csv.reader(open("/tmp/" + OUTPUT_FILE_NAME, encoding="utf_8_sig"))
                )
            },
        )
        workbook.worksheet("シート1").set_basic_filter("A1:G10000")
        logging.info("Gspreadへのデータのアップロードが完了しました")
        return 0
    except Exception as e:
        logging.error(f"Gspreadへのデータのアップロードに失敗しました: {e}")
        return -1
